from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'posts'

    name = models.CharField('Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous')
    body = models.CharField('Body', blank=False, null=False, max_length=14, db_index=True)
    image = models.ImageField('Image', blank=True, null=False, db_index=True)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created DateTime', blank=True, auto_now_add=True)
  

    def __str__(self):
        return f'{self.name}, {self.body}'