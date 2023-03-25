from django.contrib import admin
from django.urls import path
from . import views
from pages.views import call

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('contact/', CallView.as_view(), name='call'),
    path('contact/', views.call, name='call'),
    path('about/',views.about,name='about'),
]
