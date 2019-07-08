from django.db import models


# Create your models here.
class Cate(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'cate'


class Goods(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    cate = models.ForeignKey(Cate, on_delete=models.CASCADE)

    class Meta:
        db_table = 'goods'