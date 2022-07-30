# importing libraries
import pandas as pd

# argument 1 : Excel File name
# argument 2,3,... : Sheet names of that excel file
# returns : dataframe of combined data


def readExcelSheets(name, *sheetNames):
    allSheets = pd.DataFrame()
    for sheetItem in sheetNames:
        originalExcel = pd.read_excel(name, sheet_name=sheetItem)
        allSheets = pd.concat([allSheets, originalExcel])
    allSheets.to_excel('Recent Exel Report.xlsx')
    return allSheets


# For single excel file
# Parameter 1 : Excel File | Parameter 2,3,... : Sheet names of that excel file
readExcelSheets('Excel 1.xlsx', 'first-sheet', 'second-sheet')

# For multiple Excel Files
sheet1 = readExcelSheets('Excel 1.xlsx', 'first', 'second')
sheet2 = readExcelSheets('Excel 2.xlsx', 'Sheet1', 'Sheet2')
sheet3 = readExcelSheets('Excel 3.xlsx', 'Sheet1', 'Sheet2')
#sheet4 = readExcelSheets('Excel 4.xlsx', 'Sheet1', 'Sheet2')

# Appending multiple sheets into one final data frame
result = sheet1.append(sheet2)
result = sheet1.append(sheet3)
#result = sheet1.append(sheet4)

# Exporting final data frame
result.to_excel('Final Excel.xlsx')
