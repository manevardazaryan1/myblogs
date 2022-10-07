from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('register/', views.register_request, name = 'register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name= 'logout'),
    path('blogs', views.blogs, name= 'blogs'),
    path('add_post', views.add_post, name= 'add_post'),
    path('blogs/<int:pk>', views.blogDetailView, name='blog_detail'),
    path('blogs/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('blogs/<int:pk>/share', views.share_post, name='share_post'),
    path('<int:pk>', views.postDetailView, name='post_detail'),
    path('search', views.search, name='search'),
]

