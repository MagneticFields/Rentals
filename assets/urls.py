from django.urls import path

from .views import AssetListView, AssetDetailView

urlpatterns = [
    path('', AssetListView.as_view(), name='asset_list'),
    path('<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
]
