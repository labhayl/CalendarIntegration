# CalendarIntegration

## Description
CalendarIntegration is a Django-based web application that integrates with Google Calendar to perform certain tasks.

## Setup Instructions

### Prerequisites
- Python>=3.7
- Django>=3.2
- Google Calendar API credentials

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/labhayl/CalendarIntegration
   ```
   
2. Set up Google Calendar API credentials:
   - Go to the [Google Developers Console](https://console.developers.google.com)
   - Create a new project or select an existing one.
   - Enable the Google Calendar API for the project.
   - Create OAuth 2.0 credentials (client ID and client secret) for the project.
   - Download the JSON file containing the credentials.
   - Rename the JSON file to `secret_key.json` and place it in the project's root directory.

4. Configure Django settings:
   - Open the `ConvinTest/settings.py` file.
   - Update the `SECRET_KEY` with your own Django secret key.
   - Add `localhost` or your domain(s) to the `ALLOWED_HOSTS` list. (I used NGROK for allowing external access for testing and integration purposes.)

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the application:
   - Open a web browser and go to `http://localhost:8000/`.

## Usage

1. On the homepage, click on "Sign in with Google" to authorize access to your Google Calendar.
2. After successful authorization, you can perform various calendar-related tasks.
