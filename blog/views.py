from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic.edit import FormView
from .models import FileFieldForm

#from .mocks import Post
from . import models

# Create your views here.
def index(request):
    postes = models.Liste.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'postes':postes})

def show(request, id):
    #post = get_object_or_404(Post, pk=id)
    try:
        poste = models.Liste.objects.get(pk=id)
    except models.Liste.DoesNotExist:
        raise Http404('Désolé, poste #{} non trouvé.'.format(id))       
    
    return render(request, 'blog/show.html', {'poste':poste})



class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)