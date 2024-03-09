from django.urls import path
from .views import (
    TutorListView
)

urlpatterns = [
    path('users/', TutorListView.as_view(), name='subject-list')
]
