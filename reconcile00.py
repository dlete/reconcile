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
#        print(serials_supported)
#        print(what_type)

except IOError:
    print('The data file is missing')

# -----------------------------------------------------------------

try:
    os.chdir('/home/dlete/workspace/temp_store')
    """ get the "ignore" fix from https://github.com/jerryd/gtk-fortran/issues/67 """
    # try with ignore?
    live = open('output_tab_02.csv')

    serials_live = []

    for each_line in live:
        try:
            (hostname, status, entPhysicalSerialNum, entPhysicalDescr, entPhysicalModelName) = each_line.split("\t", 4)
#            print(hostname, end='')
#            catalog_number = unicode(catalog_number, errors=ignore)
#            print(catalog_number, end='')
#            print(entPhysicalSerialNum)
            serials_live.append(entPhysicalSerialNum)
        except:
            pass

    live.close()
#    print(serials_live)

except IOError:
    print('The data file is missing')

# ---------------------------------------------------------------------

"""
l1 = [1, 2, 3, 4, 5]
l2 = [9, 8, 7, 6, 5]

only_in_l1 = set(l1).difference(l2)
only_in_l2 = set(l2).difference(l1)
"""

only_in_support = set(serials_supported).difference(serials_live)
only_live = set(serials_live).difference(serials_supported)

# http://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
print("These are in Support but not Live:")
for i in only_in_support:
    print(i)

print("These are Live but Not Supported")
for i in only_live:
    print(i)

"""
print("These are in l2 but not in l1:")
for i in only_in_l2:
    print(i)
"""
