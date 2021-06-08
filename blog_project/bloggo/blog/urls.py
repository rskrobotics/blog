from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<str:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<str:pk>/edit', views.PostUpdateView.as_view(), name='post_edit'),
    path('about', views.AboutView.as_view(), name='about'),
    path('drafts', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<str:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<str:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comments/<str:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comments/<str:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<str:pk>/publish', views.post_publish, name='post_publish'),
]
