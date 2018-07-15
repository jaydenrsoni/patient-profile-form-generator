import PyPDF2 as pdf2


def read_patient_info_from_pdf(path="input.pdf"):
    input = pdf2.PdfFileReader(file(path, "rb"))


def write_patient_info_to_pdf():
    output = pdf2.PdfFileWriter()
    outputStream = file("output.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
