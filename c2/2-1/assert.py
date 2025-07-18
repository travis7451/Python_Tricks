shoes = {'name': '潮鞋', 'price' : 149}

def apply_discount (product,discount):
    price = product['price'] * discount
    assert 0 <= price <= product['price']
    return price
    
''' do not use assert to check admin, otherwise is will be close when you optimize your python code
def apply_discount (product_id,user):
    assert user.is_admin(),
    assert store.has_product(product_id), '無效的ID'
    store.get_product(product_id).delete()
''' 

#the right way is using if-raise to check it
def apply_discount (product_id,user):
    if not user.is_admin():
        raise AuthError('only can delete by admin!')
    if not store.has_product(product_id):
        raise ValueError('can not find the product ID')
        store.get_product(product_id).delete()
        
apply_discount(shoes, -0.5)
