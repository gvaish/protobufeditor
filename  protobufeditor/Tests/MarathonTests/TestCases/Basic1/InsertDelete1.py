useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoStoreSales3b.bin')
		click('Edit1')
		select('JTreeTable', 'cell:Tree,3(null)')
		click('New')

		if window('Record Selection'):
			assert_p('OptionPane.comboBox', 'Content', '[[department, order, Store]]')
			select('OptionPane.comboBox', 'Store')
			click('OK')
		close()

		select('Table', '1234', 'Data,0')
		select('Table', 'cell:Data,0(1234)')
		assert_p('Table', 'Content', '[[store, 1, , 1234, 1234], [name, 2, , , ]]')
		select('Table', 'n 1234', 'Data,1')
		select('Table', 'cell:Data,0(1234)')
		click('New')

		if window('Record Selection'):
			click('OK')
		close()

		select('Table', '456', 'Data,0')
		select('Table', 'n 456', 'Data,1')
		select('Table', 'cell:Data,0(456)')
		click('New')

		if window('Record Selection'):
			click('OK')
		close()

		select('Table', '123', 'Data,0')
		select('Table', '11', 'Data,1')
		select('Table', '11', 'Data,2')
		select('Table', '222', 'Data,3')
		select('Table', '22233', 'Data,3')
		select('Table', 'cell:Data,2(11)')
		select_menu('File>>Compare with Disk')
#		select('Table1', 'cell:Data,2(11)')
		select('Table', 'cell:' + commonBits.secondField() + ',3(n 456)')
		assert_p('Table', 'Content', '[[, , , , , , ], [, Inserted, 856, 1234, n 1234, , ], [, , , , , , ], [, Inserted, 857, 456, n 456, , ], [, , , , , , ], [, Inserted, 858, 123, 11, 11, 22233]]')
		select('Table', 'cell:' + commonBits.secondField() + ',3(n 456)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:Data,2(11)')
		select('Table', 'cell:Data,2(11)')
		select_menu('Window>>protoStoreSales3b.bin>>Tree View')
		select('Table', 'cell:Data,2(11)')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'Tree,4')
		select_menu('Fully Expand Tree')
		select('JTreeTable', 'cell:Tree,3(null)')
		assert_p('JTreeTable', 'Content', '[[, , 20, Store: 20], [, , 59, Store: 59], [, , 166, Store: 166], [, , 184, Store: 184], [, , 1234, n 1234], [, , , ], [, , , ], [, , , ], [, , , ]]')
		select('JTreeTable', 'cell:Tree,3(null)')
		select('LayoutCombo', 'Deptartment')
		select('JTreeTable', 'cell:name,5(null)')
		assert_p('JTreeTable', 'Content', '[[, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , 456, n 456], [, , , ], [, , , ]]')
		select('JTreeTable', 'cell:name,5(null)')
		select('LayoutCombo', 'Product')
		select('JTreeTable', 'cell:price,8(22233)')
		select('JTreeTable', 'cell:quantity,8(11)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 123, 11, 11, 22233]]')
		click('Save1')
		click('Close')
		click('Edit1')
		select('JTreeTable', 'cell:store,4(1234)')
		assert_p('JTreeTable', 'Content', '[[, , 20, Store: 20], [, , 59, Store: 59], [, , 166, Store: 166], [, , 184, Store: 184], [, , 1234, n 1234]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,4')
		select_menu('Fully Expand Tree')
		select('JTreeTable', 'cell:Tree,4(null)')
		assert_p('JTreeTable', 'Content', '[[, , 20, Store: 20], [, , 59, Store: 59], [, , 166, Store: 166], [, , 184, Store: 184], [, , 1234, n 1234], [, , , ], [, , , ], [, , , ], [, , , ]]')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'Tree,4')
		select_menu('Edit Record')
		select('JTreeTable', 'cell:Tree,4(null)')
		select('Table', 'cell:Data,0(1234)')
		select('Table', 'cell:Data,0(1234)')
		assert_p('Table', 'Content', '[[store, 1, , 1234, 1234], [name, 2, , n 1234, n 1234]]')
		click('Down')
		select('Table', 'cell:Data,0(456)')
		assert_p('Table', 'Content', '[[department, 1, , 456, 456], [name, 2, , n 456, n 456]]')
		click('Down')
		select('Table', 'cell:Data,1(11)')
		assert_p('Table', 'Content', '[[keycode, 1, , 123, 123], [saleDate, 2, , 11, 11], [quantity, 3, , 11, 11], [price, 4, , 22233, 22233]]')
		select_menu('Window>>protoStoreSales3b.bin>>Tree View')
		select('JTreeTable', 'cell:Tree,4(null)')
		rightclick('JTreeTable', 'Tree,4')
		select_menu('Delete Record#{s#}')
		select_menu('File>>Compare with Disk')
		select('Table', 'cell:' + commonBits.firstField() + ',2(456)')
		assert_p('Table', 'Content', '[[, Deleted, 856, 1234, n 1234, , ], [, , , , , , ], [, Deleted, 857, 456, n 456, , ], [, , , , , , ], [, Deleted, 858, 123, 11, 11, 22233], [, , , , , , ]]')
		assert_p('Table', 'Content', '[[, Deleted, 856, 1234, n 1234, , ], [, , , , , , ], [, Deleted, 857, 456, n 456, , ], [, , , , , , ], [, Deleted, 858, 123, 11, 11, 22233], [, , , , , , ]]')
		select('Table', 'cell:' + commonBits.firstField() + ',2(456)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales3b.bin>>Tree View')
		click('Save1')
	close()
