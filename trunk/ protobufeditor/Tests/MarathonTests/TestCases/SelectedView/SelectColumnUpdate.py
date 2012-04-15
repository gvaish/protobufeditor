useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoStoreSales3.bin')
		click('Edit1')
#		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
#		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,2')
		select_menu('Expand Tree')
#		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		select('JTreeTable', 'cell:keycode,5(61664713)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select('JTreeTable', 'rows:[5,6,7],columns:[Tree]')
		select_menu('View>>Column View #{Selected Records#}')
##		select('JTreeTable', 'rows:[5,6,7],columns:[Tree]')
		select('Table', 'cell:Row 2,1(40118)')
		assert_p('Table', 'Content', '[[61664713, 61664713, 61684613], [40118, 40118, 40118], [1, -1, 1], [17990, -17990, 12990]]')
		select('Table', '-11', 'Row 2,2')
		select('Table', '-117990', 'Row 2,3')
		select('Table', 'cell:Row 2,2(-11)')
		assert_p('Table', 'Content', '[[61664713, 61664713, 61684613], [40118, 40118, 40118], [1, -11, 1], [17990, -117990, 12990]]')
		select('Table', 'cell:Row 2,2(-11)')
		select_menu('Edit>>Compare with Disk')
##		select('Table1', 'cell:Row 2,2(-11)')
		select('Table', 'cell:saleDate,0(40118)')
		assert_p('Table', 'Content', '[[, Old, 36, 61664713, 40118, -1, -17990], [, New, 36, , , -11, -117990]]')
		select('Table', 'cell:saleDate,0(40118)')
		assert_p('TextPane', 'Text', '')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:Row 2,2(-11)')
		select('Table', 'cell:Row 2,2(-11)')
		select_menu('Window>>protoStoreSales3.bin>>Tree View')
##		select('Table', 'cell:Row 2,2(-11)')
		select('JTreeTable', 'cell:saleDate,5(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -11, -117990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select('JTreeTable', '-1', 'quantity,6')
		select('JTreeTable', '-17990', 'price,6')
		select('JTreeTable', 'cell:keycode,5(61664713)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select_menu('Window>>protoStoreSales3.bin>>Column Table')
		select('Table', 'cell:Row 2,2(-1)')
		select('Table', 'cell:Row 2,1(40118)')
		assert_p('Table', 'Content', '[[61664713, 61664713, 61684613], [40118, 40118, 40118], [1, -1, 1], [17990, -17990, 12990]]')
		select('Table', 'cell:Row 2,1(40118)')
		select_menu('Edit>>Compare with Disk')
		select('Table1', 'cell:Row 2,1(40118)')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
##		select('Table', 'cell:Row 2,1(40118)')

#		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoStoreSales3.bin'):
#			click('No')
#		close()
	close()
