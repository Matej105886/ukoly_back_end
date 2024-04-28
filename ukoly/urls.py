from ukoly import views
"""
URL configuration for ukoly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goals/', views.goals),
    path('tasks/<int:goal_id>/add_task/', views.add_task_to_goal),
    path('tasks/<int:task_id>/delete_task/', views.delete_task),
    path('goals/<int:goal_id>/delete_goal/', views.delete_goal),
    path('goals/<int:goal_id>/edit_goal/', views.edit_goal),
    path('goals/<int:goal_id>/get_goal/', views.get_goal),
    path('tasks/<int:task_id>/edit_task/', views.edit_task),
    path('tasks/<int:task_id>/get_task/', views.get_task),
]
