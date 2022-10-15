from django.shortcuts import render

from family.models import FamilyMember

# Create your views here.


def show_family_members(request):
    members = FamilyMember.objects.all()
    return render(request, 'family.html', {'members': members})
