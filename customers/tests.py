from django.urls import include, path, reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase, RequestsClient, URLPatternsTestCase

from customers.models import Customer


# 1) Regular tests
print('Test creating a customer')
class CustomerTests(APITestCase):
	def test_create_customer(self):
		"""
		Ensure we can create a new account object
		"""
		url = 'http://127.0.0.1:8000/api/customers/'
		data = {'first_name': 'Jones'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Customer.objects.count(), 1)
		self.assertEqual(Customer.objects.get().first_name, 'Jones')


# 2) Testing using a few different methods
print('Test that the api is up and running')
# Make sure the api is up and running
client = RequestsClient()
response = client.get('http://127.0.0.1:8000/api/customers/')
assert response.status_code == 200



# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()

view = CustomerDetail.as_view()

# Make sure we can create a customer using the factory method
request = factory.post('/api/customers/', {'first_name':'Dianne'})
print('first factory request to post is ', request)



# TODO test views

# TODO test getting a client by id