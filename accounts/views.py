from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CustomerLoginForm, CustomerRegistrationForm, ReservationForm
from . models import *
from django.views.generic import CreateView, FormView
from .decorators import allowed_users
# Create your views here.


def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)


def room(request):
    rooms = Room.objects.all()
    return render(request, 'accounts/rooms.html', {'rooms': rooms})


@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    # last_ten_customers = Customer.objects.all().order_by('-id')[:10]
    # last_ten_reservations = Reservation.objects.all().order_by('-id')[:10]
    # last_ten_in_ascending_order = reversed(last_ten_reservations)
    # context = {'last_ten_customers': last_ten_customers, 'last_ten_reservations': last_ten_reservations}
    customers = Customer.objects.all()
    reservations = Reservation.objects.all()
    context = {'customers': customers, 'reservations': reservations}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user.customer
            form.save()
            messages.success(request, 'Reservation added')
            return redirect('reservation')
    context = {'form': form}
    return render(request, 'accounts/reservation_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def my_reservation(request):
    customer_reservation = Reservation.objects.filter(customer=request.user.customer)
    context = {'customer_reservation': customer_reservation}
    return render(request, 'accounts/customer_reservation.html', context)


@login_required(login_url='login')
def update_reservation(request, pk):
    reservations = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservations)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservations)
        if form.is_valid():
            form.instance.customer = request.user.customer
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/reservation_form.html', context)


@login_required(login_url='login')
def delete_reservation(request, pk):
    reservations = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservations.delete()
        return redirect('home')
    context = {'item': reservations}
    return render(request, 'accounts/delete_reservation.html', context)


class CustomerLoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = CustomerLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        em = form.cleaned_data.get('email')
        pword = form.cleaned_data.get('password')
        usr = authenticate(username=uname, email=em, password=pword)
        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'invalid credentials'})

        return super().form_valid(form)

    def get(self, *args, **kwargs):  # redirect users to home if they're already logged in
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(CustomerLoginView, self).get(*args, **kwargs)


class CustomerRegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        group = Group.objects.get(name='customer')
        user.groups.add(group)
        login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):  # redirect users to tasks lists if they're already logged in
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(CustomerRegistrationView, self).get(*args, **kwargs)


def about_us(request):
    context = {}
    return render(request, 'accounts/about_us.html', context)
















