from django.urls import path

from . import views

urlpatterns = [
    path("<pk>/aulas", views.listar_aulas, name='cursos.listar.aulas'),
    path('listar/', views.listar_cursos, name='cursos.listar.tudo'),
    path("novo/", views.NovoCursoView.as_view(), name="cursos.novo"),
    path("alterar/<pk>", views.AlterarCursoView.as_view(), name="cursos.alterar"),
    path('', views.pagina_inicial, name='cursos.inicio'),
    path('like/<pk>', views.like_curso, name="cursos.like.curso")
]
