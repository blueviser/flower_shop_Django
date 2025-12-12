import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
django.setup()

from shop.models import Category, Product
from django.core.files import File
from io import BytesIO
from PIL import Image
import requests

def create_test_image(color='red'):
    """Создает тестовое изображение"""
    img = Image.new('RGB', (400, 300), color=color)
    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    return img_io

def populate_database():
    print("Создание категорий...")
    
    categories_data = [
        {'name': 'Букеты', 'slug': 'bouquets'},
        {'name': 'Розы', 'slug': 'roses'},
        {'name': 'Тюльпаны', 'slug': 'tulips'},
        {'name': 'Орхидеи', 'slug': 'orchids'},
        {'name': 'Свадебные', 'slug': 'wedding'},
        {'name': 'Подарочные', 'slug': 'gift'},
    ]
    
    categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={'name': cat_data['name']}
        )
        categories[cat_data['slug']] = category
        print(f'Категория: {category.name}')
    
    print("\nСоздание товаров...")
    
    products_data = [
        {
            'name': 'Розовая мечта',
            'slug': 'pink-dream',
            'category': 'bouquets',
            'price': 3500,
            'description': 'Нежный букет из розовых роз и эустом. Идеально для романтического свидания.'
        },
        {
            'name': 'Красная страсть',
            'slug': 'red-passion',
            'category': 'roses',
            'price': 2800,
            'description': 'Букет из 51 красной розы. Выражает сильные чувства и страсть.'
        },
        {
            'name': 'Весенние тюльпаны',
            'slug': 'spring-tulips',
            'category': 'tulips',
            'price': 1800,
            'description': 'Яркие разноцветные тюльпаны. Символ весны и обновления.'
        },
        {
            'name': 'Белая орхидея',
            'slug': 'white-orchid',
            'category': 'orchids',
            'price': 4200,
            'description': 'Элегантная белая орхидея в горшке. Для изысканного подарка.'
        },
        {
            'name': 'Свадебный букет',
            'slug': 'wedding-bouquet',
            'category': 'wedding',
            'price': 5500,
            'description': 'Нежный свадебный букет невесты из белых роз и лилий.'
        },
        {
            'name': 'Праздничная композиция',
            'slug': 'holiday-composition',
            'category': 'gift',
            'price': 3200,
            'description': 'Яркая праздничная композиция для любого торжества.'
        },
        {
            'name': 'Летнее настроение',
            'slug': 'summer-mood',
            'category': 'bouquets',
            'price': 2400,
            'description': 'Солнечный букет из полевых цветов. Дарит радость и тепло.'
        },
        {
            'name': 'Желтые розы',
            'slug': 'yellow-roses',
            'category': 'roses',
            'price': 2600,
            'description': 'Букет из желтых роз. Символ дружбы и заботы.'
        },
    ]
    
    for prod_data in products_data:
        category = categories[prod_data['category']]
        
        # Создаем тестовое изображение
        colors = {'bouquets': 'pink', 'roses': 'red', 'tulips': 'yellow', 
                 'orchids': 'white', 'wedding': 'lightblue', 'gift': 'orange'}
        
        # Создаем продукт без изображения сначала
        product, created = Product.objects.get_or_create(
            slug=prod_data['slug'],
            defaults={
                'name': prod_data['name'],
                'category': category,
                'price': prod_data['price'],
                'description': prod_data['description'],
                'available': True
            }
        )
        
        if created:
            print(f'Товар создан: {product.name} - {product.price} руб.')
    
    print(f"\nВсего создано: {Category.objects.count()} категорий, {Product.objects.count()} товаров")

if __name__ == '__main__':
    populate_database()