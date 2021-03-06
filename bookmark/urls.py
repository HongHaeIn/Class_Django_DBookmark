from django.urls import path

from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView

app_name = 'bookmark'

urlpatterns=[
    path('list/', BookmarkListView.as_view(), name='list'),#book.mark:list
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]