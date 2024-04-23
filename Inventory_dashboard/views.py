from django.shortcuts import render,redirect
from .models import Product
from .models import Order
from .forms import OrderForm
from Inventory_Management_Project.stockslibrary.stockslibrary.invsystem import calculate_total_quantity
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse


def index(request):
     # This function renders the index.html template
    return render(request,'index.html')

def products(request):
    # Retrieve all product items from the database
    product_items=Product.objects.all()
    # calling the library function
    total_quantity = calculate_total_quantity(product_items)
    # Render the products.html template with product items as context
    return render(request, 'products.html', {'product_items': product_items, 'total_quantity': total_quantity})
    
def staff(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with POST data
        form = OrderForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the 'staff' page after successful form submission
            return redirect('staff')
    else:
        # If the request method is not POST, create an empty form instance
        form = OrderForm()
    # Retrieve all orders from the database
    orders=Order.objects.all()
    # Render the 'staff.html' template with form and orders as context
    return render(request,'staff.html',{'form': form, 'orders': orders})
    
    
def editorder(request, order_id):
    # Retrieve the order instance with the given order_id, or return a 404 page if not found
    order = get_object_or_404(Order, pk=order_id)
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with POST data and the retrieved order instance
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
             # Redirect to the 'staff' page after successful form submission
            return redirect('staff')
    else:
        # If the request method is not POST, create a form instance with the retrieved order instance
        form = OrderForm(instance=order)
        # Render the 'editorder.html' template with the form as context
    return render(request, 'editorder.html', {'form': form})

def deleteorder(request, order_id):
    # Retrieve the order instance with the given order_id, or return a 404 page if not found
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        # Redirect to the 'staff' page after successful form submission
        return redirect('staff')
     # Render the 'deleteorder.html' template with the form as context   
    return render(request, 'deleteorder.html', {'order': order})
    
def productcount(request):
    product_items=Product.objects.all()
    total_quantity = calculate_total_quantity(product_items.values_list('quantity', flat=True))
    return render(request,'products.html',{'product_items':product_items})
    
    

    


    
