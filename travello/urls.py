from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Tour Package URLs
    path("packages/", views.TourPackageListView.as_view(), name="package-list"),
    path("packages/<int:pk>/", views.TourPackageDetailView.as_view(), name="package-detail"),
    path("packages/new/", views.TourPackageCreateView.as_view(), name="package-create"),
    path("packages/<int:pk>/edit/", views.TourPackageUpdateView.as_view(), name="package-update"),
    path("packages/<int:pk>/delete/", views.TourPackageDeleteView.as_view(), name="package-delete"),
    path("packages/<int:pk>/buy/", views.buy_package, name="package-buy"),
]
