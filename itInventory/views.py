from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import itemForm, searchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import inventory
from django.core.exceptions import ObjectDoesNotExist
from urllib.parse import urlencode


def index(request):
    request.session['view']= False
    request.session['search'] = False
    request.session['choice'] = False
    init_form = searchForm()
    c = {
        'updatelist': inventory.objects.all().order_by('-updated')[:10],
        'form': init_form
    }
    if 'delete' in request.session:
        if request.session['delete']:
            c.update({'delete':True})
            request.session['delete'] = False
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            data = urlencode(form.cleaned_data)
            url = '/itInventory/queryInventory/?' + data
            return HttpResponseRedirect(url)
        else:
            form_errors = form.errors
            return render(request, 'itInventory/index.html', {'form': form, 'form_errors': form_errors, 'updatelist': inventory.objects.all().order_by('-updated')[:10]})
    else:
        form=searchForm()

    return render(request, "itInventory/index.html", c)


def addItem(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.process()
            return HttpResponseRedirect('/itInventory/')
        else:
            form_errors = form.errors
            return render(request, 'itInventory/addItem.html', {'form' : form, 'form_errors': form_errors})
    else:
        form = itemForm()

    return render(request, "itInventory/addItem.html", {'form': form})

def updateItem(request, item_ID):
    t = 'itInventory/updateItem.html'
    a = inventory.objects.get(id=item_ID)
    c = {
        'item': a,
        'item_ID': str(item_ID)
    }
    if request.method=="POST":
        form = itemForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            url = '/itInventory/itemDetail/'+str(item_ID)+'/'
            return HttpResponseRedirect(url)
        else:
            form_errors = form.errors
            return render(request, 'itInventory/updateItem.html', {'form': form, 'form_errors': form_errors, 'item':a, 'item_ID': str(item_ID)})

    else:
        form = itemForm(initial={'machine':a.machine, 'room':a.room,'mac':a.mac,'ip':a.ip,'vlan':a.vlan,'manufacturer':a.manufacturer,'model':a.model,'serial':a.serial,'user':a.user,'os':a.os,'department':a.department,'sponsor':a.sponsor,'notes':a.notes})

    return render(request, t, {'form':form, 'item':a, 'item_ID':str(item_ID)})

def viewInventory(request):
    request.session['view']=True
    t = "itInventory/viewInventory.html"
    c = {
        'a':inventory.objects.all()
    }
    return render(request, t, c)

def deleteItem(request, item_ID):
    if request.method=="POST":
        inventory.objects.filter(id=item_ID).delete()
        request.session['delete'] = True
        return HttpResponseRedirect('/itInventory/')
    a = inventory.objects.get(id=item_ID)
    t = "itInventory/deleteItem.html"
    c = {
        'item': a,
        'item_ID': str(item_ID),
    }
    return render(request, t, c)

def queryInventory(request):
    t = 'itInventory/queryInventory.html'
    search = request.GET.get('search')
    choices = request.GET.get('choices')
    request.session['search'] = search
    request.session['choice'] = choices
    querylist=process(search, choices)
    c={
        'a':querylist
    }
    return render(request, t, c)

def process(search, choices):
    a = search
    b = choices
    if b == 'Machine':
        try:
            c = inventory.objects.filter(machine__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
    elif b == 'Serial':
        try:
            c = inventory.objects.filter(serial__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
    elif b == 'MAC Address':
        try:
            c = inventory.objects.filter(mac__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
    elif b == 'IP Address':
        try:
            c = inventory.objects.filter(ip__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
    elif b == 'User':
        try:
            c = inventory.objects.filter(user__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist
    elif b == 'Department':
        try:
            c = inventory.objects.filter(department__icontains=a)
            return c
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist

def searchItem(request):
    #paginator
    a = inventory.objects.all()
    paginator = Paginator(a, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        c = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        c = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        c = paginator.page(paginator.num_pages)

    init_form = searchForm()
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            data = urlencode(form.cleaned_data)
            url = '/itInventory/queryInventory/?'+data
            return HttpResponseRedirect(url)
        else:
            form_errors = form.errors
            return render(request, 'itInventory/searchItem.html', {'form': form, 'form_errors': form_errors, 'a': c, 'loop':paginator.num_pages})
    else:
        form = searchForm()

    return render(request, "itInventory/searchItem.html", {'form': init_form, 'a': c, 'loop':paginator.num_pages})

def itemDetail(request, item_ID):
    a = inventory.objects.get(id=item_ID)
    t = "itInventory/itemDetail.html"
    c = {
        'item': a,
        'item_ID': str(item_ID),
    }

    return render(request, t, c)

