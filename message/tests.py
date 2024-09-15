from django.test import SimpleTestCase
from django.urls import reverse
class MessagePageTest(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("//")
        self.assertEqual(response.status_code,200)

    def test_url_availble_by_name(self):
        response = self.client.get(reverse('message'))
        self.assertEqual(response.status_code,200)


    def test_template_name(self)    :
        response = self.client.get(reverse('message'))
        self.assertTemplateUsed(response , 'home.html')

    def test_template_content(self):
        response = self.client.get('//')
        self.assertContains(response,'<h1> this is your message </h1>')
        


