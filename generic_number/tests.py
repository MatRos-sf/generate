from django.test import TestCase, SimpleTestCase, Client
from http import HTTPStatus
from django.urls import reverse, resolve
from .views import random_number, generic_password, toss_a_coin, dice, random_list
import json
from .forms import RangeForms

class TestUrl(SimpleTestCase):
    def test_random_number_url_is_resolved(self):
        url = reverse('random')
        self.assertEqual(resolve(url).func, random_number)
    def test_toss_a_coin_url_is_resolved(self):
        url = reverse('toss_a_coin')
        self.assertEqual(resolve(url).func, toss_a_coin)
    def test_random_list_url_is_resolved(self):
        url = reverse('random_list')
        self.assertEqual(resolve(url).func, random_list)
    def test_random_dice_url_is_resolved(self):
        url = reverse('random_dice')
        self.assertEqual(resolve(url).func, dice)
    def test_generic_password_url_is_resolved(self):
        url = reverse('generic_password')
        self.assertEqual(resolve(url).func, generic_password)


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_toss_a_coin_page(self):

        response = self.client.get(reverse('toss_a_coin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic_number/toss_a_coin.html')

    def test_random_list_page(self):

        response = self.client.get(reverse('random_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic_number/generic_list.html')

    def test_home_page(self):

        response = self.client.get(reverse('random_dice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'generic_number/generic_dice.html')

class TestForms(SimpleTestCase):
    def test_random_number_form(self):
        form = RangeForms(data={"a": 1,
                                "b": 10,
                                "amount": 2})
        self.assertTrue(form.is_valid())

    def test_random_number_form_valid(self):
        form = RangeForms(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_random_number_form_valid_amount(self):
        form = RangeForms(data={"a": 1,
                                "b": 10,
                                "amount": 101})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)





