from django.shortcuts import render
from booktest.models import BookInfo, HeroInfo
from datetime import date
from django.db.models import F, Q, Sum

# Create your views here.


# book = BookInfo(
#     btitle= '三国演义',
#     bpub_date= date(1988,1,1),
#     bread= 10,
#     bcomment=10
# )
# book.save()

# hero = HeroInfo(
#     hname= '曹操',
#     hgender= 0,
#     hbook= book,
# )
# hero.save()

# HeroInfo.objects.create(
#     hname= '刘备',
#     hgender=0,
#     hbook=book
# )


# BookInfo.objects.all()

# BookInfo.objects.get(id=1)
# BookInfo.objects.filter(id=1)

# BookInfo.objects.count()

# BookInfo.objects.filter(btitle__contains='湖')

# BookInfo.objects.filter(btitle__endswith='部')

# BookInfo.objects.filter(btitle__isnull=False)

# BookInfo.objects.filter(id__in=[2,4])

# BookInfo.objects.filter(id__gt=2)

# BookInfo.objects.exclude(id=3)

# BookInfo.objects.filter(bpub_date__year='1980')

# BookInfo.objects.filter(bpub_date__gt=date(1990,1,1))

# BookInfo.objects.filter(bread__gte=F('bcomment'))

# BookInfo.objects.filter(bread__gt=F('bcomment')*2)

# BookInfo.objects.filter(bread__gt=20, id__lt=3)

# BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)

# BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))

# BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))

# BookInfo.objects.filter(~Q(id=3))

# BookInfo.objects.aggregate(Sum('bread'))

# BookInfo.objects.all().order_by('bread')
# BookInfo.objects.all().order_by('-bread')


# b = BookInfo.objects.get(id=1)
# b.heroinfo_set.all()

# h = HeroInfo.objects.get(id=1)
# h.hbook
#
# BookInfo.objects.filter(heroinfo__hcomment__contains='降龙')

# HeroInfo.objects.filter(hbook__btitle='天龙八部')

# HeroInfo.objects.filter(hbook__bread__gt=30)

# hero = HeroInfo.objects.get(hname='曹操')
# hero.hname = '司马懿'
# hero.save()

# HeroInfo.objects.filter(hname='刘备').update(hname='诸葛亮')

# hero = HeroInfo.objects.get(id=19)
# hero.delete()

# HeroInfo.objects.filter(id=18).delete()


BookInfo.objects.filter(bread__gt=30).order_by('bpub_date')