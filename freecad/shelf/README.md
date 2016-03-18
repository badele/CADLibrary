## Example

**Code**

```python
shelfA = generate_self(nbcols=2, nbrows=9, colwidth=250, name='meuble_gauche')
shelfB = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 6, 7], name='meuble_central')
shelfC = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 7], name='meuble_droit')
```

**Materials shopping list result**


```text
meuble_gauche
=============

    16 * 250mm x 250mm x 20mm
    3 * 20mm x 20mm x 2880mm
    2 * 560mm x 560mm x 20mm
    -------------------------
```

**Image result**

<img border="0" width="50%" src="https://raw.githubusercontent.com/badele/CADLibrary/master/freecad/shelf/sample.png"/>
