from django.db import models
from db.base_model import BaseModel


# Create your models here.

class OrderInfo(BaseModel):
    '''订单模型类'''
    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付')
    )
    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '代发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单ID')
    user = models.ForeignKey('user.User', verbose_name='用户')
    addr = models.ForeignKey('user.Address', verbose_name='地址')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='图书数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='图书总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')

    class Meta:
        db_table = 'df_order_info'
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderBooks(BaseModel):
    '''订单图书模型类'''
    order = models.ForeignKey('OrderInfo', verbose_name='订单')
    sku = models.ForeignKey('goods.Books', verbose_name='图书')
    count = models.IntegerField(default=1, verbose_name='图书数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='图书价格')
    comment = models.CharField(max_length=256, verbose_name='评论')


class Meta:
    db_table = 'df_order_books'
    verbose_name = '订单图书'
    verbose_name_plural = verbose_name
