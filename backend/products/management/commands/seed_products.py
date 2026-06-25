"""
Management command: seed_products
Run: python manage.py seed_products
"""
from django.core.management.base import BaseCommand
from products.models import Category, Product, ProductImage, Banner

CATALOG = {
    'women': {
        'name': 'Women',
        'icon': '👩',
        'filters': ['All', 'Figurines', 'Fashion & Beauty', 'Couples'],
        'description': 'Silicone molds featuring women-themed designs — fashion figures, accessories, beauty products and more.',
        'products': [
            {'product_id': 'w1', 'name': 'Chanel Perfume Bottle', 'emoji': '🌸', 'price': 599, 'mrp': 599, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion & Beauty', 'img': '', 'description': 'Size: 10×6×2 cm'},
            {'product_id': 'w2', 'name': 'YSL and D&G Lipstick Set', 'emoji': '💄', 'price': 645, 'mrp': 645, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion & Beauty', 'img': '', 'description': 'Size: 8.5×2.5×1.5 cm'},
            {'product_id': 'w3', 'name': "Women's Handbags Set", 'emoji': '👜', 'price': 835, 'mrp': 835, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion & Beauty', 'img': '', 'description': 'Size: 3.6×3.6×1 cm'},
            {'product_id': 'w4', 'name': "Women's Makeup Set", 'emoji': '💅', 'price': 835, 'mrp': 835, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion & Beauty', 'img': '', 'description': 'Size: 3.6×3.6×1 cm'},
            {'product_id': 'w5', 'name': "Indian Mom's Dressing Set", 'emoji': '👗', 'price': 835, 'mrp': 835, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion & Beauty', 'img': '', 'description': 'Size: 3.6×3.6×1 cm'},
            {'product_id': 'w6', 'name': 'Couple', 'emoji': '👫', 'price': 755, 'mrp': 755, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Couples', 'img': '', 'description': 'Size: 10×7.5×1.5 cm'},
            {'product_id': 'w7', 'name': 'Girl Holding Heart Balloons', 'emoji': '🎈', 'price': 705, 'mrp': 705, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Figurines', 'img': '', 'description': 'Size: 10×6.5×1.5 cm'},
            {'product_id': 'w8', 'name': 'Girl Carrying a Dog', 'emoji': '🐶', 'price': 635, 'mrp': 635, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Figurines', 'img': '', 'description': 'Size: 10×7×2 cm'},
        ],
    },
    'men': {
        'name': 'Men',
        'icon': '👨',
        'filters': ['All', 'Figurines', 'Fashion Objects', 'Gym & Fitness'],
        'description': 'Silicone molds featuring men-themed designs — figures, fashion objects, gym equipment and more.',
        'products': [
            {'product_id': 'mn1', 'name': 'Man in Shirt with Folded Arms', 'emoji': '👔', 'price': 670, 'mrp': 670, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Figurines', 'img': '', 'description': 'Size: 9×8×1.2 cm'},
            {'product_id': 'mn2', 'name': 'Man in Suit with Folded Arms', 'emoji': '🤵', 'price': 670, 'mrp': 670, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Figurines', 'img': '', 'description': 'Size: 9×8×1.2 cm'},
            {'product_id': 'mn3', 'name': 'Man in Shirt & Suit with Folded Arms Combo Set', 'emoji': '👔', 'price': 735, 'mrp': 735, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Figurines', 'img': '', 'description': 'Size: 7.7×7×1.5 cm'},
            {'product_id': 'mn4', 'name': "Men's Fashion Objects Set - Large", 'emoji': '👞', 'price': 1025, 'mrp': 1025, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion Objects', 'img': '', 'description': 'Set contains 6 designs — Wallet, Perfume bottle, Shoes, Watch, Belt and Hat. Size: 5×5×2 cm'},
            {'product_id': 'mn5', 'name': "Men's Fashion Objects Set - Small", 'emoji': '👞', 'price': 705, 'mrp': 705, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion Objects', 'img': '', 'description': 'Set contains 6 designs — Wallet, Perfume bottle, Shoes, Watch, Belt and Hat. Size: 3.6×3.6×1.2 cm'},
            {'product_id': 'mn6', 'name': "Men's Gym Set", 'emoji': '💪', 'price': 730, 'mrp': 730, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Gym & Fitness', 'img': '', 'description': 'Set contains 6 designs — Boxing Gloves, Biceps, Dumbell, Torso, Kettlebell, Whey Protein bottle. Size: 3.6×3.6×1.6 cm'},
            {'product_id': 'mn7', 'name': 'Genz Objects Set', 'emoji': '🎧', 'price': 720, 'mrp': 720, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion Objects', 'img': '', 'description': 'Set contains 6 designs — Headphones, Trophy, Tshirt, Cap, Smartwatch, Slides. Size: 3.6×3.6×1.6 cm'},
            {'product_id': 'mn8', 'name': 'Liquour Bottles Set', 'emoji': '🍾', 'price': 1199, 'mrp': 1199, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Fashion Objects', 'img': '', 'description': 'Size: 10×4.5×2 cm'},
        ],
    },
    'animals': {
        'name': 'Animals & Teddies',
        'icon': '🐨',
        'filters': ['All', 'Teddy Bears', 'Rabbits'],
        'description': 'Adorable animal and teddy bear silicone molds for chocolates and candles.',
        'products': [
            {'product_id': 'an1', 'name': 'Teddy Holding Tulips', 'emoji': '🧸', 'price': 587, 'mrp': 587, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Teddy Bears', 'img': '', 'description': 'Size: 8.2×7.8×2.8 cm'},
            {'product_id': 'an2', 'name': 'Teddy Bear Pair', 'emoji': '🧸', 'price': 595, 'mrp': 595, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Teddy Bears', 'img': '', 'description': 'Size: 7.6×7.4×2 cm'},
            {'product_id': 'an3', 'name': 'Teddy Bear with Heart', 'emoji': '🧸', 'price': 580, 'mrp': 580, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Teddy Bears', 'img': '', 'description': 'Size: 3.7×3.7×1.7 cm'},
            {'product_id': 'an4', 'name': 'Teddy Bear with Letters, I Heart U', 'emoji': '🧸', 'price': 560, 'mrp': 560, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Teddy Bears', 'img': '', 'description': 'Size: 3.7×3.7×1.6 cm'},
            {'product_id': 'an5', 'name': 'Singing Teddy Hiding Gift Box', 'emoji': '🎁', 'price': 695, 'mrp': 695, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Teddy Bears', 'img': '', 'description': 'Size: 8×3.5×4 cm'},
            {'product_id': 'an6', 'name': 'Baby Rabbit on its Back', 'emoji': '🐰', 'price': 595, 'mrp': 595, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Rabbits', 'img': '', 'description': 'Size: 8×4.5×2.8 cm'},
            {'product_id': 'an7', 'name': 'Rabbit with Hand Heart Gesture', 'emoji': '🐰', 'price': 645, 'mrp': 645, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Rabbits', 'img': '', 'description': 'Size: 6×5×4.5 cm'},
        ],
    },
    'cakes': {
        'name': 'Cakes & Cupcakes',
        'icon': '🎂',
        'filters': ['All', 'Cakes', 'Cupcakes'],
        'description': 'Beautiful cake and cupcake shaped silicone molds.',
        'products': [
            {'product_id': 'ck1', 'name': 'Heart Creeper Pattern on Cake with Ribbon Bow', 'emoji': '🎂', 'price': 875, 'mrp': 875, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Cakes', 'img': '', 'description': 'Size: 9.5×9×7 cm'},
            {'product_id': 'ck2', 'name': 'Wavy Rim Heart Creeper Pattern on Cake with Ribbon Bow', 'emoji': '🎂', 'price': 765, 'mrp': 765, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Cakes', 'img': '', 'description': 'Size: 7×7×5 cm'},
            {'product_id': 'ck3', 'name': 'Cupcake with Cream', 'emoji': '🧁', 'price': 670, 'mrp': 670, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Cupcakes', 'img': '', 'description': 'Size: 7×7×5 cm'},
        ],
    },
    'rakhi': {
        'name': 'Rakhi',
        'icon': '🪢',
        'filters': ['All', 'Chocolate & Candle Molds', 'Candle Holders', 'Tealight Holders', 'Combo Sets'],
        'description': 'Raksha Bandhan special silicone molds for chocolates, candles and tealight holders.',
        'products': [
            {'product_id': 'rk1', 'name': 'Rakhi', 'emoji': '🪢', 'price': 579, 'mrp': 579, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Chocolate & Candle Molds', 'img': '', 'description': 'Size: 14.5×5×1.5 cm'},
            {'product_id': 'rk2', 'name': 'Sister Tying Rakhi', 'emoji': '🪢', 'price': 675, 'mrp': 675, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Chocolate & Candle Molds', 'img': '', 'description': 'Size: 10.5×9×1.5 cm'},
            {'product_id': 'rk3', 'name': 'Rakhi Tying Hands', 'emoji': '🤝', 'price': 570, 'mrp': 570, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Chocolate & Candle Molds', 'img': '', 'description': 'Size: 7.6×7.6×2 cm'},
            {'product_id': 'rk4', 'name': 'Drama Queen Sister', 'emoji': '👑', 'price': 735, 'mrp': 735, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Chocolate & Candle Molds', 'img': '', 'description': 'Size: 10.5×10.5×2 cm'},
            {'product_id': 'rk5', 'name': 'Flower Tealight Candle Set', 'emoji': '🌸', 'price': 665, 'mrp': 665, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Tealight Holders', 'img': '', 'description': 'Size: 4.3×4.3×2 cm'},
            {'product_id': 'rk6', 'name': 'Happy Rakhsabandhan Tealight Holder and Flower Tealight Candle Combo Set', 'emoji': '🕯️', 'price': 925, 'mrp': 925, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Combo Sets', 'img': '', 'description': 'Sizes: 10×10×1.8 cm and 4.3×4.3×2 cm'},
            {'product_id': 'rk7', 'name': 'Happy Rakhsabandhan Tealight Holder', 'emoji': '🕯️', 'price': 670, 'mrp': 670, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Tealight Holders', 'img': '', 'description': 'Size: 10×10×1.8 cm'},
            {'product_id': 'rk8', 'name': 'Happy Rakhi Candle Holder and Rakhi Tying Hands Candle Combo Set', 'emoji': '🕯️', 'price': 899, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Combo Sets', 'img': '', 'description': 'Sizes: 11.5×10.5×2.5 cm and 7.6×7.6×2 cm'},
            {'product_id': 'rk9', 'name': 'Happy Rakhi Candle Holder', 'emoji': '🕯️', 'price': 685, 'mrp': 685, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Candle Holders', 'img': '', 'description': 'Size: 11.5×10.5×2.5 cm'},
        ],
    },
    'diwali': {
        'name': 'Diwali',
        'icon': '🪔',
        'filters': ['All', 'Crackers', 'Festive Shapes', 'Mandalas'],
        'description': 'Diwali themed silicone molds — crackers, diyas, mandalas and festive shapes.',
        'products': [
            {'product_id': 'dw1', 'name': 'Anaar Cracker', 'emoji': '🎆', 'price': 725, 'mrp': 725, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Crackers', 'img': '', 'description': 'Size: 9×9×7.3 cm'},
            {'product_id': 'dw2', 'name': 'Sutli Bomb', 'emoji': '💣', 'price': 565, 'mrp': 565, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Crackers', 'img': '', 'description': 'Size: 4×4×4.3 cm'},
            {'product_id': 'dw3', 'name': 'Chakri Cracker', 'emoji': '🌀', 'price': 535, 'mrp': 535, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Crackers', 'img': '', 'description': 'Size: 7.5×7.5×1 cm'},
            {'product_id': 'dw4', 'name': 'Bonfire Logs', 'emoji': '🪵', 'price': 530, 'mrp': 530, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Festive Shapes', 'img': '', 'description': 'Size: 7×5 cm'},
            {'product_id': 'dw5', 'name': 'Kite and Spool', 'emoji': '🪁', 'price': 655, 'mrp': 655, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Festive Shapes', 'img': '', 'description': 'Sizes: 7, 6, 4.5 and 5, 4 cm'},
            {'product_id': 'dw6', 'name': 'Dhol', 'emoji': '🥁', 'price': 557, 'mrp': 557, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Festive Shapes', 'img': '', 'description': 'Size: 6×6×5 cm'},
            {'product_id': 'dw7', 'name': 'Bonfire Mandala Base', 'emoji': '🪔', 'price': 495, 'mrp': 495, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Mandalas', 'img': '', 'description': 'Size: 8×8×1 cm'},
            {'product_id': 'dw8', 'name': 'Mandala Base', 'emoji': '🪔', 'price': 545, 'mrp': 545, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Mandalas', 'img': '', 'description': 'Size: 8.5×8.5×1.5 cm'},
        ],
    },
    'eidramadan': {
        'name': 'Eid / Ramadan',
        'icon': '🌙',
        'filters': ['All', 'Mosques', 'Lanterns', 'Slabs'],
        'description': 'Islamic festival silicone molds for Eid and Ramadan celebrations.',
        'products': [
            {'product_id': 'er1', 'name': 'Miniature Mosques', 'emoji': '🕌', 'price': 950, 'mrp': 950, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Mosques', 'img': '', 'description': 'Size: 3.5×3.5×2 cm'},
            {'product_id': 'er2', 'name': 'Islamic Patterned Lanterns', 'emoji': '🏮', 'price': 685, 'mrp': 685, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Lanterns', 'img': '', 'description': 'Size: 9.8×5.8×1 cm'},
            {'product_id': 'er3', 'name': 'Islamic Patterned Slab', 'emoji': '✨', 'price': 645, 'mrp': 645, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Slabs', 'img': '', 'description': 'Size: 15×8×1 cm'},
        ],
    },
    'jars': {
        'name': 'Jars',
        'icon': '🫙',
        'filters': ['All', 'Plain Jars', 'Shaped Jars', 'Jars with Lid'],
        'description': 'Decorative jar silicone molds for candles, concrete, and resin — various shapes and sizes.',
        'products': [
            {'product_id': 'jr1', 'name': 'Zigzag Jar with Outer Support - Small', 'emoji': '🫙', 'price': 870, 'mrp': 870, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Plain Jars', 'img': '', 'description': 'Size: 9×6.5 cm'},
            {'product_id': 'jr2', 'name': 'Zigzag Jar with Outer Support - Large', 'emoji': '🫙', 'price': 1795, 'mrp': 1795, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Plain Jars', 'img': '', 'description': 'Size: 15×9 cm'},
            {'product_id': 'jr3', 'name': 'Heart Shaped Jar', 'emoji': '❤️', 'price': 735, 'mrp': 735, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Shaped Jars', 'img': '', 'description': 'Size: 9×8.5×4 cm'},
            {'product_id': 'jr4', 'name': 'XOXO Jar', 'emoji': '🫙', 'price': 890, 'mrp': 890, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Shaped Jars', 'img': '', 'description': 'Size: 9×9.5×4.5 cm'},
            {'product_id': 'jr5', 'name': 'Tulip Jar with Lid', 'emoji': '🌷', 'price': 1199, 'mrp': 1199, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Jars with Lid', 'img': '', 'description': 'Size: 9×9×8.2 cm'},
            {'product_id': 'jr6', 'name': 'Christmas Bauble with Lid', 'emoji': '🎄', 'price': 1279, 'mrp': 1279, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Jars with Lid', 'img': '', 'description': 'Size: 9.2×9.2×11 cm'},
            {'product_id': 'jr7', 'name': 'Plain Jar with Lid', 'emoji': '🫙', 'price': 1025, 'mrp': 1025, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Jars with Lid', 'img': '', 'description': 'Size: 9×9×7 cm'},
            {'product_id': 'jr8', 'name': 'Vase Jar', 'emoji': '🏺', 'price': 1028, 'mrp': 1028, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Shaped Jars', 'img': '', 'description': 'Size: 9.5×9.5×9.2 cm'},
        ],
    },
    'decor': {
        'name': 'Decor',
        'icon': '🏠',
        'filters': ['All', 'Office Accessories', 'Lighting', 'Clocks', 'Bookends'],
        'description': 'Home and office decor silicone molds — organizers, lamp stands, bookends, clocks and more.',
        'products': [
            {'product_id': 'dc1', 'name': 'Desk Organizer 1', 'emoji': '✏️', 'price': 950, 'mrp': 950, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Office Accessories', 'img': '', 'description': 'Size: 21×5×2.5 cm'},
            {'product_id': 'dc2', 'name': 'Desk Organizer 2', 'emoji': '✏️', 'price': 950, 'mrp': 950, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Office Accessories', 'img': '', 'description': 'Size: 20×8×2.5 cm'},
            {'product_id': 'dc3', 'name': 'Arch Table Lamp Stand', 'emoji': '💡', 'price': 920, 'mrp': 920, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Lighting', 'img': '', 'description': 'Size: 12×8×8.5 cm'},
            {'product_id': 'dc4', 'name': 'Arch Book Ends', 'emoji': '📚', 'price': 1530, 'mrp': 1530, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Bookends', 'img': '', 'description': 'Size: 13×11.5×4.5 cm'},
            {'product_id': 'dc5', 'name': 'Hexagon Clock', 'emoji': '🕐', 'price': 965, 'mrp': 965, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Clocks', 'img': '', 'description': 'Size: 10×11.5×3.5 cm'},
        ],
    },
}

BANNERS = [
    {'title': 'Premium Silicone Molds', 'subtitle': 'Craft candles, chocolates & more with precision-grade molds', 'cta_text': 'Shop Now', 'cta_link': '#', 'order': 1},
    {'title': 'Women & Figurine Molds', 'subtitle': 'Fashion figures, accessories & beauty-themed silicone molds', 'cta_text': 'Explore', 'cta_link': '#', 'order': 2},
    {'title': 'Festive Collection', 'subtitle': 'Diwali, Rakhi, Eid/Ramadan and all major festival molds', 'cta_text': 'View Festive', 'cta_link': '#', 'order': 3},
    {'title': 'Jar & Decor Molds', 'subtitle': 'Decorative jar, clock, bookend & lamp stand silicone molds', 'cta_text': 'Shop Decor', 'cta_link': '#', 'order': 4},
    {'title': 'Animals & Teddies', 'subtitle': 'Adorable teddy bear and rabbit molds for chocolates and candles', 'cta_text': 'Discover', 'cta_link': '#', 'order': 5},
]


class Command(BaseCommand):
    help = 'Seeds the database with the default OXFOX product catalog'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing products before seeding')

    def handle(self, *args, **options):
        if options['clear']:
            ProductImage.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
            Banner.objects.all().delete()
            self.stdout.write(self.style.WARNING('Cleared all existing data.'))

        created_cats = 0
        created_prods = 0
        created_imgs = 0

        for order_idx, (cat_key, cat_data) in enumerate(CATALOG.items(), start=1):
            cat, cat_created = Category.objects.update_or_create(
                key=cat_key,
                defaults={
                    'name': cat_data['name'],
                    'icon': cat_data['icon'],
                    'description': cat_data['description'],
                    'filters': cat_data.get('filters', []),
                    'order': order_idx,
                    'is_active': True,
                }
            )
            if cat_created:
                created_cats += 1

            for prod_data in cat_data['products']:
                badge = prod_data.get('badge') or ''
                prod, prod_created = Product.objects.update_or_create(
                    product_id=prod_data['product_id'],
                    defaults={
                        'category': cat,
                        'name': prod_data['name'],
                        'emoji': prod_data.get('emoji', '📦'),
                        'price': prod_data['price'],
                        'mrp': prod_data['mrp'],
                        'material': prod_data.get('material', 'Silicone'),
                        'badge': badge,
                        'filter_tag': prod_data.get('filter_tag', ''),
                        'description': prod_data['description'],
                        'is_active': True,
                        'discount': 0,
                    }
                )
                if prod_created:
                    created_prods += 1

                img_url = prod_data.get('img', '')
                if img_url:
                    _, img_created = ProductImage.objects.update_or_create(
                        product=prod, order=1,
                        defaults={'url': img_url}
                    )
                    if img_created:
                        created_imgs += 1

        created_banners = 0
        for banner_data in BANNERS:
            _, b_created = Banner.objects.update_or_create(
                order=banner_data['order'],
                defaults={**banner_data, 'is_active': True}
            )
            if b_created:
                created_banners += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done: {created_cats} categories, {created_prods} products, {created_imgs} images, {created_banners} banners created.'
        ))
        self.stdout.write(
            f'Totals: {Category.objects.count()} categories, {Product.objects.count()} products in DB.'
        )
