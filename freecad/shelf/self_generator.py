#! python
# -*- coding: utf-8 -*-

import Part, math
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
    etagere.Shape = Part.makeBox(length, length, height, pos)

    # Add to inventory
    mini = min(length,length)
    maxi = max(length,length)
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


# Left Part
shelfA = generate_self(nbcols=2, nbrows=9, colwidth=250, name='meuble_gauche')
shelfA.ViewObject.ShapeColor = (0.80, 0.80, 0.40)

# Central part
shelfB = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 6, 7], name='meuble_central')
shelfB.Placement.Base = FreeCAD.Vector(560, 0, 0)
shelfB.ViewObject.ShapeColor = (0.27, 0.80, 0.80)

# Right part
shelfC = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 7], name='meuble_droit')
shelfC.Placement.Base = FreeCAD.Vector(1100, 0, 0)
shelfC.ViewObject.ShapeColor = (0.80, 0.53, 0.80)

# Show inventory
show_inventory()

FreeCAD.ActiveDocument.recompute()