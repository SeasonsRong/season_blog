from django.contrib import admin

from article.models import Article

import sys;

reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)


    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-all.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )