from django.shortcuts import render
from .models import TravelOption
from django.db.models import Q

def travel_list(request):
    travels = TravelOption.objects.all()

    travel_type = request.GET.get('type', 'All')
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')
    query = request.GET.get('q', '')

    if travel_type != 'All':
        travels = travels.filter(type__iexact=travel_type)
    if source:
        travels = travels.filter(source__icontains=source)
    if destination:
        travels = travels.filter(destination__icontains=destination)
    if date:
        travels = travels.filter(date_time__date=date)
    if query:
        travels = travels.filter(
            Q(type__icontains=query) |
            Q(source__icontains=query) |
            Q(destination__icontains=query)
        )

    filters = {
        'type': travel_type,
        'source': source,
        'destination': destination,
        'date': date,
        'q': query,
    }

    return render(request, 'travels/travel_list.html', {'travels': travels, 'filters': filters})
