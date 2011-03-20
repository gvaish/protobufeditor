useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoStoreSales3.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,2')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		select('JTreeTable', 'cell:saleDate,5(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select('JTreeTable', 'rows:[5,6,7],columns:[saleDate]')
		select_menu('View>>Record View #{Selected Records#}')
##		select('JTreeTable', 'rows:[5,6,7],columns:[saleDate]')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 61664713, 61664713], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 17990, 17990]]')
		click('Right')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 61664713, 61664713], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -17990, -17990]]')
		select('Table', '-11', 'Data,2')
		select('Table', '-1117990', 'Data,3')
		select('Table', 'cell:Data,2(-11)')
		assert_p('Table', 'Content', '[[keycode, 1, , 61664713, 61664713], [saleDate, 2, , 40118, 40118], [quantity, 3, , -11, -11], [price, 4, , -1117990, -1117990]]')
		select_menu('Window>>protoStoreSales3.bin>>Tree View')
		select('JTreeTable', 'cell:saleDate,5(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -11, -1117990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select_menu('File>>Compare with Disk')
		select('Table', 'cell:saleDate,0(40118)')
		assert_p('Table', 'Content', '[[, Old, 36, 61664713, 40118, -1, -17990], [, New, 36, , , -11, -1117990]]')
		select('Table', 'cell:saleDate,0(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales3.bin>>Tree View')
		select('JTreeTable', '-1', 'quantity,6')
		select('JTreeTable', '-17990', 'price,6')
##		select('JTreeTable', '')
		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('Table', 'cell:Data,1(40118)')
		assert_p('Table', 'Content', '[[keycode, 1, , 61664713, 61664713], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -17990, -17990]]')
		select_menu('File>>Compare with Disk')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')

#		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoStoreSales3b.bin'):
#			click('No')
#		close()
	close()
