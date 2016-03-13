// Etagère
EEPAISSEUR=20;
ELARGEUR1=250;
ELARGEUR2=500;
EPROFONDEUR=400;
EHAUTEUR=300;
WPOIGNE=80;
HPOIGNE=20;
JEUTIRROIR=5;
HTIRROIR=EHAUTEUR-20;

// Colonnes
COL1=0;
COL2=EEPAISSEUR+ELARGEUR1;
COL3=COL2+EEPAISSEUR+ELARGEUR1;
COL4=COL3+EEPAISSEUR+(ELARGEUR2);
COL5=COL4+EEPAISSEUR+(ELARGEUR2);

// Lignes
ROW0=0;
ROW1=EHAUTEUR;
ROW2=ROW1+EEPAISSEUR+EHAUTEUR;
ROW3=ROW2+EEPAISSEUR+EHAUTEUR;
ROW4=ROW3+EEPAISSEUR+EHAUTEUR;
ROW5=ROW4+EEPAISSEUR+EHAUTEUR;
ROW6=ROW5+EEPAISSEUR+EHAUTEUR;
ROW7=ROW6+EEPAISSEUR+EHAUTEUR;
ROW8=ROW7+EEPAISSEUR+EHAUTEUR;
ROW9=ROW8+EEPAISSEUR+EHAUTEUR;

// Piece
PIECEHAUTEUR=3000;
PIECELARGEUR=2520;
PIECELONGEUR=3660;
FENETRELARGEUR=1400;
FENETREHAUTEUR=1800;
FENETREPOSX=170;
FENETREPOSZ=900;
PRISEWIDTH=80;
PRISEPOSZ=230;
PRISEPOSX=1360;
PORTELARGEUR=910;
PORTEHAUTEUR=2150;
PORTEPOS=PRISEPOSX+PRISEWIDTH+100;

// Meuble
MHAUTEUR=ROW9+EEPAISSEUR;
LITLARGEUR=1400;
LITLONGEUR=1900;
LITPOSY=1700;

// Cylinder Resolution
$fn=50;


// Etagère Horizontal
module etagere_horizontal(largeur=ELARGEUR1,profondeur=EPROFONDEUR,epaisseur=EEPAISSEUR) {
        cube ( [largeur,profondeur,epaisseur]);
};

// Etagère Vertical
module etagere_vertical(hauteur=EHAUTEUR1,profondeur=EPROFONDEUR,epaisseur=EEPAISSEUR) {
        cube ( [epaisseur,profondeur,hauteur]);
};

// Tirroir
module tirroir (largeur=ELARGEUR1,profondeur=EPROFONDEUR,hauteur=HTIRROIR,epaisseur=EEPAISSEUR) {
    wtirroir = largeur - (2*JEUTIRROIR);
    htirroir = hauteur - (2*JEUTIRROIR);
    translate ([JEUTIRROIR,0,JEUTIRROIR]) {
        difference () {
            difference () {
                // Tirroir
                cube ( [wtirroir,profondeur,htirroir]);
                // Vide
                translate ([epaisseur,epaisseur,epaisseur]) {    
                    cube ( [wtirroir-2*epaisseur,profondeur-2*epaisseur,hauteur]);
                }
            }
            // POIGNE
            translate ([(wtirroir-WPOIGNE)/2,EEPAISSEUR+epaisseur/2,hauteur-HPOIGNE]) 
            rotate([90,0,0]) 
            minkowski()
            {
                cube ( [WPOIGNE,epaisseur,HPOIGNE]);
                cylinder(r=HPOIGNE/4,h=HPOIGNE);
            }
        }
    }
}

// Mur de la chambre
module mur() {
    // Porte
    difference () {
        cube ([PIECELARGEUR, 1,PIECEHAUTEUR]);
        translate ([PORTEPOS,-EEPAISSEUR*1,0]) cube ([PORTELARGEUR,EEPAISSEUR*2,PORTEHAUTEUR]); 
    }
    // Fenetre
    difference () {
        translate ([0,-PIECELONGEUR,0]) cube ([PIECELARGEUR, 1,PIECEHAUTEUR]); // Mur
        translate ([FENETREPOSX,-EEPAISSEUR-PIECELONGEUR,FENETREPOSZ]) cube ([FENETRELARGEUR,EEPAISSEUR*2,FENETREHAUTEUR]); // Vide Fenetre        
    }
    mirror ([0,1,0]) cube ([1, PIECELONGEUR,PIECEHAUTEUR]);
    translate ([PIECELARGEUR,0,0]) mirror ([0,1,0]) cube ([1, PIECELONGEUR,PIECEHAUTEUR]);
}

