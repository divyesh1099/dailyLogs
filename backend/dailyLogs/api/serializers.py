from rest_framework import serializers
from .models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user', 'mood', 'keywords', 'summary', 'views_count']
        read_only_fields = ['user']