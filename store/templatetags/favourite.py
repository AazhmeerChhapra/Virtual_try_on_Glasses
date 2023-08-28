from django import template

register = template.Library()


@register.filter (name='is_in_cart')
def is_in_cart(product, favourite):
    keys = favourite.keys()
    for id in keys:
        print("these are ",id)
        if int (id) == product.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(product, favourite):
    keys = favourite.keys ()
    for id in keys:
        if int (id) == product.id:
            return favourite.get (id)
    return 0;


@register.filter (name='price_total')
def price_total(product, favourite):
    return product.price * cart_quantity (product, favourite)


@register.filter (name='total_cart_price')
def total_cart_price(products, favourite):
    sum = 0;
    for p in products:
        sum += price_total (p, favourite)

    return sum
