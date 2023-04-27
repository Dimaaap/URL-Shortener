import json

from django.test import TestCase, Client
from django.urls import reverse

from account.models import *


class TestViews(TestCase):

    def test_update_password_view_GET(self):
        client = Client()
        response = client.get(reverse('update-password', kwargs={'url_username': 'procdima4845'}))
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'account/update-password.html')
