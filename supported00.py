import os

try:
    os.chdir('/home/dlete/reconcile_support')
    """ get the "ignore" fix from https://github.com/jerryd/gtk-fortran/issues/67 """
    # try with ignore?
    supported = open('csco_support_brief.csv', errors='replace')

    for each_line in supported:
        try:
            (hostname, catalog_number, description, serial_number, quantity) = each_line.split(",", 4)
#            print(hostname, end='')
#            catalog_number = unicode(catalog_number, errors=ignore)
#            print(catalog_number, end='')
            print(serial_number)
        except:
            pass

    supported.close()

except IOError:
    print('The data file is missing')
