# Generated by Django 2.1.1 on 2018-11-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('object_id', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=100, verbose_name='联系地址')),
                ('message', models.CharField(max_length=500, verbose_name='留言信息')),
            ],
            options={
                'verbose_name': '用户留言信息',
                'verbose_name_plural': '用户留言信息',
            },
        ),
    ]
