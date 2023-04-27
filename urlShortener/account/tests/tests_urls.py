from django.test import SimpleTestCase
from django.urls import reverse, resolve

from account.views import *


class TestUrls(SimpleTestCase):

    data_dict = {"url_username": "procdima4845"}

    def test_list_url_is_resolved(self):
        url = reverse('update-password', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, update_password_view)

    def test_disable_tfa_is_resolved(self):
        url = reverse('disable', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, disable_tfa_view)

    def test_delete_codes_is_resolved(self):
        url = reverse('delete-codes', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, delete_codes_view)

    def test_generate_codes_is_resolved(self):
        url = reverse('generate-codes', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, generate_backup_codes_view)

    def test_save_codes_is_resolved(self):
        url = reverse('save-codes', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, save_code_view)

    def test_copy_codes_is_resolved(self):
        url = reverse('copy-codes', kwargs=self.data_dict)
        self.assertEquals(resolve(url).func, copy_codes_to_clipboard_view)