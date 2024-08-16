from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import movieform
from movieapp.models import movie


# Create your views here.
def index(request):
    Movie = movie.objects.all()
    context = {
        'movie_list': Movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    mov = movie.objects.get(id=movie_id)

    return render(request, 'detail.html', {'movie': mov})


def add_movie(request):
    if request.method == 'POST':
        nam = request.POST.get('name', )
        yea = request.POST.get('year', )
        de = request.POST.get('des', )
        im = request.FILES['img']
        Move = movie(name=nam, des=de, img=im, year=yea)
        Move.save()
        return redirect('/')
    return render(request, 'add.html')

def update(request, id):
    movi=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
   if request.method=='POST':
        mo=movie.objects.get(id=id)
        mo.delete()
        return redirect('/')
   return render(request,'delete.html')