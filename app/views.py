from django.shortcuts import render
from django.views.generic import View
from . import models
import os
from django.conf import settings
from datetime import datetime
from decimal import *
from django.core.paginator import Paginator
# Create your views here.

class IndexView(View):
    def get(self, request):
        goods_list = models.Goods.objects.all()


        current_page = request.GET.get('p', 1)
        paginator = Paginator(goods_list, 2)
        page = paginator.page(current_page)
        return render(request, 'index.html', {'good': page,
                                              'current_page': current_page,
                                              'total_page': paginator.num_pages})

class Add_cateView(View):
    def get(self, request):
        return render(request, 'add_cate.html', {})

    def post(self, request):
        name = request.POST.get('name')
        a = models.Cate()
        a.name = name
        a.save()
        return render(request, 'add_cate.html', {'message':'添加成功'})


class Add_goodsView(View):
    def get(self, request):
        a = models.Cate.objects.all()
        return render(request, 'add_goods.html', {'cate': a})

    def post(self, request):
        cate = request.POST.get('cate')
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('img')

        fix_image = datetime.now().strftime('%Y%m%d%H%M%S%f') + 'user_id'
        path_image = os.path.join(settings.STATICFILES_DIRS[0], fix_image+image.name)
        f = open(path_image, 'wb')
        for chunk in image.chunks():
            f.write(chunk)
        f.close()

        a = models.Goods()
        a.name = name
        a.image = '/static/' + fix_image+image.name
        a.price = price
        a.cate_id = cate
        a.save()
        return render(request, 'add_goods.html', {'message':'添加成功'})

