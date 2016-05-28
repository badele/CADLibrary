#! python
# -*- coding: utf-8 -*-

import Part, Draft, math
import FreeCAD, FreeCADGui

# Create document
if FreeCAD.ActiveDocument and FreeCAD.ActiveDocument.Name == "bench":
    FreeCAD.closeDocument("bench")
FreeCAD.newDocument('bench')

INVENTORY = {}


# Get objects by groupname
def getGroupObjects(groupname, begin=True):
    doc = FreeCAD.ActiveDocument
    objects = doc.Objects

    objectslist = []
    for obj in objects:
        if begin:
            if obj.Name.startswith(groupname):
                objectslist.append(obj)
        else:
            if obj.Name == groupname:
                objectslist.append(obj)

    return objectslist


# Convert all parts in one object
def compoundObjects(objectname, objectslist):
    doc = FreeCAD.ActiveDocument
    compound = doc.addObject("Part::Compound", objectname)
    compound.Label = objectname
    compound.Links = objectslist

    FreeCAD.ActiveDocument.recompute()


# Create customized box
def myMakeBox(length=20, width=0, height=0, name="", id=""):
    doc = FreeCAD.ActiveDocument
    cols = doc.getObject('Cols')
    etagere = doc.addObject("Part::Feature", '%(name)s_%(id)s' % locals())
    etagere.Shape = Part.makeBox(length, width, height)

    # Add to inventory
    mini = min(length,width)
    maxi = max(length,width)
    values = '%smm x %smm x %s mm' % (maxi, mini, height)
    values = (maxi, mini, height)

    INVENTORY[name] = INVENTORY.get(name,{})
    INVENTORY[name][values] = INVENTORY[name].get(values,0) + 1

    return etagere

# Show Inventory
def show_inventory():
    for objname in INVENTORY.keys():
        sizename=len(objname)
        print objname
        print "="*sizename
        print

        sizeresult = 0
        for element in INVENTORY[objname].keys():
            width, depth, height = element
            result = "    %s * %smm x %smm x %smm" % (INVENTORY[objname][element], width, depth, height)
            sizeresult = max(sizeresult, len(result)-4)
            print result
        print "    "+"-"*sizeresult
        print ""
        print ""



