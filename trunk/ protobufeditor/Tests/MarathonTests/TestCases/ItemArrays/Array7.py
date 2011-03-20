useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() +  'protoStoreSales7.bin')
		click('Edit1')
		##select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')
		select('JTreeTable', 'rows:[8,9],columns:[keycode]')
		select_menu('View>>Column View #{Selected Records#}')
		##select('JTreeTable', 'rows:[8,9],columns:[keycode]')
		assert_p('Table', 'Content', '[[69684558, 69694158], [[40118, 40118, 40118], [40118, 40118, 40118]], [[1, -1, 1], [1, -1, 1]], [[19000, -19000, 5010], [19000, -19000, 5010]], [[SALE, RETURN, SALE], [SALE, RETURN, SALE]], [[19.0, -19.0, 5.01], [19.0, -19.0, 5.01]], [[19.0, -19.0, 5.01], [19.0, -19.0, 5.01]], [[\'\',\' -1\',\' -1 1\'], [\'\',\' -1\',\' -1 1\']]]')
		select('Table', 'cell:Row 2,6([19.0, -19.0, 5.01])')
		select('Table', 'cell:Row 2,6([19.0, -19.0, 5.01])')
		click('ArrowButton')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0], [2, 5.01]]')
		select('Table', 'cell:Data,2(5.01)')
		select('Table', '5.0107896', 'Data,2')
		select('Table', 'cell:Data,0(19.0)')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0], [2, 5.0107896]]')
		select('Table', 'cell:Data,2(5.0107896)')
		click('Add Row Before')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0], [2, 0.0], [3, 5.0107896]]')
		select('Table', '0.04567', 'Data,2')
		select('Table', 'cell:Data,1(-19.0)')
		assert_p('Table', 'Content', '[[0, 19.0], [1, -19.0], [2, 0.04567], [3, 5.0107896]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales7.bin>>Column Table')
		assert_p('Table', 'Content', '[[69684558, 69694158], [[40118, 40118, 40118], [40118, 40118, 40118]], [[1, -1, 1], [1, -1, 1]], [[19000, -19000, 5010], [19000, -19000, 5010]], [[SALE, RETURN, SALE], [SALE, RETURN, SALE]], [[19.0, -19.0, 5.01], [19.0, -19.0, 5.01]], [[19.0, -19.0, 5.01], [19.0, -19.0, 0.04567, 5.0107896]], [[\'\',\' -1\',\' -1 1\'], [\'\',\' -1\',\' -1 1\']]]')
		click('BaseDisplay$HeaderToolTips', 'Row 2')
		assert_p('Table', 'Text', '')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('JTreeTable', 'rows:[8,9],columns:[keycode]')
		select('JTreeTable', 'rows:[8,9],columns:[keycode]')
		select_menu('Window>>protoStoreSales7.bin>>Tree View')
		select('JTreeTable', 'rows:[8,9],columns:[keycode]')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63604808, [40118], [1], [4870], [SALE], [4.87], [4.87], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 69684558, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 5.01], [\'\',\' -1\',\' -1 1\']], [, , 69694158, [40118, 40118, 40118], [1, -1, 1], [19000, -19000, 5010], [SALE, RETURN, SALE], [19.0, -19.0, 5.01], [19.0, -19.0, 0.04567, 5.0107896], [\'\',\' -1\',\' -1 1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 62684671, [40118, 40118], [1, -1], [69990, -69990], [SALE, RETURN], [69.99, -69.99], [69.99, -69.99], [\'\',\' -1\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 65674532, [40118], [1], [3590], [SALE], [3.59], [3.59], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , 63674861, [40118], [10], [2700], [SALE], [2.7], [2.7], [\'\']], [, , 64634429, [40118], [1], [3990], [SALE], [3.99], [3.99], [\'\']], [, , 66624458, [40118], [1], [890], [SALE], [0.89], [0.89], [\'\']], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ], [, , , , , , , , , ]]')

	close()
