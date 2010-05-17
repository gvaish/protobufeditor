useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window('Protocol Buffer Editor'):
		select('FileChooser',  commonBits.sampleDir() + 'protoFieldTest.bin')
		click('Edit1')
		select('Table', 'cell:2|f02,0(0)')
		rightclick('Table', '7|f07,3')
##		select('Table', 'cell:2|f02,0(0)')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|f02,0(0)')
		assert_p('Table', 'Content', '[[f01, 1, , 30000, 30000], [f02, 2, , 30000, 30000], [f03, 3, , 30000, 30000], [f04, 4, , 30000, 30000], [f05, 5, , 30000, 30000], [f06, 6, , 300000000, 300000000], [f07, 7, , 300000000, 300000000], [f08, 8, , 300000000, 300000000], [f09, 9, , 300000000, 300000000], [f10, 10, , 300000000, 300000000], [f11, 11, , 30000.0, 30000.0], [f12, 12, , 3.0E8, 3.0E8], [f13, 13, , true, true], [f14, 14, , false, false], [f15, 15, , 300000000, 300000000], [f16, 16, , 300000000 optional, 300000000 optional], [f17, 17, , RETURN, RETURN], [f18, 18, , RETURN, RETURN], [f19, 19, , 0000000003, 0000000003], [f20, 20, , 0000000003, 0000000003]]')
		select('Table', '300001', 'Data,0')
		select('Table', '2', 'Data,1')
		select('Table', '300003', 'Data,2')
		select('Table', '300004', 'Data,3')
		select('Table', '300005', 'Data,4')
		select('Table', '3000000006', 'Data,5')
		select('Table', '3000000007', 'Data,6')
		select('Table', '3000000008', 'Data,7')
		select('Table', '3000000009', 'Data,8')
		select('Table', '30000000010', 'Data,9')
		select('Table', '300010.0', 'Data,10')
		select('Table', '31.0E8', 'Data,11')
##		select('Table', 'cell:Data,11(3.0E8)')
##		rightclick('Table', 'Data,12')
##		select('Table', 'cell:Data,11(3.0E8)')
		select('Table', 'false', 'Data,12')
		select('Table', 'true', 'Data,13')
		select('Table', '30000000012', 'Data,14')
		select('Table', '30000000013 optional', 'Data,15')
		select('Table', 'OTHER', 'Data,16')
		select('Table', '', 'Data,17')
		select('Table', '000000000312', 'Data,18')
		select('Table', '000000000356', 'Data,19')
		select('Table', 'cell:Data,18(000000000312)')
		assert_p('Table', 'Content', '[[f01, 1, , 300001, 300001], [f02, 2, , 2, 2], [f03, 3, , 300003, 300003], [f04, 4, , 300004, 300004], [f05, 5, , 300005, 300005], [f06, 6, , 3000000006, 3000000006], [f07, 7, , 3000000007, 3000000007], [f08, 8, , 3000000008, 3000000008], [f09, 9, , 3000000009, 3000000009], [f10, 10, , 30000000010, 30000000010], [f11, 11, , 300010.0, 300010.0], [f12, 12, , 3.1E9, 3.1E9], [f13, 13, , false, false], [f14, 14, , true, true], [f15, 15, , 30000000012, 30000000012], [f16, 16, , 30000000013 optional, 30000000013 optional], [f17, 17, , OTHER, OTHER], [f18, 18, , , ], [f19, 19, , 000000000312, 000000000312], [f20, 20, , 000000000356, 000000000356]]')
		select('Table', 'cell:Data,18(000000000312)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:2|f02,0(0)')
		select('Table', 'cell:2|f02,0(0)')

	close()