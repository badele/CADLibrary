## Example


**Code**

```python
cutleryA = generate_separator(width=280, depth=420, woodwidth=10, cutlerydepth=160, nblongcols=1, nbshortcols=3, name='cutleryA')
cutleryB = generate_separator(width=280, depth=420, woodwidth=10, cutlerydepth=260, nblongcols=1, nbshortcols=3, name='cutleryB')
cutleryC = generate_separator(width=280, depth=360, woodwidth=10, cutlerydepth=260, nblongcols=2, nbshortcols=2, name='cutleryC')
```

**Materials shopping list result**

```text
cutleryA
========

    2 * 160mm x 10mm x 70mm
    2 * 260mm x 10mm x 70mm
    1 * 400mm x 10mm x 70mm
    3 * 192.5mm x 10mm x 70mm
    2 * 420mm x 10mm x 70mm
    -------------------------
    TOTAL: 1432.5mm x 10mm x 70mm
```

**Image result**

<img border="0" width="50%" height src="https://raw.githubusercontent.com/badele/CADLibrary/master/freecad/cutlery_tray/sample.png"/>
