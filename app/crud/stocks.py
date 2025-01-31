import pdfplumber


def anaylzePDFTest():
  with pdfplumber.open("sample.pdf") as pdf:
    for page in pdf.pages:
      print(page.extract_text())  # Extracts text from each page

  return 'hello'
    # return new_user