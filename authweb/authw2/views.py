from django.shortcuts import render

# Create your views here.



from django.shortcuts import redirect
from django.contrib.auth import login
from social_django.utils import load_strategy
from social_core.backends.google import GoogleOAuth2
from django.shortcuts import redirect
from django.conf import settings
from urllib.parse import urlencode




def second_google_login(request):
    strategy = load_strategy(request)
    backend = GoogleOAuth2(strategy)
    return redirect(backend.auth_url())
















def google_login(request):
    base_url = "https://accounts.google.com/o/oauth2/auth"
    params = {
        "client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        "redirect_uri": request.build_absolute_uri('/auth/callback/'),
        "response_type": "code",
        "scope": " ".join(settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE),
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = f"{base_url}?{urlencode(params)}"
    return redirect(auth_url)

























