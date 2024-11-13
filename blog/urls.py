from django.urls import path
from . import views
from .views import CategoriaList, PostList, PostsByCategoria

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="Categoria"),
    path('api/categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('api/posts/', PostList.as_view(), name='post-list'),
    path('api/posts/categoria/<int:categoria_id>/', PostsByCategoria.as_view(), name='posts-by-categoria'),
]