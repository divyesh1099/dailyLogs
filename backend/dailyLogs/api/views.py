from django.shortcuts import render
from rest_framework import generics, throttling
from .models import LogEntry
from .serializers import LogEntrySerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly  # Custom permission class

from django.db.models import F
from rest_framework import generics
from rest_framework.response import Response


def index(requests):
    return render(requests, 'api/index.html')

class LogEntryListCreate(generics.ListCreateAPIView):
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LogEntryDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    throttle_classes = [throttling.AnonRateThrottle, throttling.UserRateThrottle]
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment views count
        instance.views_count = F('views_count') + 1
        instance.save(update_fields=['views_count'])
        # Ensure the database updates the count before proceeding
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
