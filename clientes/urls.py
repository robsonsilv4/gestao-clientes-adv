from django.urls import path
from .views import pessoas_list, pessoas_new, pessoas_update, pessoas_delete
from .views import PessoaList, PessoaDetail, PessoCreate

urlpatterns = [
    path('list/', pessoas_list, name='pessoa_list'),
    path('new/', pessoas_new, name='pessoa_new'),
    path('update/<int:id>/', pessoas_update, name='pessoa_update'),
    path('delete/<int:id>/', pessoas_delete, name='pessoa_delete'),
    path('pessoa_list/', PessoaList.as_view(), name='pessoacbv_list'),
    path('pessoa_detail/<int:pk>/', PessoaDetail.as_view(), name='pessoacbv_detail'),
    path('pessoa_create/', PessoCreate.as_view(), name='pessoacbv_create')
]
