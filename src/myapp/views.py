from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from .models import Pic, share
from .forms import PicForm
from PIL import Image
from django.urls import reverse

global image

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = Pic.objects.create(**form.cleaned_data)
            global image
            image = newpic.picfile
            context={
            'image': newpic.picfile
            }

    return render(request, 'fileuploader.html', context)
    return image

def index(request):
    form = PicForm()
    return render(request, 'index.html', {"form":form})

def wbcolor(request):
    print(image.url[1:])
    col = Image.open(image.url[1:])
    gray = col.convert('L')
    gray.save(image.url[1:])
    context={
    'image': image
    }
    return render(request, 'fileuploader.html', context)

def rotate(request):
    deg = request.POST.get('deg', False)
    img = Image.open(image.url[1:])
    rot = img.rotate(int(deg))
    rot.save(image.url[1:])
    context={
    'image': image
    }
    return render(request, 'fileuploader.html', context)

def resize(request):
    length = request.POST.get('length', False)
    width = request.POST.get('width', False)
    img = Image.open(image.url[1:])
    res = img.resize((int(length), int(width)))
    res.save(image.url[1:])
    context={
    'image': image
    }
    return render(request, 'fileuploader.html', context)

def crop(request):
    try:
        x = request.POST.get('x', False)
        width = request.POST.get('width', False)
        length = request.POST.get('length', False)
        y = request.POST.get('y', False)
        img = Image.open(image.url[1:])
        crp = img.crop((int(x), int(y), int(x+width), int(y+length)))
        crp.save(image.url[1:])
        context={
        'image': image
        }
    except ValueError as error:
        print('we will not catch exception: Exception')
    return render(request, 'fileuploader.html', context)

def sshare(request):
    share.objects.create(photo=image)
    ash = share.objects.all()
    cont = {'ash': ash}
    return render(request, 'share.html', cont)

def gallery(request):
    ash = share.objects.all()
    cont = {'ash': ash}
    return render(request, 'gallery.html', cont)
