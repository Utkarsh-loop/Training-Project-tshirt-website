import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tshirt_project.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Product

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created.")

# Create mock products
if not Product.objects.exists():
    Product.objects.create(
        title='Oversized Black Tee',
        description='Premium 280GSM heavyweight cotton in classic black. Designed with dropped shoulders and a boxy fit.',
        price=35.00,
        image='products/black_oversized_tshirt.png'
    )
    Product.objects.create(
        title='Oversized White Tee',
        description='Pristine white heavyweight t-shirt for daily wear. Exceptional durability and comfort.',
        price=35.00,
        image='products/white_oversized_tshirt.png'
    )
    Product.objects.create(
        title='Oversized Beige Tee',
        description='Earthy beige tone, perfect relaxed fit. A wardrobe staple that pairs with everything.',
        price=35.00,
        image='products/beige_oversized_tshirt.png'
    )
    print("Mock products added.")
