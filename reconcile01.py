import os
import xlrd #http://www.python-excel.org/

try:
    os.chdir('/home/dlete/reconcile_support')

    book = xlrd.open_workbook("csco_support.xlsx")
    sheet = book.sheet_by_name("state_supported_mar2013-feb2014")

#    print(sheet.nrows)

#    print(sheet.col(0))
# https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966#sheet.Cell-class

    for i in sheet.col(12):
        serial = str(i.value)
        serial = serial.strip()
        what_type = i.ctype
        print(serial)
        print(what_type)

except IOError:
    print('The data file is missing')
