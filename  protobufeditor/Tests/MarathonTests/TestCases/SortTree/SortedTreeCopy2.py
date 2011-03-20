useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'protoSales.bin')
		click('Edit1')
		select_menu('View>>Sorted Field Tree')
		##select('List', 'sale')
		select('Table', 'store', 'Field,0')
		select('Table', 'department', 'Field,1')
		select('Table', 'cell:Field,1(department)')
		click('Build Tree')
		select('JTreeTable', 'cell:keycode,0(null)')
		rightclick('JTreeTable', 'keycode,0')
		select_menu('Copy Record#{s#}')
		select('JTreeTable', 'cell:keycode,2(null)')
		rightclick('JTreeTable', 'keycode,2')
		select_menu('Paste Record#{s#} Prior')
		select('JTreeTable', 'cell:keycode,2(null)')
		assert_p('JTreeTable', 'RowCount', '5')
		select('JTreeTable', 'cell:keycode,2(null)')
		rightclick('JTreeTable', 'keycode,2')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Tree,5(null)')
		assert_p('JTreeTable', 'RowCount', '10')
		select('JTreeTable', 'cell:Tree,3(null)')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:keycode,4(63604808)')
		assert_p('JTreeTable', 'Text', '63604808', 'keycode,4')
		select('JTreeTable', 'cell:store,4(20)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 170, 40118, 1, 4870], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:Tree,8(null)')
		rightclick('JTreeTable', 'Tree,8')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:keycode,10(66624458)')
		assert_p('JTreeTable', 'Text', '66624458', 'keycode,10')
		select('JTreeTable', 'cell:keycode,11(63674861)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 170, 40118, 1, 4870], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 64634429, 20, 957, 40118, 1, 3990], [, , 66624458, 20, 957, 40118, 1, 890], [, , 63674861, 20, 957, 40118, 10, 2700], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:Tree,6(null)')
		rightclick('JTreeTable', 'Tree,6')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:keycode,7(62684671)')
		assert_p('JTreeTable', 'Text', '62684671', 'keycode,7')
		select('JTreeTable', 'cell:keycode,8(62684671)')
		rightclick('JTreeTable', 'keycode,8')
		select('JTreeTable', 'cell:keycode,8(62684671)')
		assert_p('JTreeTable', 'RowCount', '16')
		select('JTreeTable', 'cell:saleDate,7(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , , , , , , ], [, , 63604808, 20, 170, 40118, 1, 4870], [, , , , , , , ], [, , , , , , , ], [, , 62684671, 20, 685, 40118, 1, 69990], [, , 62684671, 20, 685, 40118, -1, -69990], [, , , , , , , ], [, , , , , , , ], [, , 64634429, 20, 957, 40118, 1, 3990], [, , 66624458, 20, 957, 40118, 1, 890], [, , 63674861, 20, 957, 40118, 10, 2700], [, , , , , , , ], [, , , , , , , ]]')
		select('JTreeTable', 'cell:Tree,1(null)')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:Tree,6(null)')
		assert_p('JTreeTable', 'RowCount', '22')
		select('JTreeTable', 'rows:[7,8,9,10,11,12,13,14,15],columns:[Tree]')
		select_menu('View>>Table View #{Selected Records#}')
		select('JTreeTable', 'rows:[7,8,9,10,11,12,13,14,15],columns:[Tree]')
		select('Table', 'cell:1|keycode,4(63604808)')
		assert_p('Table', 'Content', '[[64614401, 59, 957, 40118, 1, 1990], [64614401, 59, 957, 40118, 1, 1990], [62684217, 59, 957, 40118, 1, 9990], [64624770, 59, 957, 40118, 1, 2590], [63604808, 20, 170, 40118, 1, 4870], [69684558, 20, 280, 40118, 1, 19000], [69684558, 20, 280, 40118, -1, -19000], [69684558, 20, 280, 40118, 1, 5010], [69694158, 20, 280, 40118, 1, 19000], [69694158, 20, 280, 40118, -1, -19000], [69694158, 20, 280, 40118, 1, 5010], [62684671, 20, 685, 40118, 1, 69990], [62684671, 20, 685, 40118, -1, -69990], [65674532, 20, 929, 40118, 1, 3590]]')
		select('Table', 'cell:1|keycode,7(69684558)')
		assert_p('Table', 'Text', '69684558', '1|keycode,7')
		select('Table', 'cell:1|keycode,1(64614401)')
		assert_p('Table', 'Text', '62684217', '1|keycode,2')
		select('Table', 'cell:1|keycode,1(64614401)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'protoSales.bin'):
			click('No')
		close()
	close()
