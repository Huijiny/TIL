from django.db import models
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # image_thumbnail = ImageSpecField(source='image',
    #                                   processors=[ResizeToFill(200, 200)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    image = ProcessedImageField(upload_to='images/%Y/%m/%d',
                                           processors=[ResizeToFill(500, 500)],
                                           format='JPEG',
                                           options={'quality': 100})