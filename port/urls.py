from port import views
from django.urls import path,include
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('services/', views.service_view, name='service'),
    path('skills/', views.skills_view, name='skills'),
    path('education/', views.education_view, name='education'),
    path('contact/', views.contact_view, name='contact'),
    path('resume/', views.resume_view, name='resume'),

]
