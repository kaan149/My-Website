from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.CharField(max_length=100 ,verbose_name='makale img', default=1)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def get_image_path(self):
        return 'img/' + self.image