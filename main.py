import shapefile

sf = shapefile.Reader("pyshp/shapefiles/A1_LANE")

print (sf.shapeType)

shapes = sf.shapes()

print (len(shapes))

s = sf.shape(7)
print (['%.3f' % coord for coord in s.bbox])

for name in dir(shapes[3]):
    if not name.startswith('_'):
        print (name)


fields = sf.fields
print (fields)

shapeRecs = sf.shapeRecords()

print (len(shapeRecs))

print (shapeRecs[0].record[1:3])
print (shapeRecs[0].shape.points[0:2])
