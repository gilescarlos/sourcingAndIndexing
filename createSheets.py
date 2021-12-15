from glob import glob
from openpyxl import load_workbook
import Resources
# from tika import parser

folder = input("What list to index: ") + "\\"                                           # Folder with found journals
filePaths = glob(folder + "*.pdf")                                                      # List of file names in the folder
fileNames = []                                                                          # Empty list of file names

for i in range(len(filePaths)):
    fileNames.append(filePaths[i].replace(folder, ""))                        # For every file path, get the file name and add it to the list of file names

titlesAuthorsJournals = Resources.getTitlesWithAuthors()                                # Get list of lists containing a title, an author, and a journal 

indexer = input("Who indexed: ")                                                        # Ask who is indexing
for i in range(len(fileNames)):
    authorLastName = fileNames[i].split("-2021", 1)[0]                                  # Get the author's last name

    title = ""
    journal = ""
    for j in range(len(titlesAuthorsJournals)):                                         # For every title/author/journal combination          
        if (Resources.checkForAuthor(titlesAuthorsJournals[j][0], authorLastName)):     # See if the current author last name is found in the title/author/journal combo
            title += titlesAuthorsJournals[j][1]                                        # Get the title
            journal += titlesAuthorsJournals[j][2]                                      # Get the journal

    xlFileName = fileNames[i].split(".", 1)[0] + ".xlsx"                                # Create the name for the Excel file

    publisher = fileNames[i].split("(", 1)[1]                           
    publisher = publisher.split(")", 1)[0]                                              # Get the publisher from the journal's file name

    workbook = load_workbook(filename = "resources\Indexing Sheet 03122021.xlsx")       # Opening the indexing spreadsheet
    sheet = workbook.active                                                             # Main spreadsheet to input data

    sheet["C2"] = indexer                                                               # Write information from above into corresponding cells
    sheet["C3"] = title
    sheet["C4"] = authorLastName
    sheet["C5"] = journal
    sheet["C6"] = publisher

    workbook.save(filename = folder + xlFileName)                                       # Save the spreadsheet in folder with found journals

"""
brainKits = Resources.getKits()
routes = Resources.getRoutes()
agents = Resources.getAgents()
vehicles = Resources.getVehicles
pumps = Resources.getPumps()


filePaths = []

for i in range(len(fileNames)):
    filePaths.append(folder + fileNames[i])

text = parser.from_file(filePaths[0])

linesInPDF = text['content'].splitlines()
while '' in linesInPDF: 
    linesInPDF.remove('')    

wordsInPDF = [word for line in linesInPDF for word in line.split()]
for i in range(len(wordsInPDF)):
    if "(" in wordsInPDF[i]:
        wordsInPDF[i] = wordsInPDF[i].replace("(", "")
    elif ")" in wordsInPDF[i]:
        wordsInPDF[i] = wordsInPDF[i].replace(")", "") 
"""