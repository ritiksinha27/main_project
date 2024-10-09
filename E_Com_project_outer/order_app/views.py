from django.shortcuts import render,redirect
from order_app.models import order_details
# Create your views here.

def ord_view(request):
    a = order_details.objects.all().order_by ('-id')
    if request.method == 'POST':
        order_no = request.POST.get('order_no')
        user_id = request.POST.get('user_id')
        product = request.POST.get('product')
        total_prise = request.POST.get('total_price')
        payment =request.POST.get('payment')
        shypping_address = request.POST.get('shypping_address')
        order_status = request.POST.get('order_status')
         
        if order_no:
            order_details.objects.create(order_no = order_no, user_id = user_id, product = product, total_prise = total_prise, payment = payment, shypping_address = shypping_address, order_status = order_status)
            return redirect('pro_home')
    return render(request, 'pro_home.html', {'key' : a})
