# views.py
from django.shortcuts import redirect, render
from store.models.product import Products

def favourite_item(request, product_id):
    if 'favorites' not in request.session:
        request.session['favorites'] = {}
    favorites = request.session['favorites']
    favorites[product_id] = favorites.get(product_id, 0) + 1
    request.session['favorites'] = favorites
    return redirect('homepage')  # Redirect to your product list page

def favorite_items(request):
    favorites = request.session.get('favorites', {})
    # Fetch products using the keys in favorites
    favorite_products = Products.objects.filter(id__in=favorites.keys())
    return render(request, 'favourite.html', {'favorite_products': favorite_products})