from django.shortcuts import render, get_object_or_404, redirect
from .models import Concert, Time
from .form import ticketForm


def mainSite(request):
    return render(request, 'main/menuSite.html')

def afishaSite(request):
    concert = Concert.objects.all()
    return render(request, 'main/afishaSite.html', {'concert': concert})

def ticketsSite(request, concert_id):
    error = ''
    if request.method == 'POST':
        form = ticketForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Неверно введены данные'

    ticket = get_object_or_404(Concert, id=concert_id)

    form = ticketForm(initial={'concert': ticket.id,
                               'price': ticket.price})

    context = {
        'ticket': ticket,
        'form': form,
        'error': error
    }

    return render(request, 'main/ticketsSite.html', context=context)

def contactsSite(request):
    return render(request, 'main/contactsSite.html')

def showAfisha(request, concert_id):
    show = get_object_or_404(Concert, pk=concert_id)

    context = {
        'show': show,
        'img': show.img,
        'description': show.description,
        'name_concert': show.name_concert,
        'date_time': show.date_time,
        'janr': show.janr,
        'regisser': show.regisser,
        'length': show.length,
        'type': show.type,
        'price': show.price,
        'concert_id': show.id
    }

    return render(request, 'main/slugBuy.html', context)
