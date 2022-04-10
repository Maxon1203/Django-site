from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib.auth import views as authViews
#from django.contrib.auth import views


urlpatterns = [

    #path('exit/', authViews.LogoutView.as_view(), name='exit'),

    path('', views.index, name='index_url'),
    path('tag/', views.index_tag, name='index_tag_url'),

    path('<int:id_post>/', views.post_detail, name='post_detail_url'),

    path('<int:id_post>/add_comment', views.add_comment, name='add_comment_url'),

    path('post_create', views.PostCreate.as_view(), name='post_create_url'),
    path('<int:id_post>/post_update/',
         views.PostUpdate.as_view(), name="post_update_url"),
    path('<int:id_post>/post_delete/',
         views.PostDelete.as_view(), name="post_delete_url"),


    path('tag_create', views.TagCreateView. as_view(), name='tag_create_url'),
    path('tag/<int:tag_id>/tag_update',
         views.TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<int:tag_id>/tag_delete',
         views.TagDelete.as_view(), name='tag_delete_url'),
    path('index_filter_url/<int:tag_id>/',
         views.index_filter, name='index_filter_url'),


    path('account/', view=views.UserUpdateView.as_view(),
         name="profile_detail_url"),
    path('account/update', view=views.UserUpdateView.as_view(),
         name="profile_update_url"),
    path('account/posts', view=views.UserPostsListView.as_view(),
         name="profile_posts_url")
]
