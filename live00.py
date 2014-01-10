import os

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
    print(serials_live)

except IOError:
    print('The data file is missing')
