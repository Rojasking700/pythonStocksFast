import pdfplumber
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

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
      


      client = Groq(api_key=os.getenv("GROQ_API_KEY"),)
      completion = client.chat.completions.create(
          model="llama-3.1-8b-instant",
          messages=[
            {
              "role": "system",
              "content": "you are a stock market analysist"
            },

            # Set a user message for the assistant to respond to.
            {
              "role": "user",
              "content": "summarize this for me:",
            }, 
            
            {
              "role": "user",
              "content": pageTextResults[0],
            }
            #  "summarize This:",
            #  pageTextResults[0]
          ],
          temperature=1,
          max_completion_tokens=1024,
          top_p=1,
          stream=True,
          stop=None,
      )

      for chunk in completion:
          print(chunk.choices[0].delta.content or "", end="")



  return {
    'extractedText': pageTextResults,
    'completion': completion
    # 'extractedTables': extractedTables
    }