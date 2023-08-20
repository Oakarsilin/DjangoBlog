from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import todoListCreate, todoListUpdate, todoListView, todoListDelete
from django.contrib.auth.models import User

# Create your tests here.
class TestUrls (SimpleTestCase):
    
    def test_url_todoListCreate (self):
        createview_url = reverse ('todolist.new')
        self.assertEquals (resolve(createview_url).func, todoListCreate, 'Todolist CreateView testing failed!!')
        self.assertEquals (resolve(createview_url).route, 'todolist/new/', 'Todolist route testing failed!!')

    def test_url_todoListView (self):
        listview_url = reverse ('todolist.all')
        self.assertEquals (resolve(listview_url).func.view_class, todoListView, 'Todolist ListView testing failed!!')
        self.assertEquals (resolve(listview_url).route, 'todolist/allitem/', 'Todolist route testing failed!!')

    def test_url_todoListUpdate (self):
        pk = 1
        updateview_url = reverse ('todolist.update', args=[pk])
        self.assertEquals (resolve(updateview_url).func.view_class, todoListUpdate, 'Todolist UpdateView testing failed!!')
        self.assertEquals (resolve(updateview_url).route, 'todolist/item/update/<int:pk>/', 'Todolist route testing failed!!')

    def test_url_todoListDelete (self):
        pk = 1
        deleteview_url = reverse ('todolist.delete', args=[pk])
        self.assertEquals (resolve(deleteview_url).func.view_class, todoListDelete, 'Todolist DeleteView testing failed!!')
        self.assertEquals (resolve(deleteview_url).route, 'todolist/item/delete/<int:pk>/', 'Todolist route testing failed!!')

class TestViews(TestCase):

    def setUp (self):
        self.client = Client()
        User.objects.create_user (username='oakarsilin', password='12345678')

    def test_listview_get (self):
        self.client.login(username='oakarsilin', password='12345678')
        response = self.client.get(reverse('todolist.all'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'userhomepage.html')