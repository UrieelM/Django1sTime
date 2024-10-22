from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username="testuser", password="12345")

    def test_create_note(self):
        """Test para la creación correcta de una nueva nota."""
        note = Note.objects.create(user=self.user, title_note="Comprar leche", content_note="Recordar comprar leche")
        self.assertEqual(note.title_note, "Comprar leche")
        self.assertEqual(note.content_note, "Recordar comprar leche")
        self.assertEqual(note.user, self.user)  # Verificar que la nota pertenece al usuario correcto

    def test_update_note(self):
        """Test para actualizar una nota existente."""
        note = Note.objects.create(user=self.user, title_note="Comprar leche", content_note="Recordar comprar leche")
        note.title_note = "Comprar leche y huevos"  # Cambiar el título
        note.content_note = "Recordar comprar leche y huevos"  # Cambiar el contenido
        note.save()

        updated_note = Note.objects.get(id=note.id)
        self.assertEqual(updated_note.title_note, "Comprar leche y huevos")
        self.assertEqual(updated_note.content_note, "Recordar comprar leche y huevos")

    def test_view_note_details(self):
        """Test para ver los detalles de una nota."""
        note = Note.objects.create(user=self.user, title_note="Estudiar", content_note="Estudiar para el examen")
        self.assertEqual(note.user, self.user)  # Verificar que la nota pertenece al usuario correcto
        self.assertEqual(note.title_note, "Estudiar")
        self.assertEqual(note.content_note, "Estudiar para el examen")

    def test_delete_note(self):
        """Test para eliminar una nota."""
        note = Note.objects.create(user=self.user, title_note="Comprar leche", content_note="Recordar comprar leche")
        note_id = note.id
        note.delete()  # Eliminar la nota

        with self.assertRaises(Note.DoesNotExist):
            Note.objects.get(id=note_id)  # Verificar que la nota ya no existe

    def test_load_note_list(self):
        """Test para cargar la lista de notas."""
        Note.objects.create(user=self.user, title_note="Comprar leche", content_note="Recordar comprar leche")
        Note.objects.create(user=self.user, title_note="Estudiar", content_note="Estudiar para el examen")
        
        notes = Note.objects.filter(user=self.user)
        self.assertEqual(notes.count(), 2)  # Verificar que hay dos notas creadas

        # Verificar que las notas correctas están en la lista
        titles = [note.title_note for note in notes]
        self.assertIn("Comprar leche", titles)
        self.assertIn("Estudiar", titles)