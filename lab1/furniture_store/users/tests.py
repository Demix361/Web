from django.test import TestCase
from django.test import Client, TestCase
from .models import Profile
from unittest.mock import patch

"""
class ProfileTest(TestCase):

	@patch('users.models.Order')
	def test_start(self, MockOrder):
		MockOrder.get.return_value = users.models.Order()
		mock_order = MockOrder()
"""