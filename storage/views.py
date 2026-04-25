from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema, OpenApiTypes
from rest_framework.exceptions import MethodNotAllowed
from drf_spectacular.openapi import OpenApiParameter
from django_filters.rest_framework import DjangoFilterBackend
from scalar.get_filter_parameters import get_filter_parameters
from .filters import StorageFilter

from .models import Storage, Tags
from .serializers import StorageSerializer, TagsSerializer

MULTIPART_SCHEMA = {
    'multipart/form-data': {
        'type': 'object',
        'properties': {
            'label': {'type': 'string'},
            'description': {'type': 'string'},
            'function': {'type': 'string'},
            'link': {'type': 'string'},
            'image': {'type': 'string', 'format': 'binary'},
            'tags': {'type': 'string'}
        }
    }
}


class StorageView(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = StorageSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = StorageFilter
    
    @extend_schema(
        parameters = get_filter_parameters(StorageFilter)
    )

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET', detail='use /get_storage/ instead')
    
    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST', detail='use /create_storage/ instead')
    
    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET', detail='user /get_storage_id/ intead')
    
    
    def get_queryset(self):
        return Storage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @extend_schema(
        request={'multipart/form-data': StorageSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        request={'multipart/form-data': StorageSerializer},
    )
    @action(detail=False, methods=["post"])
    def create_storage(self, request, pk=None):
        storages = Storage.objects.filter(user=request.user)
        if request.FILES.get('image') and request.FILES['image'].size > 10 * 1024 * 1024:
            return Response({'Error': 'Image size exceed limit 10MB'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def get_storage(self, request):
        content = Storage.objects.filter(user=request.user)
        serializer = self.get_serializer(content, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def get_storage_id(self, request, pk=None):
        content = self.get_object()
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def delete_storage(self, request, pk=None):
        content = self.get_object()
        content.delete()
        return Response({'Message': f'Deleted Data id:{content.id} From Storage'}, status=status.HTTP_200_OK)

    @extend_schema(
        request={'multipart/form-data': StorageSerializer},
    )
    @action(detail=True, methods=['push', 'patch'])
    def update_storage(self, request, pk=None):
        content = self.get_object()
        serializer = self.get_serializer(content, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsView(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TagsSerializer
    
    def get_queryset(self, request):
        return Tags.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    @action(detail=False, methods=["post"])
    def create_tag(self, request):
        serializer = self.get_seriailizer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def list_all_tag(self, request):
        tag = Tags.objects.filter(user=request.user)
        serializer = self.get_serializer(tag, partial=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def get_tag_by_id(self, request, pk=None):
        tag = self.get_object()
        serializer = self.get_serializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['delete'])
    def delete_tag(self, request, pk=None):
        tag = self.get_object()
        tag.delete()
        return Response({'Message':'Tag Deleted'})
    
    @action(detail=True, methods=['push', 'patch'])
    def update_tag(self, request, pk=None):
        tag = self.get_object()
        serializer = self.get_serializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)