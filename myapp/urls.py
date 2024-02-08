from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('course/',views.courses,name='course'),
    path('cou/',views.CourseCreateView.as_view(),name='create_course')
]
