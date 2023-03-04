from django.shortcuts import render, get_object_or_404
from .models import Announcement
from .models import Church
from .models import ChurchRequest
from .models import Suggestion
from django.http import Http404


# Create your views here.


def churchs_list(request):
    churchs = Church.objects.all()
    return render(request, 'request/acceuil.html', {'churchs': churchs})


def church_detail(request, church_id):
    church = get_object_or_404(Church, id=church_id)
    return render(request, 'requeste/church/church_main.html')
