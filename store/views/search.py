from django.shortcuts import render

def search(request):
    if request.method == 'GET':
        search_query = request.GET.get('query')  # Retrieve the search query from the request parameters

        # Perform the search operation based on the search query
        # Implement your search logic here
        # Assuming you have a list of products to search from called 'products'

        results = []
        for product in products:
            # Check if the search query matches the complete name of the product or contains unique numbers
            if search_query.lower() in product['name'].lower() or contains_unique_numbers(search_query, product['name']):
                results.append(product)

        # Return the search results to the client
        # You can render a template with the search results or return a JSON response, depending on your requirements

        # Example: Rendering a template with search results
        context = {
            'search_query': search_query,
            'results': results,
        }
        return render(request, 'search_results.html', context)

def contains_unique_numbers(search_query, product_name):
    """
    Check if the search query contains unique numbers and matches the complete name in the alphabet.
    Modify this function according to your requirements.
    """
    numbers = set('0123456789')  # Unique numbers
    query_digits = set(char for char in search_query if char.isdigit())
    return query_digits == numbers and search_query.lower() == product_name.lower()
