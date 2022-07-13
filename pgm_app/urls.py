from django.urls import path
from . import views
app_name = 'pgm_app'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('project/<slug:slug>/',views.ProjectDetailView.as_view(), name='project'),
]