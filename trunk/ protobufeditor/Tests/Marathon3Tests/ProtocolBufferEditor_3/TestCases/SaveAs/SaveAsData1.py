#{{{ Marathon
from default import *
#}}} Marathon

from Modules import commonBits


def test():

    set_java_recorded_version("1.6.0_22")
    if frame(' - Open File:0'):
        select('File', commonBits.sampleDir() + 'DTAR020_tst1.bin')
        click('Edit')
    close()

    if window('Protocol Buffer Editor'):
##        click('SaveAs')

        select_menu('File>>Export')


        if frame('Export - DTAR020_tst1.bin:0'):
            select('Keep screen open', 'true')
            select('Edit Output File', 'true')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin$:0'):
            assert_content('JTable_22', [ ['63604808', '20', '40118', '170', '1', '4870'],
['69684558', '20', '40118', '280', '1', '19000'],
['69684558', '20', '40118', '280', '-1', '-19000'],
['69694158', '20', '40118', '280', '1', '5010'],
['62684671', '20', '40118', '685', '1', '69990'],
['62684671', '20', '40118', '685', '-1', '-69990'],
['61664713', '59', '40118', '335', '1', '17990'],
['61664713', '59', '40118', '335', '-1', '-17990'],
['61684613', '59', '40118', '335', '1', '12990'],
['68634752', '59', '40118', '410', '1', '8990'],
['60694698', '59', '40118', '620', '1', '3990'],
['60664659', '59', '40118', '620', '1', '3990'],
['60614487', '59', '40118', '878', '1', '5950'],
['68654655', '166', '40118', '60', '1', '5080'
],
['69624033', '166', '40118', '80', '1', '18190'],
['60604100', '166', '40118', '80', '1', '13300'],
['68674560', '166', '40118', '170', '1', '5990']
])
        close()



##        window_closed('Record Editor')
    close()

    pass
