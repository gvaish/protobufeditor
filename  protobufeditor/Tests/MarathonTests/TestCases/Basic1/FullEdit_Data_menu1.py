useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228.bin')
		#commonBits.setRecordLayout(select, 'ams Store')
		click('Edit1')
		select_menu('Data>>Filter')
		select('Table', 'cell:Field,1(Loc_Nbr)')
		assert_p('Table', 'Content', '[[Brand_Id, true], [Loc_Nbr, true], [Loc_Type, true], [Loc_Name, true], [Loc_Addr_Ln1, true], [Loc_Addr_Ln2, true], [Loc_Addr_Ln3, true], [Loc_Postcode, true], [Loc_State, true], [Loc_Actv_Ind, true]]')
		#select('Table1', '')
#		select('Table', 'cell:Record,0(ams Store)')
#		assert_p('Table', 'Content', '[[Locations, true]]')
#		select('Table', 'cell:Record,0(ams Store)')
		select('Table1', 'Loc_Type', 'Field,0')
		select('Table1', 'dc', 'Value,0')
		select('Table1', 'cell:Value,0()')
		click('Filter1')
		select('Table', 'cell:4|Loc_Name,15(State Warehouse VIC)')
		assert_p('Table', 'Content', '[[TAR, 5839, DC, DC - Taras Ave, , 30-68 Taras Ave, Altona North, 3025, VIC, A], [TAR, 5850, DC, VIC West Ad Support, , Lot 2 Little Boundary Rd, Laverton, 3028, VIC, A], [TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5700, DC, Head Office, , , , , , A], [TAR, 5887, DC, QLD Ad Support, , , , , , A], [TAR, 5888, DC, SA Ad Support, , , , , , A], [TAR, 5109, DC, National Ad Support, , , , , , A], [TAR, 5895, DC, VIC East Ad Support, , , , , , A], [TAR, 5897, DC, Sydney Gate DC, No 2 Sydney Gate, 830 Bourke Street, Waterloo, 2017, NSW, A], [TAR, 5949, DC, Central Returns Centre, , 214-228 Blackshaws Rd, Altona North, , VIC, A], [TAR, 5951, DC, NSW West Sydney Ad Support, , , , , , A], [TAR, 5952, DC, TAS Ad Support, , , , , , A], [TAR, 5953, DC, North Geelong Warehouse, Target Head Office, 12 Thompson Road, North Geelong, 3215, VIC, A], [TAR, 5954, DC, State  Warehouse NSW, Target State Warehouse NSW (Westgate), Warehouse D Murtha Street, Arndell Park, 2148, NSW, A], [TAR, 5955, DC, State Warehouse VIC, Target State Warehouse VIC (Patricks), 180 Fitzgerald Road, Laverton, 3028, VIC, A], [TAR, 5957, DC, State Warehouse SA, Target State Warehouse  (Patricks), 180 Fitzgerald Road, Laverton, 3028, VIC, A], [TAR, 5958, DC, State Warehouse  WA, Target State Warehouse (WA) FCL, 56 Dowd Street, Welshpool, 6106, WA, A], [TAR, 5956, DC, State Warehouse QLD, Target State Warehouse QLD (RMS), 243 Bradman Street, Acacia Ridge, 4110, QLD, A], [TAR, 5959, DC, NSW  South Sydney Ad Support, South Sydney Ad Support, 753 Hume Highway, Bass Hill, , NSW, A], [TAR, 5960, DC, NSW East Sydney Ad Support,  Building B, Portside Distribution Ce, 2 - 8 Mc Pherson Street,, Botany, 2019, NSW, A], [TAR, 5963, DC, QLD South Ad Support, , , , , , A], [TAR, 5964, DC, QLD North Ad Support, , , , , , A], [TAR, 5965, DC, Canning Vale DC, Canning Vale DC, Cnr Nicholson & Bannister Rd\'s, Canning Vale, 6155, WA, A], [TAR, 5966, DC, Huntingwood DC, Huntingwood DC, 35 Huntingwood Drive, Huntingwood, 2148, NSW, A], [TAR, 5967, DC, Hendra DC, Hendra DC, Cnr Headly Ave & Nudgee Road, Hendra, 4011, QLD, A], [TAR, 5968, DC, Beverly DC, Beverly DC, 117 Main Street, Beverly, 5009, SA, A], [TAR, 5969, DC, Woodlands DC (DO NOT USE), Woodlands DC, Lot 9 Mills Road, Braeside, 3195, VIC, A]]')
		select('Table', 'rows:[11,12,13,14,15,16,17,18,19,20],columns:[4|Loc_Name]')
		select_menu('Data>>Table View #{Selected Records#}')
