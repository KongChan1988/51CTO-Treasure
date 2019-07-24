from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=64,db_index=True)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    host_name = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
    prrt = models.IntegerField()
    base = models.ForeignKey("Business",to_field="id",on_delete=models.CASCADE)

class Application(models.Model):
    name = models.CharField(max_length=32)
#     r = models.ManyToManyField("Host")
#
# class APP_m2m_Host(models.ManyToManyField):
#     Hobj = models.ForeignKey("Host",to_field="nid",on_delete=models.CASCADE)
#     Aobj = models.ForeignKey("Application",to_field="id",on_delete=models.CASCADE)
