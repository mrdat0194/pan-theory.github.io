from pdf2docx import Converter

pdf_file = 'Blog_ThichHocToan.pdf'
docx_file = 'Blog_ThichHocToan.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()