#! python
# -*- coding: utf-8 -*-

import Part, math
import FreeCAD, FreeCADGui

# Create document
if FreeCAD.ActiveDocument and FreeCAD.ActiveDocument.Name == "cutlery_tray":
    FreeCAD.closeDocument("cutlery_tray")
FreeCAD.newDocument('cutlery_tray')

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


# Create box
def makebox(width=0, depth=0, height=70, pos=FreeCAD.Vector(), name="", id=""):
    doc = FreeCAD.ActiveDocument

    # Create Box
    etagere = doc.addObject("Part::Feature", '%(name)s_horizontal%(id)s' % locals())
    etagere.Shape = Part.makeBox(width, depth, height, pos)

    # Add to inventory
    mini = min(width,depth)
    maxi = max(width,depth)
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

        total = 0
        sizeresult = 0
        for element in INVENTORY[objname].keys():
            width, depth, height = element
            total += width * INVENTORY[objname][element]
            result = "    %s * %smm x %smm x %smm" % (INVENTORY[objname][element], width, depth, height)
            sizeresult = max(sizeresult, len(result)-4)
            print result
        print "    "+"-"*sizeresult
        print "    TOTAL: %smm x %smm x %smm" %  (total, depth, height)
        print ""
        print ""


# Create customized shelf
def generate_separator(width=280, depth=420, height=70, woodwidth=10, cutlerydepth=260, nblongcols=1, nbshortcols=3,
                       nbrows=2, name='separator'):
    doc = FreeCAD.ActiveDocument

    # Compute cols dimension
    rowsdepth = depth - cutlerydepth - 3 * woodwidth

    nbcols = nblongcols + nbshortcols
    freewidth = width - 2 * woodwidth - ((nbcols - 1) * woodwidth)
    colspace = freewidth / float(nbcols)
    collongdepth = depth - 2 * woodwidth
    colshortdepth = depth - 2 * woodwidth - rowsdepth - woodwidth

    # Left and right
    makebox(woodwidth, depth, height, name=name)
    makebox(woodwidth, depth, height, FreeCAD.Vector(width - woodwidth, 0, 0), name=name)

    # Top and bottom
    makebox(width - 2 * woodwidth, woodwidth, height, FreeCAD.Vector(woodwidth, 0, 0), name=name)
    makebox(width - 2 * woodwidth, woodwidth, height, FreeCAD.Vector(woodwidth, depth - woodwidth, 0), name=name)

    # Cols
    for x in range(1, nbcols):
        posx = woodwidth + (x * colspace) + ((x - 1) * woodwidth)
        if x <= nblongcols:
            makebox(woodwidth, collongdepth, height, pos=FreeCAD.Vector(posx, woodwidth, 0), name=name)
        else:
            makebox(woodwidth, colshortdepth, height, pos=FreeCAD.Vector(posx, woodwidth, 0), name=name)

    # Compute cols dimension
    leftshortposx = woodwidth + (nblongcols * colspace) + ((nblongcols - 1) * woodwidth) + woodwidth
    rowposy = colshortdepth + woodwidth
    shortwidth = width - leftshortposx - woodwidth
    freedepth = rowsdepth - ((nbrows - 1) * woodwidth)
    rowspace = freedepth / float(nbrows)

    # Rows
    if nbrows>0:
        makebox(shortwidth, woodwidth, height, FreeCAD.Vector(leftshortposx, rowposy, 0), name=name)
        for y in range(1, nbrows):
            posy = rowposy + woodwidth + (y * rowspace) + ((y - 1) * woodwidth)
            makebox(shortwidth, woodwidth, height, FreeCAD.Vector(leftshortposx, posy, 0), name=name)

    # Compound object
    objs = getGroupObjects(name)
    compoundObjects(name, objs)

    return doc.getObject(name)


# Init doc
doc = FreeCAD.ActiveDocument

cutleryA = generate_separator(width=280, depth=420, woodwidth=10, cutlerydepth=160, nblongcols=1, nbshortcols=3,
                              nbrows=3, name='cutleryA')
cutleryA.ViewObject.ShapeColor = (0.80, 0.80, 0.40)

cutleryB = generate_separator(width=280, depth=420, woodwidth=10, cutlerydepth=260, nblongcols=1, nbshortcols=3,
                              nbrows=2, name='cutleryB')
cutleryB.Placement.Base = FreeCAD.Vector(300, 0, 0)
cutleryB.ViewObject.ShapeColor = (0.27, 0.80, 0.80)

cutleryC = generate_separator(width=280, depth=360, woodwidth=10, cutlerydepth=260, nblongcols=2, nbshortcols=2,
                              nbrows=1, name='cutleryC')
cutleryC.Placement.Base = FreeCAD.Vector(600, 0, 0)
cutleryC.ViewObject.ShapeColor = (0.80, 0.53, 0.80)

# Show inventory
show_inventory()

FreeCAD.ActiveDocument.recompute()
