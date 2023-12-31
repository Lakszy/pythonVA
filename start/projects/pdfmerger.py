from pypdf import PdfMerger

pdfs = ["file4.pdf","file3.pdf","file1.pdf","file2.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()