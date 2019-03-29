from rest_framework import serializers

from .models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookInfo  #　指明模型类
        fields = '__all__'  # 指明模型类的哪些字段生成
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
        # # exclude = ('image',)
        # extra_kwargs = {
        #     'bread':{'min_value':0, 'required':True},
        #     'bcomment':{'min_value':0, 'required':True}
        #
        # }
        # read_only_fields = ('id', 'bread', 'bcomment')
