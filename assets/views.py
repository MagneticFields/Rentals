from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Vehicles


class BaseAssetListView(ListView):
    template_name = 'assets/index.html'


class BaseAssetDetailView(DetailView):
    template_name = 'assets/detail.html'


class AssetListView(BaseAssetListView):
    model = Vehicles
    paginate_by = 10


class AssetDetailView(BaseAssetDetailView):
    model = Vehicles


class AssetCreateView(CreateView):
    model = Vehicles
    fileds = ['__all__']
