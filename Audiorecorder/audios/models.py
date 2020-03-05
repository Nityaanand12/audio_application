from django.db import models

# Create your models here.
class AudioRecordFile(models.Model):
    user_name      = models.CharField(max_length=30,blank=False)
    photo          = models.ImageField()
    voice_record   = models.FileField()

    def __str__(self):
    	return "{}".format(user_name)
