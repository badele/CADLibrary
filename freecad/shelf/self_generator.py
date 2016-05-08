#! python
# -*- coding: utf-8 -*-

import Part, Draft, math
import FreeCAD, FreeCADGui

# Create document
if FreeCAD.ActiveDocument and FreeCAD.ActiveDocument.Name == "shelf":
    FreeCAD.closeDocument("shelf")
FreeCAD.newDocument('shelf')

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


# Create horizontal shelf
def horizontal_shelf(length=0, width=0, height=20, pos=FreeCAD.Vector(), name="", id=""):
    doc = FreeCAD.ActiveDocument
    rows = doc.getObject('Rows')
    etagere = doc.addObject("Part::Feature", '%(name)s_horizontal%(id)s' % locals())
    etagere.Shape = Part.makeBox(length, width, height, pos)

    # Add to inventory
    mini = min(length,width)
    maxi = max(length,width)
    values = '%smm x %smm x %s mm' % (maxi, mini, height)
    values = (maxi, mini, height)

    INVENTORY[name] = INVENTORY.get(name,{})
    INVENTORY[name][values] = INVENTORY[name].get(values,0) + 1



# Create vertical shelf
def vertical_shelf(length=20, width=0, height=0, pos=FreeCAD.Vector(), name="", id=""):
    doc = FreeCAD.ActiveDocument
    cols = doc.getObject('Cols')
    etagere = doc.addObject("Part::Feature", '%(name)s_vertical%(id)s' % locals())
    etagere.Shape = Part.makeBox(length, width, height, pos)

    # Add to inventory
    mini = min(length,length)
    maxi = max(length,length)
    values = '%smm x %smm x %s mm' % (maxi, mini, height)
    values = (maxi, mini, height)

    INVENTORY[name] = INVENTORY.get(name,{})
    INVENTORY[name][values] = INVENTORY[name].get(values,0) + 1


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

def DrawDim(p1,p2,p3,name,extlines=250):
    # Dimension
    dim = Draft.makeDimension(p1,p2,p3)
    dim.Label = name
    dim.ViewObject.DisplayMode ="3D"
    dim.ViewObject.ExtLines = extlines
    dim.ViewObject.Decimals = 0
    dim.ViewObject.ArrowType = "Arrow"
    dim.ViewObject.ArrowSize = 0
    dim.ViewObject.FontSize = 0.2
    dim.ViewObject.TextSpacing = 200
    dim.ViewObject.LineColor = (0.75, 0.75, 0.75)


# Create customized shelf
def generate_self(nbcols=2, nbrows=8, colwidth=250, rowhight=300, depth=400, woodwidth=20, name='etagere',
                  ignorerows=[]):
    doc = FreeCAD.ActiveDocument

    # Compute shelf dimension
    allwidth = nbcols * (colwidth + woodwidth) + woodwidth
    allhigth = nbrows * (rowhight + woodwidth) + woodwidth

    # Top and bottom
    horizontal_shelf(allwidth, depth, woodwidth, FreeCAD.Vector(0, 0, 0), name=name, id="bottom")
    horizontal_shelf(allwidth, depth, woodwidth, FreeCAD.Vector(0, 0, allhigth), name=name, id="top")

    # Left and Right
    vertical_shelf(woodwidth, depth, allhigth - woodwidth, pos=FreeCAD.Vector(0, 0, woodwidth), name=name, id="left")
    vertical_shelf(woodwidth, depth, allhigth - woodwidth, pos=FreeCAD.Vector(allwidth - woodwidth, 0, woodwidth),
                   name=name, id="right")

    # Cols
    for x in range(0, nbcols):
        posx = x * (woodwidth + colwidth) + woodwidth
        if x > 0:
            vertical_shelf(woodwidth, depth, allhigth - woodwidth, pos=FreeCAD.Vector(posx - woodwidth, 0, woodwidth),
                           name=name, id=x)

        for z in range(0, nbrows):
            posz = z * (woodwidth + rowhight)
            if z > 0 and z not in ignorerows:
                horizontal_shelf(colwidth, depth, woodwidth, pos=FreeCAD.Vector(posx, 0, posz), name=name, id=z)

    # Compound object
    objs = getGroupObjects(name)
    compoundObjects(name, objs)

    return doc.getObject(name)


# Global Parameters
DEPTH=400
WOODWIDTH=20
NBROWS=9
ROWHIGHT=300
DIMLEVEL1=2*ROWHIGHT
DIMLEVEL2=ROWHIGHT
NBCOL1=2
NBCOL2=1
NBCOL3=1
WIDTHCOL1=250
WIDTHCOL2=500
WIDTHCOL3=500

# Compute values
totalhight = NBROWS*(ROWHIGHT+WOODWIDTH)+(2*WOODWIDTH)
col1=0
col2=WOODWIDTH+NBCOL1*(WOODWIDTH+WIDTHCOL1)
col3=col2+2*WOODWIDTH+WIDTHCOL2
totalwidth = col3+2*WOODWIDTH+WIDTHCOL3

# Left Part
shelfA = generate_self(nbcols=NBCOL1, nbrows=NBROWS, rowhight=ROWHIGHT, colwidth=WIDTHCOL1, name='meuble_gauche', depth=DEPTH, woodwidth=WOODWIDTH)
shelfA.ViewObject.ShapeColor = (0.80, 0.80, 0.40)

