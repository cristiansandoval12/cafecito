from django.urls import include, path
from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel

urlpatterns = [
    path(r'categorias/', CategoriaView.as_view(), name='categoria_list'),
    path(r'categoria/new', CategoriaNew.as_view(), name='categoria_new'),
    path(r'categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path(r'categoria/delete/<int:pk>', CategoriaDel.as_view(), name='categoria_del'),
    
    path(r'subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path(r'subcategoria/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path(r'subcategoria/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path(r'subcategoria/delete/<int:pk>', SubCategoriaDel.as_view(), name='categoria_del'),
]