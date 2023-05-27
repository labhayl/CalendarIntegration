from django.contrib import admin
from django.urls import path
from ConvinTest2.views import GoogleCalendarInitView, GoogleCalendarRedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='calendar_init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(),name='calendar_redirect'),
]
