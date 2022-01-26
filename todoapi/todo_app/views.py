from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo_app.models import Task
from todo_app.serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def task_create(request):
    """ Create task """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT'])
def task_detail(request, pk):
    """ Get task infor or update existing task """
    try: 
        task = Task.objects.get(pk=pk)
    except:
        return Reponse("Error: Task not found", status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    name = task.name
    task.delete()
    return Response("Task: {} successfully deleted".format(name))

