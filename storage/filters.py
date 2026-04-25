import django_filters
from .models import Storage

class StorageFilter(django_filters.FilterSet):
    tag = django_filters.NumberFilter(field_name="tag__id")
    
    class Meta:
        model = Storage
        fields = ["tag"]