from django.views.generic import ListView
from .models import MessageCategory
from .models import Message


class HomeView(ListView):
    template_name = "home.html"
    model = Message

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('message_category')
