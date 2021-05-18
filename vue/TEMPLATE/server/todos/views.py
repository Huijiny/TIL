from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 순서가 중요한 친구들이다.
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
# 검사를 하는 순서가 이 데코레이터가 정해져있다.
# 인증여부와 관계없이 문법이나 등등 유효한 토큰인지 먼저 확인해야한다.
@authentication_classes([JSONWebTokenAuthentication])
# 그 다음에 인증을 한다.
@permission_classes([IsAuthenticated])
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        # 조회를 할 때 그 유저가 쓴 투두만 보겠다.
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 저장할 때도 그냥 저장하면 안되고, 안에다가 유저를 넣어줘야한다.
            # 그냥 장고에서는 추가적으로 데이터를 넣을 때 commit=false를 넣고 아래에서 넣어줬는데,
            # drf에서는 이 안에서 나열하는 방법을 가지고 갔다.
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
# 검사를 하는 순서가 이 데코레이터가 정해져있다.
# 인증여부와 관계없이 문법이나 등등 유효한 토큰인지 먼저 확인해야한다.
@authentication_classes([JSONWebTokenAuthentication])
# 그 다음에 인증을 한다.
@permission_classes([IsAuthenticated])
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)

    if not request.user.todos.filter(pk=todo_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({ 'id': todo_pk })
