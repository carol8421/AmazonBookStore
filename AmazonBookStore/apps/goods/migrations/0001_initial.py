# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='图书名称', max_length=20)),
                ('desc', models.CharField(verbose_name='图书简介', max_length=256)),
                ('price', models.DecimalField(verbose_name='商品价格', max_digits=10, decimal_places=2)),
                ('unite', models.CharField(verbose_name='图书单位', max_length=20)),
                ('image', models.ImageField(verbose_name='图书图片', upload_to='books')),
                ('stock', models.IntegerField(verbose_name='图书库存', default=1)),
                ('sales', models.IntegerField(verbose_name='图书销量', default=0)),
                ('status', models.SmallIntegerField(verbose_name='图书状态', default=1, choices=[(0, '下线'), (1, '上线')])),
                ('detail', tinymce.models.HTMLField(verbose_name='图书详情', blank=True)),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'df_books',
            },
        ),
        migrations.CreateModel(
            name='BooksImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('image', models.ImageField(verbose_name='图片路径', upload_to='books')),
                ('sku', models.ForeignKey(verbose_name='图书', to='goods.Books')),
            ],
            options={
                'verbose_name': '商品图片',
                'verbose_name_plural': '商品图片',
                'db_table': 'df_index_image',
            },
        ),
        migrations.CreateModel(
            name='BooksType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='种类名称', max_length=20)),
                ('logo', models.CharField(verbose_name='标识', max_length=20)),
                ('image', models.ImageField(verbose_name='图书类型图片', upload_to='type')),
            ],
            options={
                'verbose_name': '图书种类',
                'verbose_name_plural': '图书种类',
                'db_table': 'df_books_type',
            },
        ),
        migrations.CreateModel(
            name='Index_TypeBooksBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('display_type', models.SmallIntegerField(verbose_name='展示类型', default=1, choices=[(0, '标题'), (1, '图片')])),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
                ('sku', models.ForeignKey(verbose_name='图书', to='goods.Books')),
                ('type', models.ForeignKey(verbose_name='图书类型', to='goods.BooksType')),
            ],
            options={
                'verbose_name': '主页分类展示商品',
                'verbose_name_plural': '主页分类展示商品',
                'db_table': 'df_index_type_goods',
            },
        ),
        migrations.CreateModel(
            name='IndexBooksBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('image', models.ImageField(verbose_name='图片', upload_to='banner')),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
                ('sku', models.ForeignKey(verbose_name='图书', to='goods.Books')),
            ],
            options={
                'verbose_name': '首页轮播商品',
                'verbose_name_plural': '首页轮播商品',
                'db_table': 'df_index_banner',
            },
        ),
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='活动名称', max_length=20)),
                ('url', models.URLField(verbose_name='活动链接')),
                ('image', models.ImageField(verbose_name='活动图片', upload_to='banner')),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
            ],
            options={
                'verbose_name': '主页促销活动',
                'verbose_name_plural': '主页促销活动',
                'db_table': 'df_index_promotion',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='type',
            field=models.ForeignKey(verbose_name='图书种类', to='goods.BooksType'),
        ),
    ]
