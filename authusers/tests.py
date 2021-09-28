from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import CustomUser

class UsersTest(APITestCase):
    def setUp(self):
       
        self.testuser = CustomUser.objects.create_user('testuser', 'testing@email.com')
        self.testuser2 = CustomUser.objects.create_user('testuser2', '+254722800911')
        
        self.create_userurl = reverse('registerview')

    def test_create_user(self):
        user1 = {
            'username': 'user1',
            'email': 'user1@email.com'
        }
        user2 = {
            'username': 'user2',
            'phone_number': '+255722000111'
        }

        response = self.client.post(self.create_userurl, user1, format='json')
        response2 = self.client.post(self.create_userurl, user2, format='json')
        users = CustomUser.objects.all()
        print('USERS',[(user.username, user.email) for user in users])
        self.assertEqual(CustomUser.objects.count(), 4)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)
        
        print("RESPONSE", response.data)
        self.assertEqual(response.status_code, 201)

        self.assertEqual(response2.status_code, 201)
         
    def test_create_user_with_existing_email(self):
        data = {
            'username': 'testuser3',
            'email': 'testing@email.com'
        }

        response = self.client.post(self.create_userurl, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 2)
    
    def test_create_user_with_invalid_email(self):
        data = {
            'username': 'user4',
            'email': 'testing',

        }
        response = self.client.post(self.create_userurl, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_no_email(self):
        data = {
            'username': 'user5',
            'email': ''
        }
        response = self.client.post(self.create_userurl, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data['email']), 1)
    





