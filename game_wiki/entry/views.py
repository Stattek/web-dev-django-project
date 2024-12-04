from django.shortcuts import render, get_object_or_404, redirect
from .models import WikiPage, Skill
from .forms import SkillForm


# Create your views here.
def skills_page(request):
    """ 
    GET for the skills page.
    """
    skill_list = Skill.objects.all()
    context = {"skills": skill_list}
    return render(request, "entry/skills.html", context)


def wiki_page(request, page_id):
    """
    GET a Wikipedia Entry for a Skill.
    """
    wiki_page = get_object_or_404(WikiPage, pk=page_id)

    context = {"wiki_page": wiki_page}
    return render(request, "entry/wiki.html", context)


def main_page(request):
    """
    GET the main page.
    """
    return render(request, "entry/main_page.html")


def add_skill(request):
    """
    Handles GET and POST requests to add a skill.
    """
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "entry:skills_page"
            )  # Redirect to the armory page after saving
    else:
        form = SkillForm()
    return render(request, "entry/add_skill.html", {"form": form})


def delete_skill(request, skill_id):
    """
    Deletes a skill and redirects the user back to the skills page.
    """
    the_skill = get_object_or_404(Skill, id=skill_id)
    the_skill.delete()
    return redirect("entry:skills_page")
