from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Destination, TourPackage
from .forms import TourPackageForm

# Create your views here.


def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {"dests": dests})


# Tour Package Views
class TourPackageListView(ListView):
    model = TourPackage
    template_name = "tour_packages/package_list.html"
    context_object_name = "packages"
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        place = self.request.GET.get("place")
        if q:
            queryset = queryset.filter(title__icontains=q)
        if place:
            queryset = queryset.filter(place__icontains=place)
        return queryset


class TourPackageDetailView(DetailView):
    model = TourPackage
    template_name = "tour_packages/package_detail.html"
    context_object_name = "package"


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.is_travel_agent()
            or self.request.user.is_superuser
        )


class TourPackageCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = TourPackage
    form_class = TourPackageForm
    template_name = "tour_packages/package_form.html"
    success_url = reverse_lazy("package-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Tour package created successfully!")
        return super().form_valid(form)


class TourPackageUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = TourPackage
    form_class = TourPackageForm
    template_name = "tour_packages/package_form.html"
    success_url = reverse_lazy("package-list")

    def form_valid(self, form):
        messages.success(self.request, "Tour package updated successfully!")
        return super().form_valid(form)


class TourPackageDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = TourPackage
    template_name = "tour_packages/package_confirm_delete.html"
    success_url = reverse_lazy("package-list")

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Tour package deleted successfully!")
        return super().delete(request, *args, **kwargs)


@login_required
def buy_package(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    if request.user.is_authenticated:
        from .models import Purchase

        # Check if already purchased
        already_purchased = Purchase.objects.filter(user=request.user, package=package).exists()
        if not already_purchased:
            Purchase.objects.create(user=request.user, package=package)
    return redirect("profile")