// Prise electrique
module prise () {
    color ([1,0,0]) cube ([PRISEWIDTH,EEPAISSEUR,PRISEWIDTH]);
}

// Emplacement lit
module lit() {
    cube ([LITLONGEUR,LITLARGEUR,500]);
}

// Placar
module placar () {
// Montant
translate([COL1,0,0]) etagere_vertical(hauteur=MHAUTEUR);
translate([COL2,0,0]) etagere_vertical(hauteur=MHAUTEUR-2*(EHAUTEUR+EEPAISSEUR));
translate([COL3,0,0]) etagere_vertical(hauteur=MHAUTEUR);
translate([COL4,0,0]) etagere_vertical(hauteur=MHAUTEUR);
translate([COL5,0,0]) etagere_vertical(hauteur=MHAUTEUR);


// Etagère colone 1
translate([COL1+EEPAISSEUR,0,ROW1]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW2]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW3]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW4]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW5]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW6]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1+EEPAISSEUR,0,ROW7]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
//translate([COL1+EEPAISSEUR,0,ROW8]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1);
translate([COL1,0,ROW9]) etagere_horizontal(largeur=EEPAISSEUR+2*ELARGEUR1+2*EEPAISSEUR);

// Etagère colone 3
translate([COL3+EEPAISSEUR,0,ROW1]) etagere_horizontal(largeur=ELARGEUR2);
translate([COL3+EEPAISSEUR,0,ROW2]) etagere_horizontal(largeur=ELARGEUR2);
translate([COL3+EEPAISSEUR,0,ROW3]) etagere_horizontal(largeur=ELARGEUR2);
translate([COL3+EEPAISSEUR,0,ROW7]) etagere_horizontal(largeur=ELARGEUR2);
translate([COL3+EEPAISSEUR,0,ROW9]) etagere_horizontal(largeur=ELARGEUR2);

// Etagère colone 5
translate([COL4+EEPAISSEUR,0,ROW1]) etagere_horizontal(largeur=2*ELARGEUR1);
translate([COL4+EEPAISSEUR,0,ROW2]) etagere_horizontal(largeur=2*ELARGEUR1);
translate([COL4+EEPAISSEUR,0,ROW3]) etagere_horizontal(largeur=2*ELARGEUR1);
translate([COL4+EEPAISSEUR,0,ROW5]) etagere_horizontal(largeur=2*ELARGEUR1);
translate([COL4+EEPAISSEUR,0,ROW7]) etagere_horizontal(largeur=2*ELARGEUR1);
translate([COL4+EEPAISSEUR,0,ROW9]) etagere_horizontal(largeur=2*ELARGEUR1);


// Tirroir colone 1
translate([COL1+EEPAISSEUR,0,ROW0]) tirroir(hauteur=HTIRROIR);
translate([COL1+EEPAISSEUR,0,ROW1+EEPAISSEUR]) tirroir();
translate([COL1+EEPAISSEUR,0,ROW2+EEPAISSEUR]) tirroir();

// Tirroir colone 2
translate([COL2+EEPAISSEUR,0,ROW0]) tirroir();
translate([COL2+EEPAISSEUR,0,ROW1+EEPAISSEUR]) tirroir();
translate([COL2+EEPAISSEUR,0,ROW2+EEPAISSEUR]) tirroir();

// Tirroir colone 3
translate([COL3+EEPAISSEUR,0,ROW0]) tirroir(largeur=ELARGEUR2);
translate([COL4+EEPAISSEUR,0,ROW0]) tirroir(largeur=ELARGEUR2);
}

///////////////////////
// Main
///////////////////////
//%color ([1,1,1,0.2]) mur();
//translate ([0,-LITPOSY-LITLARGEUR,0]) lit();

translate ([0,-EPROFONDEUR,0]) placar();
translate ([PRISEPOSX,0,PRISEPOSZ]) prise();
