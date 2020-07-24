from django.urls import path
from homepage_app import views

app_name = 'homepage_app'

urlpatterns = [
    path('skills/', views.skills_page_view, name ='skills'),
    path('projects/', views.projects_view, name = 'projects'),
]
