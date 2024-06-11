from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        initial_data = {'username': '', 'password': ''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'main/my-login.html', {'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect("./login")


@login_required(login_url="login")
def main(request):
    spec_list = Specialization.objects.all()
    dorm = IdentityModel.objects.filter(dorm__contains="Да").count()
    RF_citizen = Identification.objects.filter(choice__contains="Паспорт гражданина РФ").count()
    INO_citizen = Identification.objects.filter(choice__contains="Паспорт иностранного гражданина").count()
    return render(request, 'main/main.html', context={
        'spec': spec_list,
        'citizen': RF_citizen,
        'citizeni': INO_citizen,
        'dorm': dorm,
    })


@login_required(login_url="login")
def registration(request):
    error = ''
    if request.method == 'POST':
        app_form = TestForm(request.POST)
        parent_form = ParentForm(request.POST)
        pass_form = PassportForm(request.POST)
        edu_form = EducationForm(request.POST)
        place_form = PlaceForm(request.POST)
        if all([app_form.is_valid(), parent_form.is_valid(), pass_form.is_valid(), edu_form.is_valid(),
                place_form.is_valid()]):
            parent = parent_form.save(commit=False)
            parent.save()
            passport = pass_form.save(commit=False)
            passport.save()
            education = edu_form.save(commit=False)
            education.save()
            place = place_form.save(commit=False)
            place.save()
            child = app_form.save(commit=False)
            child.parent_key = parent
            child.identification_key = passport
            child.edu_key = education
            child.place_key = place
            child.save()
            return redirect('registration')
        else:
            error = 'Форма заполнена неверно'

    app_form = TestForm()
    parent_form = ParentForm()
    pass_form = PassportForm()
    edu_form = EducationForm()
    place_form = PlaceForm()

    context = {'form': app_form,
               'form_2': parent_form,
               'form_3': pass_form,
               'form_4': edu_form,
               'form_5': place_form,
               'error': error,
               }
    return render(request, 'main/registration.html', context=context)


@login_required(login_url="login")
def search_page(request):
    if 'q' in request.GET:
        q = request.GET['q']
        abb_list = IdentityModel.objects.filter(surname__contains=q)
    else:
        abb_list = IdentityModel.objects.all()
    return render(request, 'main/search.html', context={
        'abb_list': abb_list,
    })


@login_required(login_url="login")
def show_abb(request, abb_id):
    abb = IdentityModel.objects.get(pk=abb_id)
    return render(request, 'main/show.html', context={
        'abb': abb,
    })


@login_required(login_url="login")
def delete(request, abb_id):
    abb = IdentityModel.objects.get(pk=abb_id)
    abb.delete()
    return redirect('search')


@login_required(login_url="login")
def update(request, abb_id):
    abb = IdentityModel.objects.get(pk=abb_id)
    pas = abb.identification_key
    par = abb.parent_key
    edu = abb.edu_key
    place = abb.place_key
    abb_form = TestForm(request.POST or None, instance=abb)
    pass_form = PassportForm(request.POST or None, instance=pas)
    parent_form = ParentForm(request.POST or None, instance=par)
    edu_form = EducationForm(request.POST or None, instance=edu)
    place_form = PlaceForm(request.POST or None, instance=place)
    if all([abb_form.is_valid(), pass_form.is_valid(), parent_form.is_valid(), edu_form.is_valid(),
            place_form.is_valid()]):
        abb_form.save()
        pass_form.save()
        parent_form.save()
        edu_form.save()
        place_form.save()
        return redirect('search')
    context = {'form': abb_form,
               'form_3': pass_form,
               'form_2': parent_form,
               'form_4': edu_form,
               'form_5': place_form,
               }
    return render(request, 'main/update.html', context=context)
