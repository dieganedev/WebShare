from django.shortcuts import render, get_object_or_404
from django.http import Http404

#from .mocks import Post
from . import models

# Create your views here.
def index(request):
    postes = models.Liste.objects.all()
    return render(request, 'blog/index.html', {'postes':postes})

def show(request, id):
    #post = get_object_or_404(Post, pk=id)
    try:
        poste = models.Liste.objects.get(pk=id)
    except models.Liste.DoesNotExist:
        raise Http404('Désolé, poste #{} non trouvé.'.format(id))       
    
    return render(request, 'blog/show.html', {'poste':poste})