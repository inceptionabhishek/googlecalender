from django.urls import path
from .views import GoogleCalendarInitView, InitialiseCalenderWelcomeView, GoogleAuthCallbackView,GoogleCalendarRedirectView

urlpatterns = [
    path('', InitialiseCalenderWelcomeView.as_view(), name='welcome'),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google-calendar-init'),
    path('rest/v1/calendar/callback/', GoogleAuthCallbackView.as_view(), name='google-auth-callback'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google-calendar-redirect'),
]