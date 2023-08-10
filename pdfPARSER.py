from pdfminer.high_level import extract_text, extract_pages
import os

cwd = os.getcwd()

print("-"*50)

print(f" The current working directory: {cwd}")

print("-"*50)

PDFdirectory = 'pdf'

joinDir = os.path.join(cwd, PDFdirectory)

print(f'The path to get the pdf files : {joinDir} ')

print("-"*50)

listDirFiles = os.listdir(joinDir) 

print(f" Files and directories inside pdf directory : {listDirFiles}" )

print("- -"*20)

print(f' Number of files inside the pdf directory: {len(listDirFiles)}')

print("-"*50)

# To get the first pdf file :

print(f' The first pdf file: {listDirFiles[0]}') 

print("-"*50)

# To extract data from the first pdf file : 

file = os.path.join(joinDir, listDirFiles[0])

print(f' Full file path of the required pdf file : {file}')

print("- -"*20)

text = extract_text(f"{file}")
print(f" Text from {listDirFiles[0]} : \n \n {text}")

