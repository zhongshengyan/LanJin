from app01 import views
from django.conf.urls import url

urlpatterns = [
    url(r'',views.hello,name='hello')
]