// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: DTAR020.proto

package net.sf.RecordEditor.ProtoBuf.re.Test.Sales;

public final class DTAR020 {
  private DTAR020() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
  }
  public interface saleOrBuilder
      extends com.google.protobuf.MessageOrBuilder {
    
    // required int32 Keycode_no = 1;
    boolean hasKeycodeNo();
    int getKeycodeNo();
    
    // required int32 Store_No = 2;
    boolean hasStoreNo();
    int getStoreNo();
    
    // required int32 DATE = 3;
    boolean hasDATE();
    int getDATE();
    
    // required int32 Dept_No = 4;
    boolean hasDeptNo();
    int getDeptNo();
    
    // required int32 Qty_Sold = 5;
    boolean hasQtySold();
    int getQtySold();
    
    // required int64 Sale_Price = 6;
    boolean hasSalePrice();
    long getSalePrice();
  }
  public static final class sale extends
      com.google.protobuf.GeneratedMessage
      implements saleOrBuilder {
    // Use sale.newBuilder() to construct.
    private sale(Builder builder) {
      super(builder);
    }
    private sale(boolean noInit) {}
    
    private static final sale defaultInstance;
    public static sale getDefaultInstance() {
      return defaultInstance;
    }
    
    public sale getDefaultInstanceForType() {
      return defaultInstance;
    }
    
    public static final com.google.protobuf.Descriptors.Descriptor
        getDescriptor() {
      return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_descriptor;
    }
    
    protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
        internalGetFieldAccessorTable() {
      return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_fieldAccessorTable;
    }
    
    private int bitField0_;
    // required int32 Keycode_no = 1;
    public static final int KEYCODE_NO_FIELD_NUMBER = 1;
    private int keycodeNo_;
    public boolean hasKeycodeNo() {
      return ((bitField0_ & 0x00000001) == 0x00000001);
    }
    public int getKeycodeNo() {
      return keycodeNo_;
    }
    
    // required int32 Store_No = 2;
    public static final int STORE_NO_FIELD_NUMBER = 2;
    private int storeNo_;
    public boolean hasStoreNo() {
      return ((bitField0_ & 0x00000002) == 0x00000002);
    }
    public int getStoreNo() {
      return storeNo_;
    }
    
    // required int32 DATE = 3;
    public static final int DATE_FIELD_NUMBER = 3;
    private int dATE_;
    public boolean hasDATE() {
      return ((bitField0_ & 0x00000004) == 0x00000004);
    }
    public int getDATE() {
      return dATE_;
    }
    
    // required int32 Dept_No = 4;
    public static final int DEPT_NO_FIELD_NUMBER = 4;
    private int deptNo_;
    public boolean hasDeptNo() {
      return ((bitField0_ & 0x00000008) == 0x00000008);
    }
    public int getDeptNo() {
      return deptNo_;
    }
    
    // required int32 Qty_Sold = 5;
    public static final int QTY_SOLD_FIELD_NUMBER = 5;
    private int qtySold_;
    public boolean hasQtySold() {
      return ((bitField0_ & 0x00000010) == 0x00000010);
    }
    public int getQtySold() {
      return qtySold_;
    }
    
    // required int64 Sale_Price = 6;
    public static final int SALE_PRICE_FIELD_NUMBER = 6;
    private long salePrice_;
    public boolean hasSalePrice() {
      return ((bitField0_ & 0x00000020) == 0x00000020);
    }
    public long getSalePrice() {
      return salePrice_;
    }
    
    private void initFields() {
      keycodeNo_ = 0;
      storeNo_ = 0;
      dATE_ = 0;
      deptNo_ = 0;
      qtySold_ = 0;
      salePrice_ = 0L;
    }
    private byte memoizedIsInitialized = -1;
    public final boolean isInitialized() {
      byte isInitialized = memoizedIsInitialized;
      if (isInitialized != -1) return isInitialized == 1;
      
      if (!hasKeycodeNo()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!hasStoreNo()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!hasDATE()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!hasDeptNo()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!hasQtySold()) {
        memoizedIsInitialized = 0;
        return false;
      }
      if (!hasSalePrice()) {
        memoizedIsInitialized = 0;
        return false;
      }
      memoizedIsInitialized = 1;
      return true;
    }
    
    public void writeTo(com.google.protobuf.CodedOutputStream output)
                        throws java.io.IOException {
      getSerializedSize();
      if (((bitField0_ & 0x00000001) == 0x00000001)) {
        output.writeInt32(1, keycodeNo_);
      }
      if (((bitField0_ & 0x00000002) == 0x00000002)) {
        output.writeInt32(2, storeNo_);
      }
      if (((bitField0_ & 0x00000004) == 0x00000004)) {
        output.writeInt32(3, dATE_);
      }
      if (((bitField0_ & 0x00000008) == 0x00000008)) {
        output.writeInt32(4, deptNo_);
      }
      if (((bitField0_ & 0x00000010) == 0x00000010)) {
        output.writeInt32(5, qtySold_);
      }
      if (((bitField0_ & 0x00000020) == 0x00000020)) {
        output.writeInt64(6, salePrice_);
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
          .computeInt32Size(1, keycodeNo_);
      }
      if (((bitField0_ & 0x00000002) == 0x00000002)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt32Size(2, storeNo_);
      }
      if (((bitField0_ & 0x00000004) == 0x00000004)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt32Size(3, dATE_);
      }
      if (((bitField0_ & 0x00000008) == 0x00000008)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt32Size(4, deptNo_);
      }
      if (((bitField0_ & 0x00000010) == 0x00000010)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt32Size(5, qtySold_);
      }
      if (((bitField0_ & 0x00000020) == 0x00000020)) {
        size += com.google.protobuf.CodedOutputStream
          .computeInt64Size(6, salePrice_);
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
    
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        com.google.protobuf.ByteString data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        com.google.protobuf.ByteString data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(byte[] data)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data).buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        byte[] data,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws com.google.protobuf.InvalidProtocolBufferException {
      return newBuilder().mergeFrom(data, extensionRegistry)
               .buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(java.io.InputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        java.io.InputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseDelimitedFrom(java.io.InputStream input)
        throws java.io.IOException {
      Builder builder = newBuilder();
      if (builder.mergeDelimitedFrom(input)) {
        return builder.buildParsed();
      } else {
        return null;
      }
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseDelimitedFrom(
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
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        com.google.protobuf.CodedInputStream input)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input).buildParsed();
    }
    public static net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale parseFrom(
        com.google.protobuf.CodedInputStream input,
        com.google.protobuf.ExtensionRegistryLite extensionRegistry)
        throws java.io.IOException {
      return newBuilder().mergeFrom(input, extensionRegistry)
               .buildParsed();
    }
    
    public static Builder newBuilder() { return Builder.create(); }
    public Builder newBuilderForType() { return newBuilder(); }
    public static Builder newBuilder(net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale prototype) {
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
       implements net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.saleOrBuilder {
      public static final com.google.protobuf.Descriptors.Descriptor
          getDescriptor() {
        return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_descriptor;
      }
      
      protected com.google.protobuf.GeneratedMessage.FieldAccessorTable
          internalGetFieldAccessorTable() {
        return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_fieldAccessorTable;
      }
      
      // Construct using net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.newBuilder()
      private Builder() {
        maybeForceBuilderInitialization();
      }
      
      private Builder(BuilderParent parent) {
        super(parent);
        maybeForceBuilderInitialization();
      }
      private void maybeForceBuilderInitialization() {
        if (com.google.protobuf.GeneratedMessage.alwaysUseFieldBuilders) {
        }
      }
      private static Builder create() {
        return new Builder();
      }
      
      public Builder clear() {
        super.clear();
        keycodeNo_ = 0;
        bitField0_ = (bitField0_ & ~0x00000001);
        storeNo_ = 0;
        bitField0_ = (bitField0_ & ~0x00000002);
        dATE_ = 0;
        bitField0_ = (bitField0_ & ~0x00000004);
        deptNo_ = 0;
        bitField0_ = (bitField0_ & ~0x00000008);
        qtySold_ = 0;
        bitField0_ = (bitField0_ & ~0x00000010);
        salePrice_ = 0L;
        bitField0_ = (bitField0_ & ~0x00000020);
        return this;
      }
      
      public Builder clone() {
        return create().mergeFrom(buildPartial());
      }
      
      public com.google.protobuf.Descriptors.Descriptor
          getDescriptorForType() {
        return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.getDescriptor();
      }
      
      public net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale getDefaultInstanceForType() {
        return net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.getDefaultInstance();
      }
      
      public net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale build() {
        net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(result);
        }
        return result;
      }
      
      private net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale buildParsed()
          throws com.google.protobuf.InvalidProtocolBufferException {
        net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale result = buildPartial();
        if (!result.isInitialized()) {
          throw newUninitializedMessageException(
            result).asInvalidProtocolBufferException();
        }
        return result;
      }
      
      public net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale buildPartial() {
        net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale result = new net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale(this);
        int from_bitField0_ = bitField0_;
        int to_bitField0_ = 0;
        if (((from_bitField0_ & 0x00000001) == 0x00000001)) {
          to_bitField0_ |= 0x00000001;
        }
        result.keycodeNo_ = keycodeNo_;
        if (((from_bitField0_ & 0x00000002) == 0x00000002)) {
          to_bitField0_ |= 0x00000002;
        }
        result.storeNo_ = storeNo_;
        if (((from_bitField0_ & 0x00000004) == 0x00000004)) {
          to_bitField0_ |= 0x00000004;
        }
        result.dATE_ = dATE_;
        if (((from_bitField0_ & 0x00000008) == 0x00000008)) {
          to_bitField0_ |= 0x00000008;
        }
        result.deptNo_ = deptNo_;
        if (((from_bitField0_ & 0x00000010) == 0x00000010)) {
          to_bitField0_ |= 0x00000010;
        }
        result.qtySold_ = qtySold_;
        if (((from_bitField0_ & 0x00000020) == 0x00000020)) {
          to_bitField0_ |= 0x00000020;
        }
        result.salePrice_ = salePrice_;
        result.bitField0_ = to_bitField0_;
        onBuilt();
        return result;
      }
      
      public Builder mergeFrom(com.google.protobuf.Message other) {
        if (other instanceof net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale) {
          return mergeFrom((net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale)other);
        } else {
          super.mergeFrom(other);
          return this;
        }
      }
      
      public Builder mergeFrom(net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale other) {
        if (other == net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.getDefaultInstance()) return this;
        if (other.hasKeycodeNo()) {
          setKeycodeNo(other.getKeycodeNo());
        }
        if (other.hasStoreNo()) {
          setStoreNo(other.getStoreNo());
        }
        if (other.hasDATE()) {
          setDATE(other.getDATE());
        }
        if (other.hasDeptNo()) {
          setDeptNo(other.getDeptNo());
        }
        if (other.hasQtySold()) {
          setQtySold(other.getQtySold());
        }
        if (other.hasSalePrice()) {
          setSalePrice(other.getSalePrice());
        }
        this.mergeUnknownFields(other.getUnknownFields());
        return this;
      }
      
      public final boolean isInitialized() {
        if (!hasKeycodeNo()) {
          
          return false;
        }
        if (!hasStoreNo()) {
          
          return false;
        }
        if (!hasDATE()) {
          
          return false;
        }
        if (!hasDeptNo()) {
          
          return false;
        }
        if (!hasQtySold()) {
          
          return false;
        }
        if (!hasSalePrice()) {
          
          return false;
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
            case 8: {
              bitField0_ |= 0x00000001;
              keycodeNo_ = input.readInt32();
              break;
            }
            case 16: {
              bitField0_ |= 0x00000002;
              storeNo_ = input.readInt32();
              break;
            }
            case 24: {
              bitField0_ |= 0x00000004;
              dATE_ = input.readInt32();
              break;
            }
            case 32: {
              bitField0_ |= 0x00000008;
              deptNo_ = input.readInt32();
              break;
            }
            case 40: {
              bitField0_ |= 0x00000010;
              qtySold_ = input.readInt32();
              break;
            }
            case 48: {
              bitField0_ |= 0x00000020;
              salePrice_ = input.readInt64();
              break;
            }
          }
        }
      }
      
      private int bitField0_;
      
      // required int32 Keycode_no = 1;
      private int keycodeNo_ ;
      public boolean hasKeycodeNo() {
        return ((bitField0_ & 0x00000001) == 0x00000001);
      }
      public int getKeycodeNo() {
        return keycodeNo_;
      }
      public Builder setKeycodeNo(int value) {
        bitField0_ |= 0x00000001;
        keycodeNo_ = value;
        onChanged();
        return this;
      }
      public Builder clearKeycodeNo() {
        bitField0_ = (bitField0_ & ~0x00000001);
        keycodeNo_ = 0;
        onChanged();
        return this;
      }
      
      // required int32 Store_No = 2;
      private int storeNo_ ;
      public boolean hasStoreNo() {
        return ((bitField0_ & 0x00000002) == 0x00000002);
      }
      public int getStoreNo() {
        return storeNo_;
      }
      public Builder setStoreNo(int value) {
        bitField0_ |= 0x00000002;
        storeNo_ = value;
        onChanged();
        return this;
      }
      public Builder clearStoreNo() {
        bitField0_ = (bitField0_ & ~0x00000002);
        storeNo_ = 0;
        onChanged();
        return this;
      }
      
      // required int32 DATE = 3;
      private int dATE_ ;
      public boolean hasDATE() {
        return ((bitField0_ & 0x00000004) == 0x00000004);
      }
      public int getDATE() {
        return dATE_;
      }
      public Builder setDATE(int value) {
        bitField0_ |= 0x00000004;
        dATE_ = value;
        onChanged();
        return this;
      }
      public Builder clearDATE() {
        bitField0_ = (bitField0_ & ~0x00000004);
        dATE_ = 0;
        onChanged();
        return this;
      }
      
      // required int32 Dept_No = 4;
      private int deptNo_ ;
      public boolean hasDeptNo() {
        return ((bitField0_ & 0x00000008) == 0x00000008);
      }
      public int getDeptNo() {
        return deptNo_;
      }
      public Builder setDeptNo(int value) {
        bitField0_ |= 0x00000008;
        deptNo_ = value;
        onChanged();
        return this;
      }
      public Builder clearDeptNo() {
        bitField0_ = (bitField0_ & ~0x00000008);
        deptNo_ = 0;
        onChanged();
        return this;
      }
      
      // required int32 Qty_Sold = 5;
      private int qtySold_ ;
      public boolean hasQtySold() {
        return ((bitField0_ & 0x00000010) == 0x00000010);
      }
      public int getQtySold() {
        return qtySold_;
      }
      public Builder setQtySold(int value) {
        bitField0_ |= 0x00000010;
        qtySold_ = value;
        onChanged();
        return this;
      }
      public Builder clearQtySold() {
        bitField0_ = (bitField0_ & ~0x00000010);
        qtySold_ = 0;
        onChanged();
        return this;
      }
      
      // required int64 Sale_Price = 6;
      private long salePrice_ ;
      public boolean hasSalePrice() {
        return ((bitField0_ & 0x00000020) == 0x00000020);
      }
      public long getSalePrice() {
        return salePrice_;
      }
      public Builder setSalePrice(long value) {
        bitField0_ |= 0x00000020;
        salePrice_ = value;
        onChanged();
        return this;
      }
      public Builder clearSalePrice() {
        bitField0_ = (bitField0_ & ~0x00000020);
        salePrice_ = 0L;
        onChanged();
        return this;
      }
      
      // @@protoc_insertion_point(builder_scope:net.sf.RecordEditor.ProtoBuf.re.Test.Sales.sale)
    }
    
    static {
      defaultInstance = new sale(true);
      defaultInstance.initFields();
    }
    
    // @@protoc_insertion_point(class_scope:net.sf.RecordEditor.ProtoBuf.re.Test.Sales.sale)
  }
  
  private static com.google.protobuf.Descriptors.Descriptor
    internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_descriptor;
  private static
    com.google.protobuf.GeneratedMessage.FieldAccessorTable
      internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_fieldAccessorTable;
  
  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\rDTAR020.proto\022*net.sf.RecordEditor.Pro" +
      "toBuf.re.Test.Sales\"q\n\004sale\022\022\n\nKeycode_n" +
      "o\030\001 \002(\005\022\020\n\010Store_No\030\002 \002(\005\022\014\n\004DATE\030\003 \002(\005\022" +
      "\017\n\007Dept_No\030\004 \002(\005\022\020\n\010Qty_Sold\030\005 \002(\005\022\022\n\nSa" +
      "le_Price\030\006 \002(\003B\002H\001"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
      new com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner() {
        public com.google.protobuf.ExtensionRegistry assignDescriptors(
            com.google.protobuf.Descriptors.FileDescriptor root) {
          descriptor = root;
          internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_descriptor =
            getDescriptor().getMessageTypes().get(0);
          internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_fieldAccessorTable = new
            com.google.protobuf.GeneratedMessage.FieldAccessorTable(
              internal_static_net_sf_RecordEditor_ProtoBuf_re_Test_Sales_sale_descriptor,
              new java.lang.String[] { "KeycodeNo", "StoreNo", "DATE", "DeptNo", "QtySold", "SalePrice", },
              net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.class,
              net.sf.RecordEditor.ProtoBuf.re.Test.Sales.DTAR020.sale.Builder.class);
          return null;
        }
      };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
        }, assigner);
  }
  
  // @@protoc_insertion_point(outer_class_scope)
}