from django.db import models
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from store.config.settings import S

class NewsBlog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_blog', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'News Blog'
        verbose_name_plural = 'News Blog'