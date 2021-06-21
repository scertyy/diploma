from rest_framework import serializers

from backend.api.board.models import Board, Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'title', 'priority', 'team', 'tasks']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Comment
        fields = '__all__'
