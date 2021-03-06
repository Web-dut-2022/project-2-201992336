# Generated by Django 3.2.13 on 2022-04-20 10:26

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='auctions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='商品名称')),
                ('description', models.CharField(max_length=64, verbose_name='描述')),
                ('startbid', models.CharField(max_length=64, verbose_name='起始价格')),
                ('category', models.CharField(max_length=64, verbose_name='类别')),
                ('image', models.CharField(max_length=256, verbose_name='图片url')),
                ('createTime', models.CharField(max_length=128, verbose_name='创建时间')),
                ('createby', models.CharField(max_length=128, verbose_name='创建者')),
                ('status', models.CharField(max_length=128, verbose_name='商品状态')),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='商品名称')),
                ('nowbid', models.CharField(max_length=64, verbose_name='现在价格')),
                ('createby', models.CharField(max_length=64, verbose_name='竞拍发起者')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='商品名称')),
                ('name', models.CharField(max_length=128, verbose_name='用户')),
                ('content', models.CharField(max_length=512, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='wathclist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, verbose_name='用户名称')),
                ('title', models.CharField(max_length=64, verbose_name='商品名称')),
                ('description', models.CharField(max_length=64, verbose_name='描述')),
                ('startbid', models.CharField(max_length=64, verbose_name='起始价格')),
                ('category', models.CharField(max_length=64, verbose_name='类别')),
                ('image', models.CharField(max_length=256, verbose_name='图片url')),
                ('createTime', models.CharField(max_length=128, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
