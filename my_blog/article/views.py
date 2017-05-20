from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed  #注意加入import语句
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #添加包
import django_comments 
from django.http import HttpResponseRedirect
from django_comments.models import Comment
import traceback  

import logging
logger = logging.getLogger("django") # 为loggers中定义的名称


# Create your views here.
def home(request):
    posts = Article.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 2)#每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
        traceback.print_exc(file=open('D:/tb.txt','w+'))
    except EmptyPage :
    	logger.info("post infor")
        post_list = paginator.paginator(paginator.num_pages)
        traceback.print_exc(file=open('D:/tb.txt','w+'))
    return render(request, 'home.html', {'post_list' : post_list})

    	

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
#        blog_comment=django_comments.models.Comment.objects.get(id=str(id))
#        logger.info(post)
    except Article.DoesNotExist:
       raise Http404
    return render(request, 'post.html', {'post' : post})
    
    	
def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def about_me(request) :
    return render(request, 'aboutme.html')
    
    
def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
                                            'error' : False})
                                            	
                                            	
def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')
    
class RSSFeed(Feed) :
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content
        
def sub_comment(request):
#    comment_list=django_comments.models.Comment.objects.all()
#    logger.info("comment is:"+comment_list.comment)
    blog_id = request.POST.get('post_id') 
    logger.info("blog id is:"+str(blog_id)) 
    #django_comments表中需要blog_id参数
    comment=request.POST.get('comment_content')                 
    django_comments.models.Comment.objects.create(
        content_type_id=9,                                               #content_type_id=9代表的是博客，8代表tag
        object_pk=blog_id,                                               
        site_id=1,
        user=request.user,                                               #当前登录的用户
        comment=comment,
    )
    return HttpResponseRedirect('/%s' %blog_id)