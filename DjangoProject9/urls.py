"""
URL configuration for DjangoProject9 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from goldenqa import views

urlpatterns = [
    path('', views.home, name='home'),  # This defines the homepage
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),  # if you use a custom login view
    path('logout/', views.logout_view, name='logout'),  # if you use a custom logout view
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('like-answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]

