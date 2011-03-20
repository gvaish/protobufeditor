useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Protocol Buffer Editor'):
		select('FileChooser', commonBits.sampleDir() + 'ProtoTest_Address1_SD.bin')
		select('ComboBox', 'Single Message')
		select('ComboBox', 'Self Describing Message')
		click('Edit1')
#		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,2')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'PhoneNumber')
		assert_p('JTreeTable', 'Content', '[[, , , ], [, , , ], [, , , ], [, , , ], [, , , ], [, , 110001, MOBILE], [, , 120001, HOME], [, , 130001, WORK], [, , , ], [, , , ], [, , 110002, MOBILE], [, , 120002, HOME], [, , 130002, WORK], [, , , ], [, , , ], [, , 110003, MOBILE], [, , 120003, HOME], [, , 130003, WORK], [, , , ], [, , , ], [, , 110004, MOBILE], [, , 120004, HOME], [, , 130004, WORK], [, , , ], [, , , ], [, , 110005, MOBILE], [, , 120005, HOME], [, , 130005, WORK], [, , , ], [, , , ], [, , 110006, MOBILE], [, , 120006, HOME], [, , 130006, WORK], [, , , ], [, , , ], [, , 110007, MOBILE], [, , 120007, HOME], [, , 130007, WORK], [, , , ], [, , , ], [, , 110008, MOBILE], [, , 120008, HOME], [, , 130008, WORK], [, , , ], [, , , ], [, , 110009, MOBILE], [, , 120009, HOME], [, , 130009, WORK], [, , , ], [, , , ], [, , 110010, MOBILE], [, , 120010, HOME], [, , 130010, WORK], [, , , ], [, , , ], [, , 110011, MOBILE], [, , 120011, HOME], [, , 130011, WORK], [, , , ], [, , , ], [, , 110012, MOBILE], [, , 120012, HOME], [, , 130012, WORK], [, , , ], [, , , ], [, , 110013, MOBILE], [, , 120013, HOME], [, , 130013, WORK], [, , , ], [, , , ], [, , 110014, MOBILE], [, , 120014, HOME], [, , 130014, WORK], [, , , ], [, , , ], [, , 110015, MOBILE], [, , 120015, HOME], [, , 130015, WORK], [, , , ], [, , , ], [, , 110016, MOBILE], [, , 120016, HOME], [, , 130016, WORK], [, , , ], [, , , ], [, , 110017, MOBILE], [, , 120017, HOME], [, , 130017, WORK], [, , , ], [, , , ], [, , 110018, MOBILE], [, , 120018, HOME], [, , 130018, WORK], [, , , ], [, , , ], [, , 110019, MOBILE], [, , 120019, HOME], [, , 130019, WORK], [, , , ], [, , , ], [, , 110020, MOBILE], [, , 120020, HOME], [, , 130020, WORK], [, , , ], [, , , ], [, , 110021, MOBILE], [, , 120021, HOME], [, , 130021, WORK], [, , , ], [, , , ], [, , 110022, MOBILE], [, , 120022, HOME], [, , 130022, WORK], [, , , ], [, , , ], [, , 110023, MOBILE], [, , 120023, HOME], [, , 130023, WORK], [, , , ], [, , , ], [, , 110024, MOBILE], [, , 120024, HOME], [, , 130024, WORK], [, , , ], [, , , ], [, , 110025, MOBILE], [, , 120025, HOME], [, , 130025, WORK], [, , , ], [, , , ], [, , 110026, MOBILE], [, , 120026, HOME], [, , 130026, WORK], [, , , ], [, , , ], [, , 110027, MOBILE], [, , 120027, HOME], [, , 130027, WORK], [, , , ], [, , , ], [, , 110028, MOBILE], [, , 120028, HOME], [, , 130028, WORK], [, , , ], [, , , ], [, , 110029, MOBILE], [, , 120029, HOME], [, , 130029, WORK], [, , , ], [, , , ], [, , 110030, MOBILE], [, , 120030, HOME], [, , 130030, WORK], [, , , ], [, , , ], [, , 110031, MOBILE], [, , 120031, HOME], [, , 130031, WORK], [, , , ], [, , , ], [, , 110032, MOBILE], [, , 120032, HOME], [, , 130032, WORK], [, , , ], [, , , ], [, , 110033, MOBILE], [, , 120033, HOME], [, , 130033, WORK], [, , , ], [, , , ], [, , 110034, MOBILE], [, , 120034, HOME], [, , 130034, WORK], [, , , ], [, , , ], [, , 110035, MOBILE], [, , 120035, HOME], [, , 130035, WORK], [, , , ], [, , , ], [, , 110036, MOBILE], [, , 120036, HOME], [, , 130036, WORK], [, , , ], [, , , ], [, , 110037, MOBILE], [, , 120037, HOME], [, , 130037, WORK], [, , , ], [, , , ], [, , 110038, MOBILE], [, , 120038, HOME], [, , 130038, WORK], [, , , ], [, , , ], [, , 110039, MOBILE], [, , 120039, HOME], [, , 130039, WORK], [, , , ], [, , , ], [, , 110040, MOBILE], [, , 120040, HOME], [, , 130040, WORK], [, , , ], [, , , ], [, , 110041, MOBILE], [, , 120041, HOME], [, , 130041, WORK], [, , , ], [, , , ], [, , 110042, MOBILE], [, , 120042, HOME], [, , 130042, WORK], [, , , ], [, , , ], [, , 110043, MOBILE], [, , 120043, HOME], [, , 130043, WORK], [, , , ], [, , , ], [, , 110044, MOBILE], [, , 120044, HOME], [, , 130044, WORK], [, , , ], [, , , ], [, , 110045, MOBILE], [, , 120045, HOME], [, , 130045, WORK], [, , , ], [, , , ], [, , 110046, MOBILE], [, , 120046, HOME], [, , 130046, WORK], [, , , ], [, , , ], [, , 110047, MOBILE], [, , 120047, HOME], [, , 130047, WORK], [, , , ], [, , , ], [, , 110048, MOBILE], [, , 120048, HOME], [, , 130048, WORK], [, , , ], [, , , ], [, , 110049, MOBILE], [, , 120049, HOME], [, , 130049, WORK]]')
		select_menu('View>>Show Proto Definition')
