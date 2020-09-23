from accounts.models import CustomUser
from django.db import models


class Portfolio(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    portfolioName = models.CharField(verbose_name='ポートフォリオ名', max_length=40)
    userName = models.CharField(verbose_name='ユーザー名', max_length=100)
    introduction1 = models.CharField(verbose_name='自己紹介1', max_length=400)
    introduction2 = models.CharField(verbose_name='自己紹介2', max_length=400)
    product1 = models.CharField(verbose_name='プロダクト1', max_length=400)
    productUrl1 = models.CharField(verbose_name='プロダクトURL1', max_length=400)
    product2 = models.CharField(verbose_name='プロダクト1', max_length=400)
    productUrl2 = models.CharField(verbose_name='プロダクトURL1', max_length=400)
    product3 = models.CharField(verbose_name='プロダクト1', max_length=400)
    productUrl3 = models.CharField(verbose_name='プロダクトURL1', max_length=400)
    image1 = models.ImageField(verbose_name='イメージ1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='イメージ2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='イメージ3', blank=True, null=True)
    extra1 = models.CharField(verbose_name='プロダクト1', max_length=400)
    extra2 = models.CharField(verbose_name='プロダクト2', max_length=400)
    extra3 = models.CharField(verbose_name='プロダクト3', max_length=400)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
