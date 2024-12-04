from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "icon", "type", "element", "casting_time", "wiki_page"]
