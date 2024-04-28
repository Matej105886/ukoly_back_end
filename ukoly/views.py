from .models import Goal
from .models import Task
from rest_framework.decorators import api_view
from .serializers import GoalSerializer
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
@api_view(["GET", "POST"])
def goals(request):
    if request.method == "GET":
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            saved_goal = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(["POST"])
def add_task_to_goal(request, goal_id):
    try:
        goal = Goal.objects.get(id=goal_id)
    except Goal.DoesNotExist:
        return Response({"error":"goal not found"}, status.HTTP_400_BAD_REQUEST)
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        saved_task = serializer.save(goal=goal)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["DELETE"])
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def edit_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    serializer = GoalSerializer(goal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_goal(request, goal_id):
    goal = get_object_or_404(Goal, pk=goal_id)
    serializer = GoalSerializer(goal, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(["PUT"])
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_task(request, task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)