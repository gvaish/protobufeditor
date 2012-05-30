// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: addressbookSD1.proto

package com.example.tutorial;

public final class AddressBookProtosSD1 {
  private AddressBookProtosSD1() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public interface AddressBookOrBuilder
      extends com.google.protobuf.MessageOrBuilder {
    
    // required .google.protobuf.FileDescriptorSet proto_files = 7;
    boolean hasProtoFiles();
    com.google.protobuf.DescriptorProtos.FileDescriptorSet getProtoFiles();
    com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder getProtoFilesOrBuilder();
    
    // repeated .tutorial.Person person = 12;
    java.util.List<com.example.tutorial.AddressbookSD1Person.Person> 
        getPersonList();
    com.example.tutorial.AddressbookSD1Person.Person getPerson(int index);
    int getPersonCount();
    java.util.List<? extends com.example.tutorial.AddressbookSD1Person.PersonOrBuilder> 
        getPersonOrBuilderList();
    com.example.tutorial.AddressbookSD1Person.PersonOrBuilder getPersonOrBuilder(
        int index);
  }
  public static final class AddressBook extends
      com.google.protobuf.GeneratedMessage
      implements AddressBookOrBuilder {
    // Use AddressBook.newBuilder() to construct.
    private AddressBook(Builder builder) {
      super(builder);
    }
    private AddressBook(boolean noInit) {}
    
    private static final AddressBook defaultInstance;
    public static AddressBook getDefaultInstance() {
      return defaultInstance;
    }
    
    public AddressBook getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return com.example.tutorial.AddressBookProtosSD1.internal_static_tutorial_AddressBook_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return com.example.tutorial.AddressBookProtosSD1.internal_static_tutorial_AddressBook_fieldAccessorTable;
    }
    
    private int bitField0_;
    // required .google.protobuf.FileDescriptorSet proto_files = 7;
    public static final int PROTO_FILES_FIELD_NUMBER = 7;
    private com.google.protobuf.DescriptorProtos.FileDescriptorSet protoFiles_;
    public boolean hasProtoFiles() {
      return ((bitField0_ & 0x00000001) == 0x00000001);
    }
    public com.google.protobuf.DescriptorProtos.FileDescriptorSet getProtoFiles() {
      return protoFiles_;
    }
    public com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder getProtoFilesOrBuilder() {
      return protoFiles_;
    }
    
    // repeated .tutorial.Person person = 12;
    public static final int PERSON_FIELD_NUMBER = 12;
    private java.util.List<com.example.tutorial.AddressbookSD1Person.Person> person_;
    public java.util.List<com.example.tutorial.AddressbookSD1Person.Person> getPersonList() {
      return person_;
    }
    public java.util.List<? extends com.example.tutorial.AddressbookSD1Person.PersonOrBuilder> 
        getPersonOrBuilderList() {
      return person_;
    }
    public int getPersonCount() {
      return person_.size();
    }
    public com.example.tutorial.AddressbookSD1Person.Person getPerson(int index) {
      return person_.get(index);
    }
    public com.example.tutorial.AddressbookSD1Person.PersonOrBuilder getPersonOrBuilder(
        int index) {
      return person_.get(index);
    }
    
