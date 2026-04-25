from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StorageView, TagsView

router = DefaultRouter()
router.register(r"storage", StorageView, basename="storage")
router.register(r"tag", TagsView, basename="tag") 


urlpatterns=[
    path('', include(router.urls)),
    
]
