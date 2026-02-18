from django.test import TestCase
from django.urls import reverse


# Create your tests here.
from .utils import add 
class AddTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

class NotesTestCase(TestCase):
    def test_notes_can_be_added(self):
        res = self.client.post(reverse('notes:add'), {
            "title":"hello",
            "description":"notes from test"
        })
        self.assertEqual(res.status_code,302)
        reshome = self.client.get(res.url)
        self.assertContains(reshome,"hello")