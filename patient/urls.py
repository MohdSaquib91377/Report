

from django.urls import path
from patient import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
]
