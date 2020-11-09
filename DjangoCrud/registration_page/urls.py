from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showallemployees, name="showallemployees"),
    path('Insert', views.Insertemp, name="Insertemp"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('edit/update/<int:id>', views.update, name="update"),
]
