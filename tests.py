from django.test import TestCase
from django.contrib.auth.models import User
from .models import ServiceRequest

class ServiceRequestModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.service_request = ServiceRequest.objects.create(
            customer=self.user, type="Gas Leak", description="Leaking pipe in kitchen."
        )

    def test_service_request_creation(self):
        self.assertEqual(self.service_request.type, "Gas Leak")
        self.assertEqual(self.service_request.customer.username, "testuser")
