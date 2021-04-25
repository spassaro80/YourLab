from django.shortcuts import render, redirect, reverse
from .models import Stats, Match, Event
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "core/home.html")

@login_required
def create(request):
    return render(request, "core/create.html")

@login_required
def update_match(request, id):
    #TODO: lógica update en el model. Refactoring código para el request.POST 
    match = Match.objects.get(id=id)
    stats = Stats.objects.get(match=match)
    stats.first_half = request.POST.get("crono1", "00:00:00")
    stats.second_half = request.POST.get("crono4", "00:00:00")
    stats.possession1A= request.POST.get("crono2", "00:00:00")
    stats.possession1B = request.POST.get("crono3", "00:00:00")
    stats.possession2A= request.POST.get("crono5", "00:00:00")
    stats.possession2B = request.POST.get("crono6", "00:00:00")
    stats.tiri_in_porta1A_sx = int(request.POST.get("tps1A"))
    stats.tiri_in_porta1A_dx = int(request.POST.get("tpd1A"))
    stats.tiri_in_porta1A_cc = int(request.POST.get("tpc1A"))
    stats.tiri_in_fuori1A_sx = int(request.POST.get("tfs1A"))
    stats.tiri_in_fuori1A_dx = int(request.POST.get("tfd1A"))
    stats.tiri_in_fuori1A_cc = int(request.POST.get("tfc1A"))
    stats.punizioni_difensive1A_sx = int(request.POST.get("pds1A"))
    stats.punizioni_difensive1A_dx = int(request.POST.get("pdd1A"))
    stats.punizioni_difensive1A_cc = int(request.POST.get("pdc1A"))
    stats.punizioni_offensive1A_sx = int(request.POST.get("pos1A"))
    stats.punizioni_offensive1A_dx = int(request.POST.get("pod1A"))
    stats.punizioni_offensive1A_cc = int(request.POST.get("poc1A"))
    stats.cross_dx1A = int(request.POST.get("crd1A"))
    stats.cross_cc1A = int(request.POST.get("crc1A"))
    stats.cross_sx1A = int(request.POST.get("crs1A"))
    stats.corners1A = int(request.POST.get("cda1A"))
    stats.parate1A = int(request.POST.get("par1A"))
    stats.fuorigioco1A = int(request.POST.get("fuo1A"))
    stats.tiri_in_porta1B_sx = int(request.POST.get("tps1B"))
    stats.tiri_in_porta1B_dx = int(request.POST.get("tpd1B"))
    stats.tiri_in_porta1B_cc = int(request.POST.get("tpc1B"))
    stats.tiri_in_fuori1B_sx = int(request.POST.get("tfs1B"))
    stats.tiri_in_fuori1B_dx = int(request.POST.get("tfd1B"))
    stats.tiri_in_fuori1B_cc = int(request.POST.get("tfc1B"))
    stats.punizioni_difensive1B_sx = int(request.POST.get("pds1B"))
    stats.punizioni_difensive1B_dx = int(request.POST.get("pdd1B"))
    stats.punizioni_difensive1B_cc = int(request.POST.get("pdc1B"))
    stats.punizioni_offensive1B_sx = int(request.POST.get("pos1B"))
    stats.punizioni_offensive1B_dx = int(request.POST.get("pod1B"))
    stats.punizioni_offensive1B_cc = int(request.POST.get("poc1B"))
    stats.cross_dx1B = int(request.POST.get("crd1B"))
    stats.cross_cc1B = int(request.POST.get("crc1B"))
    stats.cross_sx1B = int(request.POST.get("crs1B"))
    stats.corners1B = int(request.POST.get("cda1B"))
    stats.parate1B = int(request.POST.get("par1B"))
    stats.fuorigioco1B = int(request.POST.get("fuo1B"))
    stats.tiri_in_porta2A_sx = int(request.POST.get("tps2A"))
    stats.tiri_in_porta2A_dx = int(request.POST.get("tpd2A"))
    stats.tiri_in_porta2A_cc = int(request.POST.get("tpc2A"))
    stats.tiri_in_fuori2A_sx = int(request.POST.get("tfs2A"))
    stats.tiri_in_fuori2A_dx = int(request.POST.get("tfd2A"))
    stats.tiri_in_fuori2A_cc = int(request.POST.get("tfc2A"))
    stats.punizioni_difensive2A_sx = int(request.POST.get("pds2A"))
    stats.punizioni_difensive2A_dx = int(request.POST.get("pdd2A"))
    stats.punizioni_difensive2A_cc = int(request.POST.get("pdc2A"))
    stats.punizioni_offensive2A_sx = int(request.POST.get("pos2A"))
    stats.punizioni_offensive2A_dx = int(request.POST.get("pod2A"))
    stats.punizioni_offensive2A_cc = int(request.POST.get("poc2A"))
    stats.cross_dx2A = int(request.POST.get("crd2A"))
    stats.cross_cc2A = int(request.POST.get("crc2A"))
    stats.cross_sx2A = int(request.POST.get("crs2A"))
    stats.corners2A = int(request.POST.get("cda2A"))
    stats.parate2A = int(request.POST.get("par2A"))
    stats.fuorigioco2A = int(request.POST.get("fuo2A"))
    stats.tiri_in_porta1B_sx = int(request.POST.get("tps2B"))
    stats.tiri_in_porta2B_dx = int(request.POST.get("tpd2B"))
    stats.tiri_in_porta2B_cc = int(request.POST.get("tpc2B"))
    stats.tiri_in_fuori2B_sx = int(request.POST.get("tfs2B"))
    stats.tiri_in_fuori2B_dx = int(request.POST.get("tfd2B"))
    stats.tiri_in_fuori2B_cc = int(request.POST.get("tfc2B"))
    stats.punizioni_difensive2B_sx = int(request.POST.get("pds2B"))
    stats.punizioni_difensive2B_dx = int(request.POST.get("pdd2B"))
    stats.punizioni_difensive2B_cc = int(request.POST.get("pdc2B"))
    stats.punizioni_offensive2B_sx = int(request.POST.get("pos2B"))
    stats.punizioni_offensive2B_dx = int(request.POST.get("pod2B"))
    stats.punizioni_offensive2B_cc = int(request.POST.get("poc2B"))
    stats.cross_dx2B = int(request.POST.get("crd2B"))
    stats.cross_cc2B = int(request.POST.get("crc2B"))
    stats.cross_sx2B = int(request.POST.get("crs2B"))
    stats.corners2B = int(request.POST.get("cda2B"))
    stats.parate2B = int(request.POST.get("par2B"))
    stats.fuorigioco2B = int(request.POST.get("fuo2B"))
    stats.save()
    return redirect(reverse("core:display_match", args=(match.pk,)))


