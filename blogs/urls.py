from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.PostList.as_view(), name='PostList'),
    path("detail/v1/<int:pk>/", views.PostDetail.as_view(), name='PostDetail'),
]