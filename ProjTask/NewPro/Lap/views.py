from django.shortcuts import render,redirect
from .forms import LaptopForm
from .models import Laptop
def laptop(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            model_name = form.cleaned_data['model_name']

            ram = form.cleaned_data['ram']
            rom = form.cleaned_data['rom']
            processor = form.cleaned_data['processor']
            price = form.cleaned_data['price']
            weight = form.cleaned_data['weight']
            laptop= Laptop(company=company,model_name=model_name,ram=ram,rom=rom,processor=processor,price=price,weight=weight)
            laptop.save()
            return redirect('show_lap')
    template_name = 'addlap.html'
    context = {'form': form}
    return render(request, template_name, context)

def show(request):
    laptop=Laptop.objects.all()
    context={'laptop':laptop}
    template_name='showlap.html'
    return render(request, template_name, context)

def delete(request,i):
    laptop=Laptop.objects.get(id=i)
    laptop.delete()
    return redirect('show_lap')

def update(request,i):
    laptop = Laptop.objects.get(id=i)
    form = LaptopForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('show_lap')
    template_name = 'addlap.html'
    context = {'form': form}
    return render(request, template_name, context)
