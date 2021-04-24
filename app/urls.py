from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.create,name='create'),
    path('details',views.details,name='details'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete),
]