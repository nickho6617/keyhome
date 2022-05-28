from django.views.generic import TemplateView, ListView

from assets.models import OwnedProperty


class HomePageView(ListView):
    model = OwnedProperty
    template_name = "home.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            qs = OwnedProperty.objects.filter(owner=self.request.user)
        else:
            qs = None
        return qs


class AboutPageView(TemplateView):
    template_name = "about.html"
