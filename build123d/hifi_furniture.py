import random
from collections import defaultdict

from ocp_vscode import *

from build123d import *


def side_panel(width, depth, height):
    with BuildPart() as part:
        with BuildSketch():
            Rectangle(width, depth, align=(Align.MIN, Align.MIN))
        extrude(amount=height)
    return part.part


########################################################################################
# Parameters
########################################################################################

THICKNESS = 18
VINYLE_HL = 325

MEUBLE_NOIR_LARGEUR = 1010
MEUBLE_NOIR_PROFONDEUR = 330
MEUBLE_NOIR_HAUTEUR = 790
MEUBLE_NOIR_EPAISSEUR = 50

HIFI_LARGEUR = 365
HIFI_HAUTEUR = 400
HIFI_PROFONDEUR = 400

SOCLE_HAUTEUR = THICKNESS


########################################################################################
# Class and Functions
########################################################################################
class BOM:
    def __init__(self):
        self.entries = []

    def add(self, shape, thickness):
        self.entries.append((shape, thickness))

    def _iter_leaf_parts(self, shape):
        children = getattr(shape, "children", None)
        if children:
            for child in children:
                yield from self._iter_leaf_parts(child)
        else:
            yield shape

    def build(self):
        bom = defaultdict(lambda: {"qty": 0, "labels": []})

        for shape, thickness in self.entries:
            for part in self._iter_leaf_parts(shape):
                bbox = part.bounding_box()
                dims = sorted(
                    [
                        bbox.size.X,
                        bbox.size.Y,
                        bbox.size.Z,
                    ]
                )

                # Remplace la plus petite dimension par l'épaisseur métier
                dims[0] = thickness

                key = (dims[0], dims[1], dims[2])

                bom[key]["qty"] += 1

                label = getattr(part, "label", None) or "unnamed"
                if label not in bom[key]["labels"]:
                    bom[key]["labels"].append(label)

        return bom

    def print(self):
        bom = self.build()

        def fmt(x):
            return f"{x:g}"

        rows = []
        for (thickness, d1, d2), data in sorted(
            bom.items(), key=lambda x: (x[0][0], x[0][1], x[0][2])
        ):
            qty = str(data["qty"])
            thickness_txt = f"{fmt(thickness)} mm"
            dims_txt = f"{fmt(d1)} mm x {fmt(d2)} mm"
            labels = ", ".join(data["labels"])

            rows.append((qty, thickness_txt, dims_txt, labels))

        headers = ("Qty", "Thickness", "Dimensions (mm)", "Labels")

        w_qty = max(len(headers[0]), *(len(r[0]) for r in rows))
        w_thickness = max(len(headers[1]), *(len(r[1]) for r in rows))
        w_dims = max(len(headers[2]), *(len(r[2]) for r in rows))
        w_labels = max(len(headers[3]), *(len(r[3]) for r in rows))

        print(
            f"| {'Qty':>{w_qty}} "
            f"| {'Thickness':>{w_thickness}} "
            f"| {'Dimensions (mm)':<{w_dims}} "
            f"| {'Labels':<{w_labels}} |"
        )
        print(
            f"|{'-' * (w_qty +1)}:|"
            f"{'-' * (w_thickness+1)}:|"
            f":{'-' * (w_dims+1)}|"
            f":{'-' * (w_labels+1)}|"
        )

        for qty, thickness_txt, dims_txt, labels in rows:
            print(
                f"| {qty:>{w_qty}} "
                f"| {thickness_txt:>{w_thickness}} "
                f"| {dims_txt:<{w_dims}} "
                f"| {labels:<{w_labels}} |"
            )


def box(
    inner_width, inner_depth, inner_height, thickness, back_tickness, shelf_positions
):
    with BuildPart() as model:
        add(
            side_panel(inner_width + 2 * thickness, inner_depth, thickness).located(
                Location((0, 0, 0))
            )
        )

        for z in shelf_positions:
            add(
                side_panel(inner_width, inner_depth, thickness).located(
                    Location((thickness, 0, thickness + z))
                )
            )

        add(
            side_panel(inner_width + 2 * thickness, inner_depth, thickness).located(
                Location((0, 0, inner_height + thickness))
            )
        )

        add(
            side_panel(thickness, inner_depth, inner_height).located(
                Location((0, 0, thickness))
            )
        )

        add(
            side_panel(thickness, inner_depth, inner_height).located(
                Location((inner_width + thickness, 0, thickness))
            )
        )

        if back_tickness > 0:
            add(
                side_panel(
                    inner_width + 2 * thickness,
                    back_tickness,
                    inner_height + 2 * thickness,
                ).located(Location((0, inner_depth, 0)))
            )

    return model.part


