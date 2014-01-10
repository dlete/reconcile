import os
import xlrd #http://www.python-excel.org/

try:
    os.chdir('/home/dlete/reconcile_support')

    book = xlrd.open_workbook("csco_support.xlsx")
    sheet = book.sheet_by_name("state_supported_mar2013-feb2014")

#    print(sheet.nrows)

#    print(sheet.col(0))
# https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966#sheet.Cell-class
    serials_supported = []

    for i in sheet.col(12):
        if i.ctype == 0:
            serial = "EMPTY!!!"
        elif i.ctype == 1:
            serial = i.value.strip()
        elif i.ctype == 2 or i.cytpe == 3:
            serial = i.value
            if serial < 0 :
                serial = serial * (-1)
#                serial = str(serial)
            serial = int(serial)
            serial = str(serial)

            serials_supported.append(serial)
#        serial = i.value
            
#        serial = str(i.value)
#        serial = serial.strip()
        what_type = i.ctype
#        print(serial)
        print(serials_supported)
#        print(what_type)

except IOError:
    print('The data file is missing')