    private void initFields() {
      protoFiles_ = com.google.protobuf.DescriptorProtos.FileDescriptorSet.getDefaultInstance();
      person_ = java.util.Collections.emptyList();
    }
    private byte memoizedIsInitialized = -1;
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized != -1) return isInitialized == 1;
      
      if (!hasProtoFiles()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!getProtoFiles().isInitialized()) {
        memoizedIsInitialized = 0;
        return false;
      }
      for (int i = 0; i < getPersonCount(); i++) {
        if (!getPerson(i).isInitialized()) {
          memoizedIsInitialized = 0;
          return false;
        }
      }
      memoizedIsInitialized = 1;
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (((bitField0_ & 0x00000001) == 0x00000001)) {
        output.writeMessage(7, protoFiles_);
      }
      for (int i = 0; i < person_.size(); i++) {
        output.writeMessage(12, person_.get(i));
      }
      getUnknownFields().writeTo(output);
    }
    
    private int memoizedSerializedSize = -1;
    public int getSerializedSize() {
      int size = memoizedSerializedSize;
      if (size != -1) return size;
    
      size = 0;
      if (((bitField0_ & 0x00000001) == 0x00000001)) {
        size += com.google.protobuf.CodedOutputStream
          .computeMessageSize(7, protoFiles_);
      }
      for (int i = 0; i < person_.size(); i++) {
        size += com.google.protobuf.CodedOutputStream
          .computeMessageSize(12, person_.get(i));
      }
      size += getUnknownFields().getSerializedSize();
      memoizedSerializedSize = size;
      return size;
    }
    
    private static final long serialVersionUID = 0L;
    @java.lang.Override
    protected java.lang.Object writeReplace()
        throws java.io.ObjectStreamException {
      return super.writeReplace();
    }
    
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseDelimitedFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input, extensionRegistry)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static com.example.tutorial.AddressBookProtosSD1.AddressBook parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(com.example.tutorial.AddressBookProtosSD1.AddressBook prototype) {
      return newBuilder().mergeFrom(prototype);
    }
    public Builder toBuilder() { return newBuilder(this); }
    
    @java.lang.Override
    protected Builder newBuilderForType(
        com.google.protobuf.GeneratedMessage.BuilderParent parent) {
      Builder builder = new Builder(parent);
      return builder;
    }
    public static final class Builder extends
        com.google.protobuf.GeneratedMessage.Builder<Builder>
       implements com.example.tutorial.AddressBookProtosSD1.AddressBookOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return com.example.tutorial.AddressBookProtosSD1.internal_static_tutorial_AddressBook_descriptor;
      }
      
      protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return com.example.tutorial.AddressBookProtosSD1.internal_static_tutorial_AddressBook_fieldAccessorTable;
      }
      
      // Construct using com.example.tutorial.AddressBookProtosSD1.AddressBook.newBuilder()
      private Builder() {
        maybeForceBuilderInitialization();
      }
      
      private Builder(BuilderParent parent) {
        super(parent);
        maybeForceBuilderInitialization();
      }
      private void maybeForceBuilderInitialization() {
        if (com.google.protobuf.GeneratedMessage.alwaysUseFieldBuilders) {
          getProtoFilesFieldBuilder();
          getPersonFieldBuilder();
        }
      }
      private static Builder create() {
        return new Builder();
      }
      
      public Builder clear() {
        super.clear();
        if (protoFilesBuilder_ == null) {
          protoFiles_ = com.google.protobuf.DescriptorProtos.FileDescriptorSet.getDefaultInstance();
        } else {
          protoFilesBuilder_.clear();
        }
        bitField0_ = (bitField0_ & ~0x00000001);
        if (personBuilder_ == null) {
          person_ = java.util.Collections.emptyList();
          bitField0_ = (bitField0_ & ~0x00000002);
        } else {
          personBuilder_.clear();
        }
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(buildPartial());
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return com.example.tutorial.AddressBookProtosSD1.AddressBook.getDescriptor();
      }
      
      public com.example.tutorial.AddressBookProtosSD1.AddressBook getDefaultInstanceForType() {
        return com.example.tutorial.AddressBookProtosSD1.AddressBook.getDefaultInstance();
      }
      
      public com.example.tutorial.AddressBookProtosSD1.AddressBook build() {
        com.example.tutorial.AddressBookProtosSD1.AddressBook result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }
      
      private com.example.tutorial.AddressBookProtosSD1.AddressBook buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        com.example.tutorial.AddressBookProtosSD1.AddressBook result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return result;
      }
      
      public com.example.tutorial.AddressBookProtosSD1.AddressBook buildPartial() {
        com.example.tutorial.AddressBookProtosSD1.AddressBook result = new com.example.tutorial.AddressBookProtosSD1.AddressBook(this);
        int from_bitField0_ = bitField0_;
        int to_bitField0_ = 0;
        if (((from_bitField0_ & 0x00000001) == 0x00000001)) {
          to_bitField0_ |= 0x00000001;
        }
        if (protoFilesBuilder_ == null) {
          result.protoFiles_ = protoFiles_;
        } else {
          result.protoFiles_ = protoFilesBuilder_.build();
        }
        if (personBuilder_ == null) {
          if (((bitField0_ & 0x00000002) == 0x00000002)) {
            person_ = java.util.Collections.unmodifiableList(person_);
            bitField0_ = (bitField0_ & ~0x00000002);
          }
          result.person_ = person_;
        } else {
          result.person_ = personBuilder_.build();
        }
        result.bitField0_ = to_bitField0_;
        onBuilt();
        return result;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof com.example.tutorial.AddressBookProtosSD1.AddressBook) {
          return mergeFrom((com.example.tutorial.AddressBookProtosSD1.AddressBook)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(com.example.tutorial.AddressBookProtosSD1.AddressBook other) {
        if (other == com.example.tutorial.AddressBookProtosSD1.AddressBook.getDefaultInstance()) return this;
        if (other.hasProtoFiles()) {
          mergeProtoFiles(other.getProtoFiles());
        }
        if (personBuilder_ == null) {
          if (!other.person_.isEmpty()) {
            if (person_.isEmpty()) {
              person_ = other.person_;
              bitField0_ = (bitField0_ & ~0x00000002);
            } else {
              ensurePersonIsMutable();
              person_.addAll(other.person_);
            }
            onChanged();
          }
        } else {
          if (!other.person_.isEmpty()) {
            if (personBuilder_.isEmpty()) {
              personBuilder_.dispose();
              personBuilder_ = null;
              person_ = other.person_;
              bitField0_ = (bitField0_ & ~0x00000002);
              personBuilder_ = 
                com.google.protobuf.GeneratedMessage.alwaysUseFieldBuilders ?
                   getPersonFieldBuilder() : null;
            } else {
              personBuilder_.addAllMessages(other.person_);
            }
          }
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }
      
      public final boolean isInitialized() {
        if (!hasProtoFiles()) {
          
          return false;
        }
        if (!getProtoFiles().isInitialized()) {
          
          return false;
        }
        for (int i = 0; i < getPersonCount(); i++) {
          if (!getPerson(i).isInitialized()) {
            
            return false;
          }
        }
        return true;
      }
      
      public Builder mergeFrom(
          com.google.protobuf.CodedInputStream input,
          com.google.protobuf.ExtensionRegistryLite extensionRegistry)
          throws java.io.IOException {
        com.google.protobuf.UnknownFieldSet.Builder unknownFields =
          com.google.protobuf.UnknownFieldSet.newBuilder(
            this.getUnknownFields());
        while (true) {
          int tag = input.readTag();
          switch (tag) {
            case 0:
              this.setUnknownFields(unknownFields.build());
              onChanged();
              return this;
            default: {
              if (!parseUnknownField(input, unknownFields,
                                     extensionRegistry, tag)) {
                this.setUnknownFields(unknownFields.build());
                onChanged();
                return this;
              }
              break;
            }
            case 58: {
              com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder subBuilder = com.google.protobuf.DescriptorProtos.FileDescriptorSet.newBuilder();
              if (hasProtoFiles()) {
                subBuilder.mergeFrom(getProtoFiles());
              }
              input.readMessage(subBuilder, extensionRegistry);
              setProtoFiles(subBuilder.buildPartial());
              break;
            }
            case 98: {
              com.example.tutorial.AddressbookSD1Person.Person.Builder subBuilder = com.example.tutorial.AddressbookSD1Person.Person.newBuilder();
              input.readMessage(subBuilder, extensionRegistry);
              addPerson(subBuilder.buildPartial());
              break;
            }
          }
        }
      }
      
      private int bitField0_;
      
      // required .google.protobuf.FileDescriptorSet proto_files = 7;
      private com.google.protobuf.DescriptorProtos.FileDescriptorSet protoFiles_ = com.google.protobuf.DescriptorProtos.FileDescriptorSet.getDefaultInstance();
      private com.google.protobuf.SingleFieldBuilder<
          com.google.protobuf.DescriptorProtos.FileDescriptorSet, com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder, com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder> protoFilesBuilder_;
      public boolean hasProtoFiles() {
        return ((bitField0_ & 0x00000001) == 0x00000001);
      }
      public com.google.protobuf.DescriptorProtos.FileDescriptorSet getProtoFiles() {
        if (protoFilesBuilder_ == null) {
          return protoFiles_;
        } else {
          return protoFilesBuilder_.getMessage();
        }
      }
      public Builder setProtoFiles(com.google.protobuf.DescriptorProtos.FileDescriptorSet value) {
        if (protoFilesBuilder_ == null) {
          if (value == null) {
            throw new NullPointerException();
          }
          protoFiles_ = value;
          onChanged();
        } else {
          protoFilesBuilder_.setMessage(value);
        }
        bitField0_ |= 0x00000001;
        return this;
      }
      public Builder setProtoFiles(
          com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder builderForValue) {
        if (protoFilesBuilder_ == null) {
          protoFiles_ = builderForValue.build();
          onChanged();
        } else {
          protoFilesBuilder_.setMessage(builderForValue.build());
        }
        bitField0_ |= 0x00000001;
        return this;
      }
      public Builder mergeProtoFiles(com.google.protobuf.DescriptorProtos.FileDescriptorSet value) {
        if (protoFilesBuilder_ == null) {
          if (((bitField0_ & 0x00000001) == 0x00000001) &&
              protoFiles_ != com.google.protobuf.DescriptorProtos.FileDescriptorSet.getDefaultInstance()) {
            protoFiles_ =
              com.google.protobuf.DescriptorProtos.FileDescriptorSet.newBuilder(protoFiles_).mergeFrom(value).buildPartial();
          } else {
            protoFiles_ = value;
          }
          onChanged();
        } else {
          protoFilesBuilder_.mergeFrom(value);
        }
        bitField0_ |= 0x00000001;
        return this;
      }
      public Builder clearProtoFiles() {
        if (protoFilesBuilder_ == null) {
          protoFiles_ = com.google.protobuf.DescriptorProtos.FileDescriptorSet.getDefaultInstance();
          onChanged();
        } else {
          protoFilesBuilder_.clear();
        }
        bitField0_ = (bitField0_ & ~0x00000001);
        return this;
      }
      public com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder getProtoFilesBuilder() {
        bitField0_ |= 0x00000001;
        onChanged();
        return getProtoFilesFieldBuilder().getBuilder();
      }
      public com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder getProtoFilesOrBuilder() {
        if (protoFilesBuilder_ != null) {
          return protoFilesBuilder_.getMessageOrBuilder();
        } else {
          return protoFiles_;
        }
      }
      private com.google.protobuf.SingleFieldBuilder<
          com.google.protobuf.DescriptorProtos.FileDescriptorSet, com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder, com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder> 
          getProtoFilesFieldBuilder() {
        if (protoFilesBuilder_ == null) {
          protoFilesBuilder_ = new com.google.protobuf.SingleFieldBuilder<
              com.google.protobuf.DescriptorProtos.FileDescriptorSet, com.google.protobuf.DescriptorProtos.FileDescriptorSet.Builder, com.google.protobuf.DescriptorProtos.FileDescriptorSetOrBuilder>(
                  protoFiles_,
                  getParentForChildren(),
                  isClean());
          protoFiles_ = null;
        }
        return protoFilesBuilder_;
      }
      
      // repeated .tutorial.Person person = 12;
      private java.util.List<com.example.tutorial.AddressbookSD1Person.Person> person_ =
        java.util.Collections.emptyList();
      private void ensurePersonIsMutable() {
        if (!((bitField0_ & 0x00000002) == 0x00000002)) {
          person_ = new java.util.ArrayList<com.example.tutorial.AddressbookSD1Person.Person>(person_);
          bitField0_ |= 0x00000002;
         }
      }
      
      private com.google.protobuf.RepeatedFieldBuilder<
          com.example.tutorial.AddressbookSD1Person.Person, com.example.tutorial.AddressbookSD1Person.Person.Builder, com.example.tutorial.AddressbookSD1Person.PersonOrBuilder> personBuilder_;
      
      public java.util.List<com.example.tutorial.AddressbookSD1Person.Person> getPersonList() {
        if (personBuilder_ == null) {
          return java.util.Collections.unmodifiableList(person_);
        } else {
          return personBuilder_.getMessageList();
        }
      }
      public int getPersonCount() {
        if (personBuilder_ == null) {
          return person_.size();
        } else {
          return personBuilder_.getCount();
        }
      }
      public com.example.tutorial.AddressbookSD1Person.Person getPerson(int index) {
        if (personBuilder_ == null) {
          return person_.get(index);
        } else {
          return personBuilder_.getMessage(index);
        }
      }
      public Builder setPerson(
          int index, com.example.tutorial.AddressbookSD1Person.Person value) {
        if (personBuilder_ == null) {
          if (value == null) {
            throw new NullPointerException();
          }
          ensurePersonIsMutable();
          person_.set(index, value);
          onChanged();
        } else {
          personBuilder_.setMessage(index, value);
        }
        return this;
      }
      public Builder setPerson(
          int index, com.example.tutorial.AddressbookSD1Person.Person.Builder builderForValue) {
        if (personBuilder_ == null) {
          ensurePersonIsMutable();
          person_.set(index, builderForValue.build());
          onChanged();
        } else {
          personBuilder_.setMessage(index, builderForValue.build());
        }
        return this;
      }
      public Builder addPerson(com.example.tutorial.AddressbookSD1Person.Person value) {
        if (personBuilder_ == null) {
          if (value == null) {
            throw new NullPointerException();
          }
          ensurePersonIsMutable();
          person_.add(value);
          onChanged();
        } else {
          personBuilder_.addMessage(value);
        }
        return this;
      }
      public Builder addPerson(
          int index, com.example.tutorial.AddressbookSD1Person.Person value) {
        if (personBuilder_ == null) {
          if (value == null) {
            throw new NullPointerException();
          }
          ensurePersonIsMutable();
          person_.add(index, value);
          onChanged();
        } else {
          personBuilder_.addMessage(index, value);
        }
        return this;
      }
      public Builder addPerson(
          com.example.tutorial.AddressbookSD1Person.Person.Builder builderForValue) {
        if (personBuilder_ == null) {
          ensurePersonIsMutable();
          person_.add(builderForValue.build());
          onChanged();
        } else {
          personBuilder_.addMessage(builderForValue.build());
        }
        return this;
      }
      public Builder addPerson(
          int index, com.example.tutorial.AddressbookSD1Person.Person.Builder builderForValue) {
        if (personBuilder_ == null) {
          ensurePersonIsMutable();
          person_.add(index, builderForValue.build());
          onChanged();
        } else {
          personBuilder_.addMessage(index, builderForValue.build());
        }
        return this;
      }
      public Builder addAllPerson(
          java.lang.Iterable<? extends com.example.tutorial.AddressbookSD1Person.Person> values) {
        if (personBuilder_ == null) {
          ensurePersonIsMutable();
          super.addAll(values, person_);
          onChanged();
        } else {
          personBuilder_.addAllMessages(values);
        }
        return this;
      }
      public Builder clearPerson() {
        if (personBuilder_ == null) {
          person_ = java.util.Collections.emptyList();
          bitField0_ = (bitField0_ & ~0x00000002);
          onChanged();
        } else {
          personBuilder_.clear();
        }
        return this;
      }
      public Builder removePerson(int index) {
        if (personBuilder_ == null) {
          ensurePersonIsMutable();
          person_.remove(index);
          onChanged();
        } else {
          personBuilder_.remove(index);
        }
        return this;
      }
      public com.example.tutorial.AddressbookSD1Person.Person.Builder getPersonBuilder(
          int index) {
        return getPersonFieldBuilder().getBuilder(index);
      }
      public com.example.tutorial.AddressbookSD1Person.PersonOrBuilder getPersonOrBuilder(
          int index) {
        if (personBuilder_ == null) {
          return person_.get(index);  } else {
          return personBuilder_.getMessageOrBuilder(index);
        }
      }
      public java.util.List<? extends com.example.tutorial.AddressbookSD1Person.PersonOrBuilder> 
           getPersonOrBuilderList() {
        if (personBuilder_ != null) {
          return personBuilder_.getMessageOrBuilderList();
        } else {
          return java.util.Collections.unmodifiableList(person_);
        }
      }
      public com.example.tutorial.AddressbookSD1Person.Person.Builder addPersonBuilder() {
        return getPersonFieldBuilder().addBuilder(
            com.example.tutorial.AddressbookSD1Person.Person.getDefaultInstance());
      }
      public com.example.tutorial.AddressbookSD1Person.Person.Builder addPersonBuilder(
          int index) {
        return getPersonFieldBuilder().addBuilder(
            index, com.example.tutorial.AddressbookSD1Person.Person.getDefaultInstance());
      }
      public java.util.List<com.example.tutorial.AddressbookSD1Person.Person.Builder> 
           getPersonBuilderList() {
        return getPersonFieldBuilder().getBuilderList();
      }
      private com.google.protobuf.RepeatedFieldBuilder<
          com.example.tutorial.AddressbookSD1Person.Person, com.example.tutorial.AddressbookSD1Person.Person.Builder, com.example.tutorial.AddressbookSD1Person.PersonOrBuilder> 
          getPersonFieldBuilder() {
        if (personBuilder_ == null) {
          personBuilder_ = new com.google.protobuf.RepeatedFieldBuilder<
              com.example.tutorial.AddressbookSD1Person.Person, com.example.tutorial.AddressbookSD1Person.Person.Builder, com.example.tutorial.AddressbookSD1Person.PersonOrBuilder>(
                  person_,
                  ((bitField0_ & 0x00000002) == 0x00000002),
                  getParentForChildren(),
                  isClean());
          person_ = null;
        }
        return personBuilder_;
      }
      
      // @@protoc_insertion_point(builder_scope:tutorial.AddressBook)
    }
    
    static {
      defaultInstance = new AddressBook(true);
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:tutorial.AddressBook)
  }
  
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_tutorial_AddressBook_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_tutorial_AddressBook_fieldAccessorTable;
  
  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\024addressbookSD1.proto\022\010tutorial\032 google" +
      "/protobuf/descriptor.proto\032\033addressbookS" +
      "D1_Person.proto\"h\n\013AddressBook\0227\n\013proto_" +
      "files\030\007 \002(\0132\".google.protobuf.FileDescri" +
      "ptorSet\022 \n\006person\030\014 \003(\0132\020.tutorial.Perso" +
      "nB,\n\024com.example.tutorialB\024AddressBookPr" +
      "otosSD1"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          internal_static_tutorial_AddressBook_descriptor =
            getDescriptor().getMessageTypes().get(0);
          internal_static_tutorial_AddressBook_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_tutorial_AddressBook_descriptor,
              new java.lang.String[] { "ProtoFiles", "Person", },
              com.example.tutorial.AddressBookProtosSD1.AddressBook.class,
              com.example.tutorial.AddressBookProtosSD1.AddressBook.Builder.class);
          return null;
        }
      };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
          com.google.protobuf.DescriptorProtos.getDescriptor(),
          com.example.tutorial.AddressbookSD1Person.getDescriptor(),
        }, assigner);
  }
  
  // @@protoc_insertion_point(outer_class_scope)
}
