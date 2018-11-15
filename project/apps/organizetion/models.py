from django.db import models
from datetime import datetime


# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name="城市")
    desc = models.TextField(max_length=200, verbose_name="城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="封面")
    address = models.CharField(max_length=100, verbose_name="机构地址")
    city = models.ForeignKey(CityDict, verbose_name="所在城市",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name="所属机构",on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="工作单位")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(verbose_name="课程点击数", default=0)
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
