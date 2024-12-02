from django.shortcuts import render, get_object_or_404
from .models import WikiPage, Skill


# Create your views here.
def skills_page(request):
    skill_list = Skill.objects.all()
    context = {"skills": skill_list}
    return render(request, "entry/skills.html", context)


def wiki_page(request, page_id):
    """
    Get a Wikipedia Entry for a Skill.
    """
    wiki_page = get_object_or_404(WikiPage, pk=page_id)

    context = {"wiki_page": wiki_page}
    return render(request, "entry/wiki.html", context)
