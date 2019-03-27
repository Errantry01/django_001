from django.contrib import admin
from booktest.models import BookInfo, HeroInfo

# Register your models here.


# 如果想要调整admin站点样式需要定义模型站点管理类
class HeroInfoStack(admin.StackedInline):
    model = HeroInfo  # 要编辑的对象
    extra = 2  # 默认显示几个空格子


class BookInfoAdmin(admin.ModelAdmin):
    """调整书籍数据在站点界面显示"""
    list_per_page = 4

    actions_on_top = False
    actions_on_bottom = True

    list_display = ['id', 'btitle', 'bread', 'bcomment', 'bpub_date_format']

    """调整编辑页面"""
    fieldsets = (
        ('基本', {'fields':['btitle', 'bpub_date']}),
        ('高级', {
            'fields':['bread', 'bcomment'],
            'classes':('collapse',)
        })
    )

    inlines = [HeroInfoStack]  # 在书箱编辑页面关联展示 英雄数据


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    """调整英雄数据在站点展示"""
    list_display = ['id', 'hname', 'hcomment', 'hgender', 'hbook', 'read']

    list_filter = ['hbook', 'hgender']  # 设置右侧过滤栏

    search_fields = ['hname']  # 设置搜索框



admin.site.site_header = '传智书城'
admin.site.site_title = '传智书城MIS'
admin.site.index_title = '黄英使用传智书城MIS'





admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo)
