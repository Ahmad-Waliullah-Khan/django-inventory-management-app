
from django.contrib import admin
from django.urls import path

from inventoryapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>', views.item_detail, name='item_detail'),
    path('admin/', admin.site.urls),
]
