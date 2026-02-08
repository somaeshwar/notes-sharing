from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_notes, name='upload'),
    path('notes/', views.notes_list, name='notes_list'),
    path('download/<int:note_id>/', views.download_note, name='download'),

]
