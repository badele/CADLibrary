## Example

```python
shelfA = generate_self(nbcols=2, nbrows=9, colwidth=250, name='meuble_gauche')
shelfB = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 6, 7], name='meuble_central')
shelfC = generate_self(nbcols=1, nbrows=9, colwidth=500, ignorerows=[5, 7], name='meuble_droit')
```

<img border="0" width="50%" src="https://raw.githubusercontent.com/badele/CADLibrary/master/freecad/shelf/sample.png"/>
