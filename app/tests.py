from rest_framework.test import APITestCase
from rest_framework import status

class APITestCases(APITestCase):
    def test_doctor_list(self):
        response = self.client.get('/doctor/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_doctor_detail(self):
        response = self.client.get('/api/doctor/1/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])

    def test_news_list(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_news_detail(self):
        response = self.client.get('/api/news/1/')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])