def make_hifi_box(width, depth, height, x, y, z, back_thickness=0, color="black"):
    with BuildPart() as bp:
        add(
            side_panel(width, depth - back_thickness, height).located(
                Location((x, y, z))
            )
        )
        if back_thickness > 0:
            add(
                side_panel(width + 5, 5, 5).located(Location((x, y, z + 30))),
                mode=Mode.SUBTRACT,
            )
    bp.part.color = Color(color)
    return bp.part


bom = BOM()

########################################################################################
# meuble noir
########################################################################################

meuble_noir_gauche = side_panel(
    MEUBLE_NOIR_EPAISSEUR, MEUBLE_NOIR_PROFONDEUR, MEUBLE_NOIR_HAUTEUR
).located(Location((0, 0, 0)))
meuble_noir_gauche.color = Color("black")
meuble_noir_gauche.label = "meuble_noir_gauche"

meuble_noir_droite = side_panel(
    MEUBLE_NOIR_EPAISSEUR, MEUBLE_NOIR_PROFONDEUR, MEUBLE_NOIR_HAUTEUR
).located(Location((MEUBLE_NOIR_LARGEUR - MEUBLE_NOIR_EPAISSEUR, 0, 0)))
meuble_noir_droite.color = Color("black")
meuble_noir_droite.label = "meuble_noir_droite"

meuble_noir_plateau = side_panel(
    MEUBLE_NOIR_LARGEUR, MEUBLE_NOIR_PROFONDEUR, MEUBLE_NOIR_EPAISSEUR
).located(Location((0, 0, MEUBLE_NOIR_HAUTEUR - MEUBLE_NOIR_EPAISSEUR)))
meuble_noir_plateau.color = Color("black")
meuble_noir_plateau.label = "meuble_noir_plateau"

meuble_noir = Compound(
    children=[meuble_noir_gauche, meuble_noir_droite, meuble_noir_plateau]
)
meuble_noir.label = "meuble_noir"
bom.add(meuble_noir, MEUBLE_NOIR_EPAISSEUR)


########################################################################################
# Socle / structure haute
########################################################################################

block = box(
    inner_width=MEUBLE_NOIR_LARGEUR,
    inner_depth=SOCLE_HAUTEUR,
    inner_height=MEUBLE_NOIR_PROFONDEUR,
    thickness=THICKNESS,
    back_tickness=0,
    shelf_positions=[],
).located(
    Location(
        (
            -THICKNESS,
            MEUBLE_NOIR_PROFONDEUR + THICKNESS,
            MEUBLE_NOIR_HAUTEUR - THICKNESS,
        ),
        (90, 0, 0),
    ),
)
block.color = Color("#C89A68")
block.label = "socle"

BASE_LARGEUR = (
    THICKNESS
    + VINYLE_HL
    + 10
    + THICKNESS
    + HIFI_LARGEUR
    + THICKNESS
    + VINYLE_HL
    + 10
    + THICKNESS
)

back_tickness = THICKNESS

base = side_panel(BASE_LARGEUR, HIFI_PROFONDEUR + THICKNESS, THICKNESS).located(
    Location(
        (-(BASE_LARGEUR - MEUBLE_NOIR_LARGEUR) / 2, -THICKNESS, MEUBLE_NOIR_HAUTEUR)
    )
)
base.color = Color("#C89A68")
base.label = "base"

fond = side_panel(
    BASE_LARGEUR - 2 * THICKNESS, THICKNESS, HIFI_HAUTEUR + THICKNESS
).located(
    Location(
        (
            base.bounding_box().min.X + THICKNESS,
            base.bounding_box().max.Y - THICKNESS,
            base.bounding_box().max.Z,
        )
    )
)
fond.color = Color("#C89A68")
fond.label = "fond"

