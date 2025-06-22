from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_email, user_field
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = user_email(sociallogin.user)
        if not sociallogin.is_existing:
            try:
                user = get_user_model().objects.get(email=email)
                sociallogin.connect(request, user)
            except get_user_model().DoesNotExist:
                pass
