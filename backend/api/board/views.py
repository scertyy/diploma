from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from backend.api.board.models import Board, Task, Comment
from backend.api.board.serializers import BoardSerializer, TaskSerializer, CommentSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['team']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['contributor']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
