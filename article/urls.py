from django.urls import path
from article.views import detail_article

urlpatterns = [
    path("detail/<int:pk>",detail_article,name="detail")
]