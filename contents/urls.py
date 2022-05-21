from django.urls import path
from . import views

urlpatterns = [
    path('add_notes_api/', views.AddNotesApi.as_view()),
    path('get_notes_api/', views.GetNotesApi.as_view()),
]