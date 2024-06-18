from django.urls import path
from .views import PaginatedTextView

# url path that the user will follow when he or she wants to see the crawled data

urlpatterns = [
    path('paginated-text/', PaginatedTextView, name='paginated_text'),
]
