from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

# Modify the store function in home.py

# def print(param, param1):
#     pass


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    # Check if a search query is present in the request parameters
    search_query = request.GET.get('search')
    if search_query:
        # Perform the search operation to retrieve search results
        # Replace the following line with your search logic
        search_results = Products.objects.filter(name__icontains=search_query)
        # Update the 'products' variable to hold the search results
        products = search_results
    elif categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    print(data['products'])

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def back_to_store(request, product_id):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    # Check if a search query is present in the request parameters
    search_query = request.GET.get('search')
    if search_query:
        # Perform the search operation to retrieve search results
        search_results = Products.objects.filter(name__icontains=search_query)
        # Update the 'products' variable to hold the search results
        products = search_results
    elif categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