# Central part
shelfB = generate_self(nbcols=NBCOL2, nbrows=NBROWS, rowhight=ROWHIGHT, colwidth=WIDTHCOL2, ignorerows=[5, 6, 7], name='meuble_central', depth=DEPTH, woodwidth=WOODWIDTH)
shelfB.Placement.Base = FreeCAD.Vector(col2, 0, 0)
shelfB.ViewObject.ShapeColor = (0.27, 0.80, 0.80)

# Right part
shelfC = generate_self(nbcols=NBCOL3, nbrows=NBROWS, rowhight=ROWHIGHT, colwidth=WIDTHCOL3, ignorerows=[5, 7], name='meuble_droit', depth=DEPTH, woodwidth=WOODWIDTH)
shelfC.Placement.Base = FreeCAD.Vector(col3, 0, 0)
shelfC.ViewObject.ShapeColor = (0.80, 0.53, 0.80)

#Init Dimensions
FreeCADGui.activateWorkbench("DraftWorkbench")

# Horizontal plane
p1 = FreeCAD.Vector(col1,0,0)
p2 = FreeCAD.Vector(col2,0,0)
p3 = FreeCAD.Vector(0,-DIMLEVEL1,0)
DrawDim(p1,p2,p3,"Col 1",extlines=DIMLEVEL1-50)
#
for i in range(NBCOL1):
    p1 = FreeCAD.Vector(col1+WOODWIDTH+(i*(WIDTHCOL1+WOODWIDTH)),0,0)
    p2 = FreeCAD.Vector(col1+WOODWIDTH+(i*(WIDTHCOL1+WOODWIDTH))+250,0,0)
    p3 = FreeCAD.Vector(0,-DIMLEVEL2,0)
    DrawDim(p1,p2,p3,"Col 1.%(i)s" % locals(),extlines=DIMLEVEL2-50)
#
p1 = FreeCAD.Vector(col2,0,0)
p2 = FreeCAD.Vector(col3,0,0)
p3 = FreeCAD.Vector(0,-DIMLEVEL1,0)
DrawDim(p1,p2,p3,"Col 2",extlines=DIMLEVEL1-50)
#
p1 = FreeCAD.Vector(col2+WOODWIDTH,0,0)
p2 = FreeCAD.Vector(col3-WOODWIDTH,0,0)
p3 = FreeCAD.Vector(0,-DIMLEVEL2,0)
DrawDim(p1,p2,p3,"Col 2.1",extlines=DIMLEVEL2-50)
#
p1 = FreeCAD.Vector(col3,0,0)
p2 = FreeCAD.Vector(col3+2*WOODWIDTH+500,0,0)
p3 = FreeCAD.Vector(0,-DIMLEVEL1,0)
DrawDim(p1,p2,p3,"Col 3",extlines=DIMLEVEL1-50)
#
p1 = FreeCAD.Vector(col3+WOODWIDTH,0,0)
p2 = FreeCAD.Vector(col3+WOODWIDTH+500,0,0)
p3 = FreeCAD.Vector(0,-DIMLEVEL2,0)
DrawDim(p1,p2,p3,"Col 3.1",extlines=DIMLEVEL2-50)
#
FreeCAD.DraftWorkingPlane.alignToPointAndAxis(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,-1,0), -400.0)
p1 = FreeCAD.Vector(totalwidth,0,0)
p2 = FreeCAD.Vector(totalwidth,DEPTH,0)
p3 = FreeCAD.Vector(totalwidth+DIMLEVEL2,0,0)
DrawDim(p1,p2,p3,"Total depth", extlines=DIMLEVEL2-50)
#
FreeCAD.DraftWorkingPlane.alignToPointAndAxis(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,-1,0), -400.0)
p1 = FreeCAD.Vector(totalwidth,DEPTH,0)
p2 = FreeCAD.Vector(totalwidth,DEPTH,totalhight)
p3 = FreeCAD.Vector(totalwidth+DIMLEVEL2,DEPTH,0)
DrawDim(p1,p2,p3,"Total width", extlines=DIMLEVEL2-50)

# Vertical plane
FreeCAD.DraftWorkingPlane.alignToPointAndAxis(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,0,1), 0.0)
p1 = FreeCAD.Vector(0,0,totalhight)
p2 = FreeCAD.Vector(totalwidth,0,totalhight)
p3 = FreeCAD.Vector(0,DEPTH+DIMLEVEL2,totalhight)
DrawDim(p1,p2,p3,"Total hight",extlines=DIMLEVEL2-50)
#
p1 = FreeCAD.Vector(0,0,WOODWIDTH)
p2 = FreeCAD.Vector(0,0,WOODWIDTH+ROWHIGHT)
p3 = FreeCAD.Vector(-DIMLEVEL2,0,0)
DrawDim(p1,p2,p3,"Raw hight",extlines=DIMLEVEL2-50)

# Show inventory
show_inventory()

FreeCAD.ActiveDocument.recompute()

# Save picture
FreeCADGui.activeDocument().activeView().viewAxonometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
FreeCADGui.activeDocument().activeView().saveImage('sample.png',4096,3072,'Current')