gauche = side_panel(
    THICKNESS, HIFI_PROFONDEUR + THICKNESS, HIFI_HAUTEUR + THICKNESS
).located(
    Location(
        (
            base.bounding_box().min.X,
            base.bounding_box().min.Y,
            base.bounding_box().max.Z,
        )
    )
)
gauche.color = Color("#C89A68")
gauche.label = "gauche"

gauche_facade = side_panel(VINYLE_HL + 10, THICKNESS, VINYLE_HL / 2 + 10).located(
    Location(
        (
            gauche.bounding_box().max.X,
            gauche.bounding_box().min.Y,
            gauche.bounding_box().min.Z,
        )
    )
)
gauche_facade.color = Color("#C89A68")
gauche_facade.label = "gauche_facade"

gauche_hifi = side_panel(THICKNESS, HIFI_PROFONDEUR, HIFI_HAUTEUR).located(
    Location(
        (
            gauche.bounding_box().max.X + VINYLE_HL + 10,
            base.bounding_box().min.Y,
            base.bounding_box().max.Z,
        )
    )
)
gauche_hifi.color = Color("#C89A68")
gauche_hifi.label = "gauche_hifi"

droite_hifi = side_panel(THICKNESS, HIFI_PROFONDEUR, HIFI_HAUTEUR).located(
    Location(
        (
            gauche_hifi.bounding_box().max.X + HIFI_LARGEUR,
            base.bounding_box().min.Y,
            base.bounding_box().max.Z,
        )
    )
)
droite_hifi.color = Color("#C89A68")
droite_hifi.label = "droite_hifi"

droite_facade = side_panel(VINYLE_HL + 10, THICKNESS, VINYLE_HL / 2 + 10).located(
    Location(
        (
            droite_hifi.bounding_box().max.X,
            droite_hifi.bounding_box().min.Y,
            droite_hifi.bounding_box().min.Z,
        )
    )
)
droite_facade.color = Color("#C89A68")
droite_facade.label = "droite_facade"

support_platine = side_panel(
    HIFI_LARGEUR + 2 * THICKNESS, HIFI_PROFONDEUR, THICKNESS
).located(
    Location(
        (
            gauche_hifi.bounding_box().min.X,
            gauche_hifi.bounding_box().min.Y,
            gauche_hifi.bounding_box().max.Z,
        )
    )
)
support_platine.color = Color("#C89A68")
support_platine.label = "support_platine"

droite = side_panel(
    THICKNESS, HIFI_PROFONDEUR + THICKNESS, HIFI_HAUTEUR + THICKNESS
).located(
    Location(
        (
            base.bounding_box().max.X - THICKNESS,
            base.bounding_box().min.Y,
            base.bounding_box().max.Z,
        )
    )
)
droite.color = Color("#C89A68")
droite.label = "droite"

meuble_haut = Compound(
    children=[
        block,
        base,
        fond,
        gauche,
        gauche_facade,
        gauche_hifi,
        droite_hifi,
        droite_facade,
        support_platine,
        droite,
    ]
)
meuble_haut.label = "meuble_haut"
bom.add(meuble_haut, THICKNESS)


########################################################################################
# Chaine hifi
########################################################################################

hifi_x = MEUBLE_NOIR_LARGEUR - 690 - 34 + 2 * THICKNESS
hifi_y = -THICKNESS
hifi_z0 = base.bounding_box().max.Z

lecteur_cd = make_hifi_box(365, 400, 85, hifi_x, hifi_y, hifi_z0, back_tickness)
lecteur_cd.label = "lecteur_cd"

lecteur_k7 = make_hifi_box(
    365,
    400,
    115,
    hifi_x,
    hifi_y,
    lecteur_cd.bounding_box().max.Z + 5,
    back_tickness,
)
lecteur_k7.label = "lecteur_k7"

ampli = make_hifi_box(
    365,
    400,
    115,
    hifi_x,
    hifi_y,
    lecteur_k7.bounding_box().max.Z + 5,
    back_tickness,
)
ampli.label = "ampli"

