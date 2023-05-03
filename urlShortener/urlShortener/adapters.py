from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from django.urls import reverse

from users.views import signup_view


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def get_signup_redirect_url(self, request):
        return reverse(signup_view)
