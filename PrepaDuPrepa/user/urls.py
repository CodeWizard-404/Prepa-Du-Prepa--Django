from django.urls import path,include
from user import views

urlpatterns = [
    path('',views.index,name='index'),
    path('course_index', views.course_index, name='course_index'),
    path('course_show/<int:course_id>/', views.course_show, name='course_show'),
    path('download_pdf/<int:content_id>/', views.download_pdf, name='download_pdf'),
    path('profile',views.profile,name='profile'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('support',views.support,name='support'),
    path('newcourse',views.newcourse,name='newcourse'),
    path('authentication/', include('authentication.urls'))
]