# Create customized bench
def generate_bench(name='bench'):
    doc = FreeCAD.ActiveDocument

    # Chevrons
    obj = myMakeBox(RAFTER_WIDTH, RAFTER_HEIGHT,RAFTER_Z1*BOARD_HEIGHT, name=name, id="chevron gauche front")
    obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
    obj.Placement.Base = FreeCAD.Vector(COL2X,ROW2Y , 0)

    obj = myMakeBox(RAFTER_WIDTH, RAFTER_HEIGHT,RAFTER_Z2*BOARD_HEIGHT, name=name, id="chevron gauche back")
    obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
    obj.Placement.Base = FreeCAD.Vector(COL2X, ROW4Y, 0)

    obj = myMakeBox(RAFTER_WIDTH, RAFTER_HEIGHT,RAFTER_Z1*BOARD_HEIGHT, name=name, id="chevron droite front")
    obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
    obj.Placement.Base = FreeCAD.Vector(COL3X,+ROW2Y , 0)

    obj = myMakeBox(RAFTER_WIDTH, RAFTER_HEIGHT,RAFTER_Z2*BOARD_HEIGHT, name=name, id="chevron droite back")
    obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
    obj.Placement.Base = FreeCAD.Vector(COL3X, ROW4Y, 0)

    for z in range(0,RAFTER_Z1):
        # Planche left
        obj = myMakeBox(BOARD_WIDTH, BANCPROFONDEUR-(3*BOARD_WIDTH),BOARD_HEIGHT, name=name,id="planche left 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0, ROW2Y, z*BOARD_HEIGHT)

        # Planche right
        obj = myMakeBox(BOARD_WIDTH, BANCPROFONDEUR-(3*BOARD_WIDTH),BOARD_HEIGHT, name=name,id="planche right 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(COL4X, BOARD_WIDTH, z*BOARD_HEIGHT)

        # Planche front
        obj = myMakeBox(BOARD_LENGTH, BOARD_WIDTH,BOARD_HEIGHT, name=name,id="planche front 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0, 0, z*BOARD_HEIGHT)


    for z in range(RAFTER_Z1,RAFTER_Z2):
        # Planche left min
        obj = myMakeBox(BOARD_WIDTH, RAFTER_HEIGHT,BOARD_HEIGHT, name=name,id="planche min left 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0, ROW4Y, z*BOARD_HEIGHT)

        # Planche right min
        obj = myMakeBox(BOARD_WIDTH, RAFTER_HEIGHT,BOARD_HEIGHT, name=name,id="planche min right 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(COL4X, ROW4Y, z*BOARD_HEIGHT)

        # Planche middle
        obj = myMakeBox(BOARD_LENGTH, BOARD_WIDTH,BOARD_HEIGHT, name=name,id="planche middle 4")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0, ROW3Y, z*BOARD_HEIGHT)


    # Planche back
    for z in range(0,RAFTER_Z2):
        obj = myMakeBox(BOARD_LENGTH, BOARD_WIDTH,BOARD_HEIGHT, name=name,id="planche back 1")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0, ROW5Y, z*BOARD_HEIGHT)

    # Top
    obj = myMakeBox(BOARD_LENGTH, RAFTER_HEIGHT+(2*BOARD_WIDTH),BOARD_WIDTH, name=name, id="planche top")
    obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
    obj.Placement.Base = FreeCAD.Vector(0, ROW3Y, RAFTER_Z2*BOARD_HEIGHT)

    # Generates other objets
    generate_cover(name="%(name)s_cover" % locals())
    generate_pillow(name="%(name)s_pillow" % locals())

    # Compound object
    objs = getGroupObjects(name)
    compoundObjects(name, objs)


    return doc.getObject(name)


def generate_cover(name="bench"):
    for y in range(0,SEAT):
        obj = myMakeBox(BOARD_LENGTH, BOARD_HEIGHT,BOARD_WIDTH, name=name, id="chevron gauche front")
        obj.ViewObject.ShapeColor = (0.76, 0.64, 0.45)
        obj.Placement.Base = FreeCAD.Vector(0,y*BOARD_HEIGHT, RAFTER_Z1*BOARD_HEIGHT)


def generate_pillow(name="bench"):
    obj = myMakeBox(BOARD_LENGTH-20, SEAT*BOARD_HEIGHT-20,45, name=name, id="")
    obj.ViewObject.ShapeColor = (0.27, 0.80, 0.80)
    obj.ViewObject.Transparency = 80
    obj.Placement.Base = FreeCAD.Vector(10,10, (RAFTER_Z1*BOARD_HEIGHT)+BOARD_WIDTH)


# Global Parameters


BOARD_LENGTH=400
BOARD_WIDTH=20
BOARD_HEIGHT=100

RAFTER_WIDTH=80
RAFTER_HEIGHT=80
RAFTER_Z1= 3
RAFTER_Z2= 6

SEAT=4
BANCPROFONDEUR=(SEAT*BOARD_HEIGHT)+RAFTER_HEIGHT+(3*BOARD_WIDTH)
BANCWIDTH=1600


COL1X = 0
COL2X = COL1X+BOARD_WIDTH
COL3X = COL1X+BOARD_LENGTH-RAFTER_WIDTH-BOARD_WIDTH
COL4X = COL3X+RAFTER_WIDTH

ROW1Y = 0
ROW2Y = BOARD_WIDTH
ROW3Y = ROW2Y+(SEAT*BOARD_HEIGHT)-BOARD_WIDTH
ROW4Y = ROW3Y+BOARD_WIDTH
ROW5Y = ROW4Y+RAFTER_HEIGHT

# Generate benchs
NBBENCHS=3
for x in range(0,NBBENCHS):
    obj = generate_bench(name="bench_%(x)s" % locals())
    obj.Placement.Base = FreeCAD.Vector(x*BOARD_LENGTH, 0, 0)

show_inventory()