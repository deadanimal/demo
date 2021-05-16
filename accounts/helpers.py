import dateparser
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
import pkce
from decouple import config

from fusionauth.fusionauth_client import FusionAuthClient

FUSION_AUTH_BASE_URL=config("FUSION_AUTH_BASE_URL")
FUSION_AUTH_APP_ID=config("FUSION_AUTH_APP_ID")
FUSION_AUTH_API_KEY=config("FUSION_AUTH_API_KEY")
FUSION_AUTH_CLIENT_ID=config("FUSION_AUTH_CLIENT_ID")
FUSION_AUTH_CLIENT_SECRET=config("FUSION_AUTH_CLIENT_SECRET")

def get_or_create_user(username, request):
    user = User.objects.filter(username=username).first()
    if not user:
        user = User(username=username)
        user.save()
    return user


def get_login_url(request):
    if request.session.has_key('pkce_verifier') is False or request.session.has_key('code_challenge') is False:
        code_verifier = pkce.generate_code_verifier(length=128)
        code_challenge = pkce.get_code_challenge(code_verifier)
        request.session['pkce_verifier'] = code_verifier
        request.session['code_challenge'] = code_challenge
    redirect_url = request.build_absolute_uri(reverse("accounts"))
    login_url = f"{FUSION_AUTH_BASE_URL}/oauth2/authorize?client_id={FUSION_AUTH_APP_ID}&redirect_uri={redirect_url}&response_type=code&code_challenge={request.session['code_challenge']}&code_challenge_method=S256"
    login_url = login_url.format(
        FUSION_AUTH_BASE_URL, FUSION_AUTH_APP_ID,
    )
    return login_url


def is_user_login_ok(request):

    client = FusionAuthClient(
        FUSION_AUTH_API_KEY, FUSION_AUTH_BASE_URL
    )
    code = request.GET.get("code")
    if not code:
        print("no code")
        return False
    try:
        redirect_url = request.build_absolute_uri(reverse("accounts"))
        r = client.exchange_o_auth_code_for_access_token_using_pkce(
            code,
            redirect_url,
            request.session['pkce_verifier'],
            FUSION_AUTH_CLIENT_ID,
            FUSION_AUTH_CLIENT_SECRET,
        )

        if r.was_successful():
            print("all good")
            access_token = r.success_response["access_token"]
            user_id = r.success_response["userId"]
            get_or_create_user(user_id, request)
            return user_id
        else:
            print("could not exchange code for token")
            print(r.error_response)
            return False
    except Exception as e:
        print("Something went wrong")
        print(e)


def authenticated_user(request):

    if is_user_login_ok(request) is False:
        login_url = get_login_url(request)
        print(login_url)
        return login_url
    else:
        print('auth')
    # try:
    #     client = FusionAuthClient(
    #         FUSION_AUTH_API_KEY, FUSION_AUTH_BASE_URL
    #     )
    #     r = client.retrieve_user(request.user.username)

    #     if r.was_successful():
    #         user = r.success_response            
    #         return user
    #     else:
    #         print(r.error_response)
    # except Exception as e:
    #     print("couldn't get user")
    #     print(e)    
