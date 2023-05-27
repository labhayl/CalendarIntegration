from django.shortcuts import redirect
from django.http import JsonResponse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.views import View

class GoogleCalendarInitView(View):
    def get(self, request):
        flow = InstalledAppFlow.from_client_secrets_file(
            'Path to your secret_key.json file',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri='https://3518-49-206-128-205.ngrok-free.app/rest/v1/calendar/redirect/'
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent',
        )
        request.session['oauth_state'] = state
        return redirect(authorization_url)


class GoogleCalendarRedirectView(View):
    def get(self, request):
        state = request.session.get('oauth_state')
        flow = InstalledAppFlow.from_client_secrets_file(
            'Path to your secret_key.json file',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            state=state
        )
        flow.fetch_token(authorization_response=request.build_absolute_uri())
        credentials = flow.credentials

        service = build('calendar', 'v3', credentials=credentials)
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        return JsonResponse({'events': events})