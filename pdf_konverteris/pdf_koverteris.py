import aspose.words as aw

fileNames = [ "Input1.png", "Input2.png" ]

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

for fileName in fileNames:
    builder.insert_image(fileName)
    # Insert a paragraph break to avoid overlapping images.
    builder.writeln()

doc.save("Output.pdf")