@login_required
def display_match(request, id):
    match = Match.objects.get(id=id)
    stats = Stats.objects.get(match=match)
    return render(request, "core/display.html", {'match': match, 'stats': stats })

@login_required
def stats(request, id):
    match = Match.objects.get(id=id)
    stats = Stats.objects.get(match=match)
    return render(request, "core/stats.html", {'match': match, 'stats': stats })

@login_required
def display(request):
    matches = Match.objects.all()
    return render(request, "core/displayAll.html", {'matches': matches})

@login_required
def create_match(request):
    chanpionship = request.POST.get('chanpionship', None)
    time = request.POST.get('time', None)
    weather = request.POST.get('weather', None)
    date = request.POST.get('date', None)
    temperature = request.POST.get('temperature', None)
    place = request.POST.get('place', None)
    team_a = request.POST.get('team_a', None)
    team_b = request.POST.get('team_b', None)
    match = Match.objects.create(chanpionship = chanpionship, time = time, weather=weather, date=date, temperature=temperature, place=place, team_a = team_a, team_b = team_b)
    stats = Stats.objects.create(match=match)
    return redirect(reverse("core:display_match", args=(match.pk,)))

@login_required
def new_event(request,id):
    json_response = {'created' : False}
    try:
        match = Match.objects.get(id=id)
        crono = request.GET.get("crono")
        event = request.GET.get("event")
        team = request.GET.get("team")
        if team =='A':
            team = match.team_a
        elif team == 'B':
            team = match.team_b
        Event.objects.create(match=match, event = event, eventtime=crono, team=team)
        json_response = {'created' : True}
        return JsonResponse(json_response)
    except:
        return JsonResponse(json_response)