##		select('Table2', 'rows:[11,12,13,14,15,16,17,18,19,20],columns:[4|Loc_Name]')
		select('Table', 'cell:4|Loc_Name,3(State  Warehouse NSW)')
		assert_p('Table', 'Text', 'State  Warehouse NSW', '4|Loc_Name,3')
		select('Table', 'cell:4|Loc_Name,5(State Warehouse SA)')
		assert_p('Table', 'Text', 'cell:4|Loc_Name,5(State Warehouse SA)')
		select('Table', 'cell:4|Loc_Name,7(State Warehouse QLD)')
		assert_p('Table', 'Content', '[[TAR, 5951, DC, NSW West Sydney Ad Support, , , , , , A], [TAR, 5952, DC, TAS Ad Support, , , , , , A], [TAR, 5953, DC, North Geelong Warehouse, Target Head Office, 12 Thompson Road, North Geelong, 3215, VIC, A], [TAR, 5954, DC, State  Warehouse NSW, Target State Warehouse NSW (Westgate), Warehouse D Murtha Street, Arndell Park, 2148, NSW, A], [TAR, 5955, DC, State Warehouse VIC, Target State Warehouse VIC (Patricks), 180 Fitzgerald Road, Laverton, 3028, VIC, A], [TAR, 5957, DC, State Warehouse SA, Target State Warehouse  (Patricks), 180 Fitzgerald Road, Laverton, 3028, VIC, A], [TAR, 5958, DC, State Warehouse  WA, Target State Warehouse (WA) FCL, 56 Dowd Street, Welshpool, 6106, WA, A], [TAR, 5956, DC, State Warehouse QLD, Target State Warehouse QLD (RMS), 243 Bradman Street, Acacia Ridge, 4110, QLD, A], [TAR, 5959, DC, NSW  South Sydney Ad Support, South Sydney Ad Support, 753 Hume Highway, Bass Hill, , NSW, A], [TAR, 5960, DC, NSW East Sydney Ad Support,  Building B, Portside Distribution Ce, 2 - 8 Mc Pherson Street,, Botany, 2019, NSW, A]]')
		select('Table', 'cell:2|Loc_Nbr,2(5953)')
		rightclick('Table', '2|Loc_Nbr,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:2|Loc_Nbr,2(5953)')
		select('Table', 'cell:Data,4(Target Head Office)')
		assert_p('Table', 'Text', 'Target Head Office', 'Data,4')
		select('Table', 'cell:Data,6(North Geelong)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5953, 5953], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , North Geelong Warehouse, North Geelong Warehouse], [Loc_Addr_Ln1, 5, , Target Head Office, Target Head Office], [Loc_Addr_Ln2, 6, , 12 Thompson Road, 12 Thompson Road], [Loc_Addr_Ln3, 7, , North Geelong, North Geelong], [Loc_Postcode, 8, , 3215, 3215], [Loc_State, 9, , VIC, VIC], [Loc_Actv_Ind, 10, , A, A]]')
		select('Table', 'cell:Data,6(North Geelong)')
		click('Right')
		select('Table', 'cell:Data,4(Target State Warehouse NSW (Westgate))')
		assert_p('Table', 'Text', 'cell:Data,4(Target State Warehouse NSW (Westgate))')
		select('Table', 'cell:Data,5(Warehouse D Murtha Street)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5954, 5954], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , State  Warehouse NSW, State  Warehouse NSW], [Loc_Addr_Ln1, 5, , Target State Warehouse NSW (Westgate), Target State Warehouse NSW (Westgate)], [Loc_Addr_Ln2, 6, , Warehouse D Murtha Street, Warehouse D Murtha Street], [Loc_Addr_Ln3, 7, , Arndell Park, Arndell Park], [Loc_Postcode, 8, , 2148, 2148], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('Table', 'cell:Data,5(Warehouse D Murtha Street)')
		click('Right')
		select('Table', 'cell:Data,4(Target State Warehouse VIC (Patricks))')
		assert_p('Table', 'Text', 'Target State Warehouse VIC (Patricks)', 'Data,4')
		select('Table', 'cell:Data,3(State Warehouse VIC)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5955, 5955], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , State Warehouse VIC, State Warehouse VIC], [Loc_Addr_Ln1, 5, , Target State Warehouse VIC (Patricks), Target State Warehouse VIC (Patricks)], [Loc_Addr_Ln2, 6, , 180 Fitzgerald Road, 180 Fitzgerald Road], [Loc_Addr_Ln3, 7, , Laverton, Laverton], [Loc_Postcode, 8, , 3028, 3028], [Loc_State, 9, , VIC, VIC], [Loc_Actv_Ind, 10, , A, A]]')
		select('Table', 'cell:Data,3(State Warehouse VIC)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		#click('WindowsInternalFrameTitlePane', 215, 7)
		#click('WindowsInternalFrameTitlePane', 211, 19)
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
