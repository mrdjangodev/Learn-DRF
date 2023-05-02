from django.test import TestCase
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        Todo.objects.create(title='first_todo', body='a body here', is_done=True)
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first_todo')
        
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'a body here')
    
    def test_is_done(self):
        todo = Todo.objects.get(id=1)
        excepted_object_is_done = todo.is_done
        self.assertEqual(excepted_object_is_done, True)