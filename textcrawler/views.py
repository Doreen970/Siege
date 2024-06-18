from django.shortcuts import render

# My projects views

from django.shortcuts import render
from django.core.paginator import Paginator

def PaginatedTextView(request):
    """
    a function that reads the Django documentation 100 lines at a time.
    this file implements the pagination effect.
    """
    try:
        with open('django_docs.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return render(request, 'paginated_text.html', {'error': 'The file does not exist.'})

    paginator = Paginator(lines, 100) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'paginated_text.html', {'page_obj': page_obj})

