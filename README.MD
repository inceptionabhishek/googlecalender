# Google Calendar Integration with Django REST API

This project provides integration with Google Calendar using Django REST API. It allows users to authenticate with their Google accounts, authorize access to their calendars, and retrieve a list of events from their primary calendar.

APIs

1. /rest/v1/calendar/init/ - Google Calendar Init View
   This API initiates the OAuth 2.0 flow with Google. When accessed, it prompts the user to authenticate with their Google account and authorize access to their calendar.

Method: GET

Example Request:
GET /rest/v1/calendar/init/
Example Response:
The user will be redirected to the Google login page.

2. /rest/v1/calendar/redirect/ - Google Calendar Redirect View
   This API handles the redirect request sent by Google with the authorization code. It exchanges the authorization code for an access token, and then retrieves a list of events from the user's primary calendar.

Method: GET

Example Request:
GET /rest/v1/calendar/redirect/?code=xxxxxxxx
Example Response:
A list of events from the user's primary calendar will be displayed in the browser.



https://github.com/inceptionabhishek/googlecalender/assets/65409282/4662b451-f0a1-44b7-86fc-a51007186e8f



