from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField


# Create your models here.

class BooksType(BaseModel):
    '''图书类型模型类'''
    name = models.CharField(max_length=20, verbose_name='种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='图书类型图片')

    class Meta:
        db_table = 'df_books_type'
        verbose_name = '图书种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Books(BaseModel):
    '''图书模型类'''
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )
    type = models.ForeignKey('BooksType', verbose_name='图书种类')
    name = models.CharField(max_length=20, verbose_name='图书名称')
    desc = models.CharField(max_length=256, verbose_name='图书简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = models.CharField(max_length=20, verbose_name='图书单位')
    image = models.ImageField(upload_to='books', verbose_name='图书图片')
    stock = models.IntegerField(default=1, verbose_name='图书库存')
    sales = models.IntegerField(default=0, verbose_name='图书销量')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='图书状态')
    detail = HTMLField(blank=True, verbose_name='图书详情')

    class Meta:
        db_table = 'df_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class BooksImage(BaseModel):
    '''图书图片模型类'''
    sku = models.ForeignKey('Books', verbose_name='图书')
    image = models.ImageField(upload_to='books', verbose_name='图片路径')

    class Meta:
        db_table = 'df_index_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class IndexBooksBanner(BaseModel):
    '''首页轮播商品展示模型类'''
    sku = models.ForeignKey('Books', verbose_name='图书')
    image = models.ImageField(upload_to='banner', verbose_name='图片')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name


class Index_TypeBooksBanner(BaseModel):
    '''首页分类商品展示模型类'''
    DISPLAY_TYPE_CHOICES = (
        (0, "标题"),
        (1, "图片"),
    )

    type = models.ForeignKey('BooksType', verbose_name='图书类型')
    sku = models.ForeignKey('Books', verbose_name='图书')
    display_type = models.SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
    index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = "主页分类展示商品"
        verbose_name_plural = verbose_name


class IndexPromotionBanner(BaseModel):
    '''首页促销活动模型类'''
    name = models.CharField(max_length=20, verbose_name='活动名称')
    url = models.URLField(verbose_name='活动链接')
    image = models.ImageField(upload_to='banner', verbose_name='活动图片')
    index = models.SmallIntegerField(default=0, verbose_name=展示顺序)

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = "主页促销活动"
        verbose_name_plural = verbose_name