tuner = make_hifi_box(
    365,
    400,
    60,
    hifi_x,
    hifi_y,
    ampli.bounding_box().max.Z + 5,
    0,
)
tuner.label = "tuner"

chaine_hifi = Compound(children=[lecteur_cd, lecteur_k7, ampli, tuner])
chaine_hifi.label = "chaine_hifi"


########################################################################################
# Platine
########################################################################################

vinyle = side_panel(430, 350, 30).located(
    Location((290, 0, support_platine.bounding_box().max.Z))
)
vinyle.color = Color("#aaaaaa")
vinyle.label = "platine_base"

vinyle_capot = side_panel(420, 320, 45).located(
    Location((295, 0, support_platine.bounding_box().max.Z + 30))
)
vinyle_capot.color = Color("#aaaaaa", alpha=0.2)
vinyle_capot.label = "platine_capot"

with BuildPart() as vinyle_plateau_bp:
    with Locations((503, 175, support_platine.bounding_box().max.Z + 30)):
        Cylinder(radius=160, height=8)
vinyle_plateau = vinyle_plateau_bp.part
vinyle_plateau.color = Color("black")
vinyle_plateau.label = "platine_plateau"

with BuildPart() as bras_platine_bp:
    with Locations((520, -27, 0)):
        Cylinder(radius=THICKNESS, height=12)

    with Locations((520, -27, 12)):
        Cylinder(radius=4, height=THICKNESS)

    with Locations((455, -27, 24)):
        Box(130, 12, 8, align=(Align.CENTER, Align.CENTER, Align.MIN))

    with Locations((525, -27, 24)):
        Cylinder(radius=10, height=20, rotation=(0, 90, 0))

    with Locations((388, -27, 22)):
        Box(22, THICKNESS, 6, align=(Align.CENTER, Align.CENTER, Align.MIN))

    with Locations((382, -27, 16)):
        Box(8, 4, 6, align=(Align.CENTER, Align.CENTER, Align.MIN))

bras_platine = bras_platine_bp.part.located(
    Location((300, -60, support_platine.bounding_box().max.Z + 30), (0, 0, 45))
)
bras_platine.color = Color("#333333")
bras_platine.label = "bras_platine"

platine = Compound(children=[vinyle, vinyle_capot, vinyle_plateau, bras_platine])
platine.label = "platine"


########################################################################################
# Vinyles
########################################################################################

colors = [
    "#330000",
    "#003300",
    "#000033",
    "#663300",
    "#336666",
    "#660000",
    "#990000",
    "#7A1F1F",
    "#004d00",
    "#006633",
    "#2E8B57",
    "#000066",
    "#003366",
    "#1F3A5F",
    "#4B2E2E",
    "#5C4033",
    "#8B4513",
    "#2F4F4F",
    "#696969",
    "#A9A9A9",
    "#4B0082",
    "#800080",
    "#008080",
    "#556B2F",
]

nb_vinyles = 65
spacing = 5

vinyles = []
for i in range(nb_vinyles):
    vinyl = side_panel(320, 320, 2).located(
        Location((-2 * THICKNESS, i * spacing - 10, 822), (80, 0, 0))
    )
    vinyl.color = Color(random.choice(colors))
    vinyl.label = f"vinyle_gauche_{i:02d}"
    vinyles.append(vinyl)

vinyles_gauche = Compound(children=vinyles)
vinyles_gauche.label = "vinyles_gauche"


vinyles = []
for i in range(nb_vinyles):
    vinyl = side_panel(320, 320, 2).located(
        Location((758 - 2 * THICKNESS, i * spacing, 822), (80, 0, 0))
    )
    vinyl.color = Color(random.choice(colors))
    vinyl.label = f"vinyle_droite_{i:02d}"
    vinyles.append(vinyl)

vinyles_droite = Compound(children=vinyles)
vinyles_droite.label = "vinyles_droite"


########################################################################################
# Assemblage final
########################################################################################

scene = Compound(
    children=[
        meuble_noir,
        meuble_haut,
        chaine_hifi,
        platine,
        vinyles_gauche,
        vinyles_droite,
    ]
)
scene.label = "scene"


########################################################################################
# Export & Display
########################################################################################

bom.print()


show(scene)
