from django.shortcuts import render, get_object_or_404
from .models import WikiPage

def table_of_contents(request):
    #TODO: add this 
    return

# Create your views here.
def wiki_page(request, page_id):
    """
    Get a Wikipedia Entry
    """
    wiki_page = get_object_or_404(WikiPage, pk=page_id)
    
    context = {"wiki_page": wiki_page}
    return render(request, "polls/inventory.html", context)
