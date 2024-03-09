from django.urls import path
from .views import (
    SubjectListView, TicketCreateAPIView, TicketListView
)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/create/', TicketCreateAPIView.as_view(), name='create_ticket'),
]
