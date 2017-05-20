from django.db import models
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model) :
#    title = models.CharField(max_length = 100)  #博客题目
    title = models.CharField(verbose_name='标题', max_length=150, blank=False, null=False)  #博客题目

    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
#    content = models.TextField(blank = True, null = True)  #博客文章正文
#    content = RichTextField(blank=True,null=True,verbose_name="内容") 
 # 使用ckeditor中的RichTextField
#    content = HTMLField(blank = True, null = True)  #博客文章正文
    content = RichTextUploadingField(blank=True,null=True,verbose_name="内容") 


    #def __unicode__(self) :
    #    return self.title
            
 #获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']
        
