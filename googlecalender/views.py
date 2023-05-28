from google_auth_oauthlib.flow import Flow
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from googleapiclient.discovery import build

class InitialiseCalenderWelcomeView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to Google Calendar API'})

class GoogleCalendarInitView(APIView):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=['https://www.googleapis.com/auth/calendar'],
            redirect_uri=request.build_absolute_uri(reverse('google-calendar-redirect'))
        )
        authorization_url, _ = flow.authorization_url(access_type='offline')

        return HttpResponseRedirect(authorization_url)
class GoogleAuthCallbackView(APIView):
    def get(self, request):
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=['https://www.googleapis.com/auth/calendar'],
            redirect_uri=request.build_absolute_uri(reverse('google-auth-callback'))
        )
        flow.fetch_token(authorization_response=request.build_absolute_uri(), access_type='offline')
        
        # Perform additional actions with the authenticated user
        return HttpResponse('Authentication successful')
    
class GoogleCalendarRedirectView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        # Exchange authorization code for access token
        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=['https://www.googleapis.com/auth/calendar'],
            redirect_uri=request.build_absolute_uri(reverse('google-calendar-redirect'))
        )
        flow.fetch_token(authorization_response=request.build_absolute_uri(), access_type='offline')
        credentials = flow.credentials
        # Create an API client using the access token
        service = build('calendar', 'v3', credentials=credentials)
        # Get list of events
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])

        # Process and display the list of events
        if not events:
            return HttpResponse('No events found.')
        else:
            event_list = []
            for event in events:
                event_list.append(event['summary'])
            return HttpResponse(', '.join(event_list))