def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },{
        'id': 2,
        'name': 'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id':1,
        'name':'IPhone 13',
        'price': 20000000,
        'image':'https://seoulmobile.com.vn/images/stories/virtuemart/product/refurb-iphone-13-pro-max-silver-2023.jpg'
    },
        {
            'id': 1,
            'name': 'IPhone 15',
            'price': 20000000,
            'image': 'https://seoulmobile.com.vn/images/stories/virtuemart/product/refurb-iphone-13-pro-max-silver-2023.jpg'
        },
        {
            'id': 1,
            'name': 'Galaxy A54 5G',
            'price': 20000000,
            'image': 'https://seoulmobile.com.vn/images/stories/virtuemart/product/refurb-iphone-13-pro-max-silver-2023.jpg'
        },
        {
            'id': 1,
            'name': 'Oppo',
            'price': 20000000,
            'image': 'https://seoulmobile.com.vn/images/stories/virtuemart/product/refurb-iphone-13-pro-max-silver-2023.jpg'
        },
        {
            'id': 1,
            'name': 'Xiaomi',
            'price': 20000000,
            'image': 'https://seoulmobile.com.vn/images/stories/virtuemart/product/refurb-iphone-13-pro-max-silver-2023.jpg'
        }
    ]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products