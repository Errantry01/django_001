from rest_framework import serializers
from booktest.models import BookInfo

# class BookInfoSerializer(serializers.ModelSerializer):
#     """BookInfo模型类的序列化器"""
#
#     class Meta:
#         model = BookInfo
#         fields = '__all__'


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)


    # 定义　一关联多的序列化器字段
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True) # 默认是将关联模型的id序列化
    # hbook = serializers.StringRelatedField(label='图书', read_only=True)  # 默认是将关联模型的__str__方法返回值序列化出来
    # hbook = BookInfoSerializer() # 关联模型对象的序列化器中所有字段序列化出来
    hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())



class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heroinfo_set = HeroInfoSerializer(many=True)


    def validate_btitle(self, value):
        """单个字段验证"""
        if 'django' not in value.lower():
            raise serializers.ValidationError('图书不是关于ｄｊａｎｇｏ的')

        return value

    # def validate(self, attrs):
    #     """多个字段联合验证"""
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #
    #     if bread < bcomment:
    #         raise serializers.ValidationError('阅读量小于评论量')
    #
    #     return attrs


    def create(self, validated_data):
        """新建"""
        # return BookInfo(**validated_data)
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance








