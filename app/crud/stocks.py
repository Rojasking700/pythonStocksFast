import pdfplumber


def anaylzePDFTest():
  print('this is runingnngngngn')
  with pdfplumber.open("assets/testPDFs/MarketEdgeMETA.pdf") as pdf:
    
    pageTextResults = []
    extractedTables = []
    
    for page in pdf.pages:
      extractedText =  page.extract_text()
      cleanedText = extractedText.replace("\x00", " ")
      pageTextResults.append(cleanedText)
      
      # for table in page.extract_tables():
      #   print(table)
      #   extractedTables.append(table)

      # print(page.extract_tables())  # Extracts extract_tables from each page
      


  return {
    'extractedText': pageTextResults,
    # 'extractedTables': extractedTables
    }