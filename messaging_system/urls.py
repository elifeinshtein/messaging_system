from django.urls import path
from .views import MessageView, UnreadMessageView

urlpatterns = [
    path('messages/', MessageView.as_view(), name='message'),
    path('messages/unread/', UnreadMessageView.as_view(), name='unread-messages'),
]