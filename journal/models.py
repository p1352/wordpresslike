from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField('Titre',max_length=200)
    text = models.TextField('Texte')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_date = models.DateTimeField('Date de création',default=timezone.now)
    published_date=models.DateTimeField('Date de publication',blank=True, null=True)
    upload = models.ImageField('Image', null=True, upload_to="gallery")

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title





 