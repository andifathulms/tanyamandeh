from django.urls import path

from .views import Dugout

app_name = 'dugout'

urlpatterns = [
	path('', Dugout.as_view(), name='dugout-home'),
]
