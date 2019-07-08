
from django.urls import path
from . import views

app_name = 'zi_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_cate', views.Add_cateView.as_view(), name='add_cate'),
    path('add_good', views.Add_goodsView.as_view(), name='add_good'),
    # path('index/', views.index, name='index')
]
