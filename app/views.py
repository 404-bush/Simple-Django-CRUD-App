from django.shortcuts import render,redirect,get_object_or_404
from app.models import crud
from django.views.generic.list import ListView,View
from .forms import CrudForms
from django.contrib import messages

# Create your views here.
def create(request):
        # context = {}
        form = CrudForms(request.POST)
        if form.is_valid():
           form.save()
           messages.info(request,"successfully created")
           return redirect('/')
        # context['form'] = form
        return render(request,"create.html", {'form' :form})

def details(request):
        context={}
        context["obj"] = crud.objects.all()
        return render(request,"details.html",context)

def update(request,id):
    old_form = crud.objects.get(id=id)
    if request.method == 'POST':
        form = CrudForms(request.POST ,instance = old_form)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully ")
            return redirect('/')

    else:
        form = CrudForms(instance=old_form)
        return render(request,"update.html",{'form':form})

def delete(request,id):
    data = get_object_or_404(crud,id =id)
    data.delete()
    messages.success(request, "Deleted successfully")
    return details(request)






