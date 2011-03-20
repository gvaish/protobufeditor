useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() +  'protoStoreSales3SDim.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 69684558, 40118, 1, 19000], [, , 69684558, 40118, -1, -19000], [, , 69684558, 40118, 1, 5010], [, , 69694158, 40118, 1, 19000], [, , 69694158, 40118, -1, -19000], [, , 69694158, 40118, 1, 5010], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'saleDate,6')
		select_menu('Hide Column')
		assert_p('JTreeTable', 'Content', '[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , 69684558, 1, 19000], [, , 69684558, -1, -19000], [, , 69684558, 1, 5010], [, , 69694158, 1, 19000], [, , 69694158, -1, -19000], [, , 69694158, 1, 5010], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'quantity,6')
		select_menu('Hide Column')
		assert_p('JTreeTable', 'Content', '[[, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , 69684558, 19000], [, , 69684558, -19000], [, , 69684558, 5010], [, , 69694158, 19000], [, , 69694158, -19000], [, , 69694158, 5010], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'price,7')
		select_menu('Hide Column')
		assert_p('JTreeTable', 'Content', '[[, , ], [, , ], [, , ], [, , ], [, , ], [, , 69684558], [, , 69684558], [, , 69684558], [, , 69694158], [, , 69694158], [, , 69694158], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,6')
		select_menu('Show Column>>price')
		assert_p('JTreeTable', 'Content', '[[, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , 69684558, 19000], [, , 69684558, -19000], [, , 69684558, 5010], [, , 69694158, 19000], [, , 69694158, -19000], [, , 69694158, 5010], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,7')
		select_menu('Show Column>>quantity')
		assert_p('JTreeTable', 'Content', '[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , 69684558, 1, 19000], [, , 69684558, -1, -19000], [, , 69684558, 1, 5010], [, , 69694158, 1, 19000], [, , 69694158, -1, -19000], [, , 69694158, 1, 5010], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,7')
		select_menu('Show Column>>saleDate')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 69684558, 40118, 1, 19000], [, , 69684558, 40118, -1, -19000], [, , 69684558, 40118, 1, 5010], [, , 69694158, 40118, 1, 19000], [, , 69694158, 40118, -1, -19000], [, , 69694158, 40118, 1, 5010], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'saleDate,7')
		select_menu('Hide Column')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'quantity,7')
		select_menu('Hide Column')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'price,7')
		select_menu('Hide Column')
		assert_p('JTreeTable', 'Content', '[[, , ], [, , ], [, , ], [, , ], [, , ], [, , 69684558], [, , 69684558], [, , 69684558], [, , 69694158], [, , 69694158], [, , 69694158], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ], [, , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,6')
		select_menu('Show Column>>saleDate')
		assert_p('JTreeTable', 'Content', '[[, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , 69684558, 40118], [, , 69684558, 40118], [, , 69684558, 40118], [, , 69694158, 40118], [, , 69694158, 40118], [, , 69694158, 40118], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,7')
		select_menu('Show Column>>quantity')
		assert_p('JTreeTable', 'Content', '[[, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , 69684558, 40118, 1], [, , 69684558, 40118, -1], [, , 69684558, 40118, 1], [, , 69694158, 40118, 1], [, , 69694158, 40118, -1], [, , 69694158, 40118, 1], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ], [, , , , ]]')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'keycode,7')
		select_menu('Show Column>>price')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 69684558, 40118, 1, 19000], [, , 69684558, 40118, -1, -19000], [, , 69684558, 40118, 1, 5010], [, , 69694158, 40118, 1, 19000], [, , 69694158, 40118, -1, -19000], [, , 69694158, 40118, 1, 5010], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
	close()
