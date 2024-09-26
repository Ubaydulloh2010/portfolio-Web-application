from django.urls import path
from work.views import home_page,not_found

urlpatterns = [
    path('',home_page,name="home_page"),
    path('not_found/',not_found,name="not_found")
]