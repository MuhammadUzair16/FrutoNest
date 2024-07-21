from django.shortcuts import render
from .models import TeamMember

def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'about/about.html', {'team_members': team_members})

def about(request):

    team = TeamMember.objects.all()

    return render(request, 'about.html', {
        team : 'about',


    })