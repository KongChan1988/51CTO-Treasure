from django.conf.urls import url
from django.conf.urls import include
from .views import user

urlpatterns = [
    url(r'^base-info.html$', user.base_info),
    url(r'^tag.html$', user.tag),
    url(r'^category.html$', user.category),
    url(r'^article.html$', user.article),
    url(r'^add-article.html$', user.add_article),
    url(r'^edit-article-(\d+).html$', user.edit_article),
]
