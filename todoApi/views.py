from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from todoApi.models import todo
from todoApi.serializer import TodoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todoList = todo.objects.all()
        serializer = TodoSerializer(todoList, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_list_change_and_delete(request, pk):
    try:
        Todo = todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = TodoSerializer(Todo)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TodoSerializer(Todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        Todo.delete()
        return Response(
            {
                "result": "failed",
                "code": status.HTTP_204_NO_CONTENT,
                "message": "Error Message"
            }, status=status.HTTP_204_NO_CONTENT)


class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = todo.objects.all()
    serializer_class = TodoSerializer
