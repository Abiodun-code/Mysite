from django.urls import path
from .views import HomeView, AboutView,NewsListView, NewsDetailView, NewsCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('news/', NewsListView.as_view(), name='news'),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='detail'),
    path('create/', NewsCreateView.as_view(), name='create'),
]