from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Crear una nota asociada a ese usuario
        Note.objects.create(user=self.user, title_note="Comprar leche", content_note="Recordar comprar leche")
        Note.objects.create(user=self.user, title_note="Estudiar", content_note="Estudiar para el examen")

    def test_load_note_list(self):
        """Test para cargar la lista de notas"""
        notes = Note.objects.filter(user=self.user)
        self.assertEqual(notes.count(), 2)  # Verificar que hay dos notas creadas

        # Verificar detalles de la primera nota
        first_note = notes.first()
        self.assertEqual(first_note.title_note, "Comprar leche")
        self.assertEqual(first_note.content_note, "Recordar comprar leche")