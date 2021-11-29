from django.urls import path

from .views import Dugout, SessionsView, SessionsDeleteView, AnalyticsView

app_name = 'dugout'

urlpatterns = [
	path('', Dugout.as_view(), name='dugout-home'),
	path('sessions', SessionsView.as_view(), name='dugout-sessions'),
	path('sessions/<int:pk>/delete/', SessionsDeleteView.as_view(), name='sessions-delete'),
	path('analytics', AnalyticsView.as_view(), name='dugout-analytics'),
]
