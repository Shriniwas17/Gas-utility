from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return render(request, 'customers/request_success.html', {'request': service_request})
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/create_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customers/track_requests.html', {'requests': requests})
