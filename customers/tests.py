from django.urls import include, path, reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import (
    APIClient,
    APIRequestFactory,
    APITestCase,
    RequestsClient,
    URLPatternsTestCase,
)

from customers.models import Customer

from colorama import init, Fore

init(autoreset=True)

print(Fore.GREEN + "1) Test that the API is up and running")
client = RequestsClient()
response = client.get("http://127.0.0.1:8000/api/customers/")
assert response.status_code == status.HTTP_200_OK

print(Fore.GREEN + "2) Test POST and GET Customer API methods")


class CustomerPostGet(APITestCase):
    def test_create_customer(self):

        print(
            Fore.GREEN
            + "3) Assert that we can create a new customer using a POST request"
        )

        url = "http://127.0.0.1:8000/api/customers/"
        data = {
            "first_name": "Steven",
            "last_name": "Jones",
            "email": "sjones@yahoo.com",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, "Steven")
        self.assertEqual(Customer.objects.get().last_name, "Jones")
        self.assertEqual(Customer.objects.get().email, "sjones@yahoo.com")

        print(
            Fore.GREEN
            + "4) Assert that we can retrieve the newly created customer using a GET request"
        )

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().first_name, "Steven")

        print(
            Fore.GREEN
            + "5) Assert that we can get a Customer by ID using a GET request"
        )

        url = "http://127.0.0.1:8000/api/customers/1/"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().last_name, "Jones")

        print(
            Fore.GREEN
            + "6) Assert that we can edit a Customer by ID using a PUT request"
        )

        url = "http://127.0.0.1:8000/api/customers/1/"
        data = {"first_name": "Stevie", "last_name": "J", "email": "sjones@yahoo.com"}

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().last_name, "J")


# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
# Make sure we can create a customer using the factory method
request = factory.post("/api/customers/", {"last_name": "Dianne"})
assert response.status_code == status.HTTP_200_OK
request = factory.get("/api/customers/", {"last_name": "Dianne"})
