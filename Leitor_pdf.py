import PyPDF2

# carrega o arquivo pdf
pdfFileObj = open('C:\PROJETOS DEV\SQL\ebook-sql.pdf', 'rb')

# faz a leitura do arquivo PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# captura primeira pagina do pdf
pageObj = pdfReader.getPage(1)

# Extrai texto do PDF e passa para variavel
text = pageObj.extractText()

# mostra texto do PDF

print(text)
