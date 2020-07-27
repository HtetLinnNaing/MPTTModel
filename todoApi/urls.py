from django.urls import path,include
from todoApi.views import todo_list, todo_list_change_and_delete, TodoListAndCreate, TodoDetailChangeAndDelete, \
    TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_list_change_and_delete),
    path('generics/', TodoListAndCreate.as_view()),
    path('generics/<int:pk>/', TodoDetailChangeAndDelete.as_view()),
    path(r'viewset/', include(router.urls)),
]
