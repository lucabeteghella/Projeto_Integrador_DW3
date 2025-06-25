from django.urls import path
from core.views import (
    login, logout, home,
    listar_contatos, adicionar_contato,
    editar_contato, excluir_contato
)

urlpatterns = [

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('', home, name='home'),
    path('index/', home, name='index'),

    path('contatos/', listar_contatos, name='listar_contatos'),
    path('contatos/novo/', adicionar_contato, name='adicionar_contato'),
    path('contatos/<int:id>/editar/', editar_contato, name='editar_contato'),
    path('contatos/<int:id>/excluir/', excluir_contato, name='excluir_contato'),
    
]
