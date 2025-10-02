from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

class NoteViewTest(TestCase):
    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_contains_note(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Test Note')
