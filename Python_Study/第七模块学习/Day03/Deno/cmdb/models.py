from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class UserGroup(models.Model):
    name = models.CharField(max_length=64)

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=12)
    email = models.EmailField()
    user_type = models.ForeignKey(to="UserType",to_field="id",on_delete=models.CASCADE,null=True)
    u2g = models.ManyToManyField(UserGroup)