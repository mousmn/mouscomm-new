from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import forms, models

# Create your views here.

def Index(request):
    return render(request, 'mousweb/index.html')

def Post(request):
    form = forms.PostForm()
    return render(request, 'mousweb/post.html', {'form': form})

def PostSubmit(request):
    # Check if post request given else go to post creatation
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        # If valid do it otherwise return
        if form.is_valid():
            return render(request, 'mousweb/submit.html', {'form': form})
        else:
            return HttpResponseRedirect('/form')
    else:
        return HttpResponseRedirect('/form')

def Minecraft(request):
    mc = models.mc_table_model()
    context = {'mc': mc,}
    return render(request, 'mousweb/minecraft.html', context)

def DevNullUp(request):
    devup = forms.DevNullForm()
    context = {'devup': devup,}
    if request.method == 'POST':
        devup = forms.DevNullForm(request.POST, request.FILES)
        if devup.is_valid():
            devnull = models.DevNullHandle(request.FILES['upload'])
            return render(request, 'mousweb/devnull.html', context)

    else:
        return render(request, 'mousweb/devnullup.html', context)




