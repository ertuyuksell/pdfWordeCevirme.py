from pdf2docx import Converter

pdfPath="H1-Ders Notları.pdf"#Dönüştürmek istediğiniz pdf i yazın.
docxPath="H1-Ders Notlar.docx"#.docx şeklinde istediğiniz ismi vererek yazın.

cv=Converter(pdf_file=pdfPath)
cv.convert(docx_file=docxPath)
cv.close()
