from django.urls import path

from .views import(
    Login,
    ListCreateTodo, 
    RetrieveUpdateDestoryTodo
)

urlpatterns = [
    path('login/', Login.as_view(), name= 'login'),

    path('list-create-todo/', ListCreateTodo.as_view(), name='list-create-todo'),
    path('retrieve-update-destory-todo/<int:pk>/', RetrieveUpdateDestoryTodo.as_view(), name='retrieve-update-destory-todo'),

    
]