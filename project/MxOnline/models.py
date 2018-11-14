from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50,default="",primary_key=True)
    name = models.CharField(max_length=20,null=True,blank=True,default="",verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name=u"联系地址")
    message = models.CharField(max_length=500,verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name

    @classmethod
    def createuser(cls, object_id, name, email, address, message):
        c = cls(object_id=object_id, name=name, email=email, address=address,
                message=message)
        return c