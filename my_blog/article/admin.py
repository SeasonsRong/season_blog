from django.contrib import admin

from article.models import Article

import sys;

reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
admin.site.register(Article)