##		assert_p('JTreeTable', 'Content', '[[, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , id, 2, LABEL_REQUIRED, TYPE_INT32, , , ], [, , email, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , phone, 4, LABEL_REPEATED, TYPE_MESSAGE, .tutorial.Person.PhoneNumber, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , number, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , type, 2, LABEL_OPTIONAL, TYPE_ENUM, .tutorial.Person.PhoneType, , HOME], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , proto_files, 1, LABEL_REQUIRED, TYPE_MESSAGE, .google.protobuf.FileDescriptorSet, , ], [, , person, 2, LABEL_REPEATED, TYPE_MESSAGE, .tutorial.Person, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , file, 1, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FileDescriptorProto, , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , package, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , dependency, 3, LABEL_REPEATED, TYPE_STRING, , , ], [, , message_type, 4, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto, , ], [, , enum_type, 5, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumDescriptorProto, , ], [, , service, 6, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.ServiceDescriptorProto, , ], [, , extension, 7, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , options, 8, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.FileOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , field, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , extension, 6, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , nested_type, 3, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto, , ], [, , enum_type, 4, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumDescriptorProto, , ], [, , extension_range, 5, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto.ExtensionRange, , ], [, , options, 7, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.MessageOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , start, 1, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , end, 2, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , number, 3, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , label, 4, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldDescriptorProto.Label, , ], [, , type, 5, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldDescriptorProto.Type, , ], [, , type_name, 6, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , extendee, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , default_value, 7, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , options, 8, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.FieldOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , value, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumValueDescriptorProto, , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.EnumOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , number, 2, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.EnumValueOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , method, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.MethodDescriptorProto, , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.ServiceOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , input_type, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , output_type, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , options, 4, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.MethodOptions, , ], [, , , , , , , , ], [, , , , , , , , ], [, , java_package, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , java_outer_classname, 8, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , java_multiple_files, 10, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , optimize_for, 9, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FileOptions.OptimizeMode, , SPEED], [, , cc_generic_services, 16, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , java_generic_services, 17, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , py_generic_services, 18, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , message_set_wire_format, 1, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , no_standard_descriptor_accessor, 2, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , ctype, 1, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldOptions.CType, , STRING], [, , packed, 2, LABEL_OPTIONAL, TYPE_BOOL, , , ], [, , deprecated, 3, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , experimental_map_key, 9, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , name, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption.NamePart, , ], [, , identifier_value, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , positive_int_value, 4, LABEL_OPTIONAL, TYPE_UINT64, , , ], [, , negative_int_value, 5, LABEL_OPTIONAL, TYPE_INT64, , , ], [, , double_value, 6, LABEL_OPTIONAL, TYPE_DOUBLE, , , ], [, , string_value, 7, LABEL_OPTIONAL, TYPE_BYTES, , , ], [, , , , , , , , ], [, , , , , , , , ], [, , , , , , , , ], [, , name_part, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , is_extension, 2, LABEL_REQUIRED, TYPE_BOOL, , , ], [, , , , , , , , ]]')
		assert_p('JTreeTable', 'Content', '[[, , , , , , , , ], [, , , , , , , , ], [, , addressbookSD.proto, , , , , , ], [, , , , , , , , ], [, , Person, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , id, 2, LABEL_REQUIRED, TYPE_INT32, , , ], [, , email, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , phone, 4, LABEL_REPEATED, TYPE_MESSAGE, .tutorial.Person.PhoneNumber, , ], [, , , , , , , , ], [, , PhoneNumber, , , , , , ], [, , , , , , , , ], [, , number, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , type, 2, LABEL_OPTIONAL, TYPE_ENUM, .tutorial.Person.PhoneType, , HOME], [, , , , , , , , ], [, , PhoneType, , , , , , ], [, , , , , , , , ], [, , MOBILE, , , , , , ], [, , HOME, , , , , , ], [, , WORK, , , , , , ], [, , AddressBook, , , , , , ], [, , , , , , , , ], [, , proto_files, 1, LABEL_REQUIRED, TYPE_MESSAGE, .google.protobuf.FileDescriptorSet, , ], [, , person, 2, LABEL_REPEATED, TYPE_MESSAGE, .tutorial.Person, , ], [, , com.example.tutorial, , , , , , ], [, , google/protobuf/descriptor.proto, , , , , , ], [, , , , , , , , ], [, , FileDescriptorSet, , , , , , ], [, , , , , , , , ], [, , file, 1, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FileDescriptorProto, , ], [, , FileDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , package, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , dependency, 3, LABEL_REPEATED, TYPE_STRING, , , ], [, , message_type, 4, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto, , ], [, , enum_type, 5, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumDescriptorProto, , ], [, , service, 6, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.ServiceDescriptorProto, , ], [, , extension, 7, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , options, 8, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.FileOptions, , ], [, , DescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , field, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , extension, 6, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.FieldDescriptorProto, , ], [, , nested_type, 3, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto, , ], [, , enum_type, 4, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumDescriptorProto, , ], [, , extension_range, 5, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.DescriptorProto.ExtensionRange, , ], [, , options, 7, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.MessageOptions, , ], [, , , , , , , , ], [, , ExtensionRange, , , , , , ], [, , , , , , , , ], [, , start, 1, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , end, 2, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , FieldDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , number, 3, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , label, 4, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldDescriptorProto.Label, , ], [, , type, 5, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldDescriptorProto.Type, , ], [, , type_name, 6, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , extendee, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , default_value, 7, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , options, 8, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.FieldOptions, , ], [, , , , , , , , ], [, , Type, , , , , , ], [, , , , , , , , ], [, , TYPE_DOUBLE, , , , , , ], [, , TYPE_FLOAT, , , , , , ], [, , TYPE_INT64, , , , , , ], [, , TYPE_UINT64, , , , , , ], [, , TYPE_INT32, , , , , , ], [, , TYPE_FIXED64, , , , , , ], [, , TYPE_FIXED32, , , , , , ], [, , TYPE_BOOL, , , , , , ], [, , TYPE_STRING, , , , , , ], [, , TYPE_GROUP, , , , , , ], [, , TYPE_MESSAGE, , , , , , ], [, , TYPE_BYTES, , , , , , ], [, , TYPE_UINT32, , , , , , ], [, , TYPE_ENUM, , , , , , ], [, , TYPE_SFIXED32, , , , , , ], [, , TYPE_SFIXED64, , , , , , ], [, , TYPE_SINT32, , , , , , ], [, , TYPE_SINT64, , , , , , ], [, , Label, , , , , , ], [, , , , , , , , ], [, , LABEL_OPTIONAL, , , , , , ], [, , LABEL_REQUIRED, , , , , , ], [, , LABEL_REPEATED, , , , , , ], [, , EnumDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , value, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.EnumValueDescriptorProto, , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.EnumOptions, , ], [, , EnumValueDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , number, 2, LABEL_OPTIONAL, TYPE_INT32, , , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.EnumValueOptions, , ], [, , ServiceDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , method, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.MethodDescriptorProto, , ], [, , options, 3, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.ServiceOptions, , ], [, , MethodDescriptorProto, , , , , , ], [, , , , , , , , ], [, , name, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , input_type, 2, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , output_type, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , options, 4, LABEL_OPTIONAL, TYPE_MESSAGE, .google.protobuf.MethodOptions, , ], [, , FileOptions, , , , , , ], [, , , , , , , , ], [, , java_package, 1, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , java_outer_classname, 8, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , java_multiple_files, 10, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , optimize_for, 9, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FileOptions.OptimizeMode, , SPEED], [, , cc_generic_services, 16, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , java_generic_services, 17, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , py_generic_services, 18, LABEL_OPTIONAL, TYPE_BOOL, , , true], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , OptimizeMode, , , , , , ], [, , , , , , , , ], [, , SPEED, , , , , , ], [, , CODE_SIZE, , , , , , ], [, , LITE_RUNTIME, , , , , , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , MessageOptions, , , , , , ], [, , , , , , , , ], [, , message_set_wire_format, 1, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , no_standard_descriptor_accessor, 2, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , FieldOptions, , , , , , ], [, , , , , , , , ], [, , ctype, 1, LABEL_OPTIONAL, TYPE_ENUM, .google.protobuf.FieldOptions.CType, , STRING], [, , packed, 2, LABEL_OPTIONAL, TYPE_BOOL, , , ], [, , deprecated, 3, LABEL_OPTIONAL, TYPE_BOOL, , , false], [, , experimental_map_key, 9, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , CType, , , , , , ], [, , , , , , , , ], [, , STRING, , , , , , ], [, , CORD, , , , , , ], [, , STRING_PIECE, , , , , , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , EnumOptions, , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , EnumValueOptions, , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , ServiceOptions, , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , MethodOptions, , , , , , ], [, , , , , , , , ], [, , uninterpreted_option, 999, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption, , ], [, , , , , , , , ], [, , 1000, , , , , , ], [, , UninterpretedOption, , , , , , ], [, , , , , , , , ], [, , name, 2, LABEL_REPEATED, TYPE_MESSAGE, .google.protobuf.UninterpretedOption.NamePart, , ], [, , identifier_value, 3, LABEL_OPTIONAL, TYPE_STRING, , , ], [, , positive_int_value, 4, LABEL_OPTIONAL, TYPE_UINT64, , , ], [, , negative_int_value, 5, LABEL_OPTIONAL, TYPE_INT64, , , ], [, , double_value, 6, LABEL_OPTIONAL, TYPE_DOUBLE, , , ], [, , string_value, 7, LABEL_OPTIONAL, TYPE_BYTES, , , ], [, , , , , , , , ], [, , NamePart, , , , , , ], [, , , , , , , , ], [, , name_part, 1, LABEL_REQUIRED, TYPE_STRING, , , ], [, , is_extension, 2, LABEL_REQUIRED, TYPE_BOOL, , , ], [, , com.google.protobuf, , , , , , ]]')

	close()
