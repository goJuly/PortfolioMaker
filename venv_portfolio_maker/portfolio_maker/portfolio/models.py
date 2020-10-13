from accounts.models import CustomUser
from django.db import models
from django import forms


class Portfolio(models.Model):

    portfolioName = models.CharField(verbose_name='ポートフォリオ名', max_length=40)
    userName = models.CharField(verbose_name='ユーザー名', max_length=100)
    introduction1 = models.TextField(verbose_name='自己紹介1', max_length=400, null=True)
    introduction2 = models.TextField(verbose_name='自己紹介2', max_length=400, null=True)
    product1 = models.TextField(verbose_name='紹介したいプロダクト１', max_length=400, null=True)
    productUrl1 = models.URLField(verbose_name='プロダクトURL1', max_length=400, null=True)
    product2 = models.TextField(verbose_name='紹介したいプロダクト2', max_length=400, null=True)
    productUrl2 = models.URLField(verbose_name='プロダクトURL2', max_length=400, null=True)
    product3 = models.TextField(verbose_name='紹介したいプロダクト3', max_length=400, null=True)
    productUrl3 = models.URLField(verbose_name='プロダクトURL3', max_length=400, null=True)
    image1 = models.ImageField(verbose_name='イメージ1', blank=True, null=True)
    image2 = models.ImageField(verbose_name='イメージ2', blank=True, null=True)
    image3 = models.ImageField(verbose_name='イメージ3', blank=True, null=True)
    extra1 = models.CharField(verbose_name='予備項目1', max_length=400, null=True)
    extra2 = models.CharField(verbose_name='予備項目2', max_length=400, null=True)
    extra3 = models.CharField(verbose_name='予備項目3', max_length=400, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now_add=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
