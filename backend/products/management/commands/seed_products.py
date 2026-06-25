"""
Management command: seed_products
Run: python manage.py seed_products
"""
from django.core.management.base import BaseCommand
from products.models import Category, Product, ProductImage, Banner

CATALOG = {
    'candles': {
        'name': 'Candle Molds',
        'icon': '🕯️',
        'filters': ['All','Festive / Holiday','Flower','Teddy Bear','Birds & Animal','Foliage','Ornamental Patterns','Taper Candle','Pillar Candle','Alphabet','Number'],
        'description': 'Premium food-grade silicone molds for crafting pillar, taper, geometric, floral, and novelty candles of all sizes.',
        'products': [
            {'product_id': 'cn1', 'name': 'Pillar Candle Molds', 'emoji': '🕯️', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Pillar Candle', 'img': 'https://images.unsplash.com/photo-1602252253699-94778ce98c2d?w=600&q=75', 'description': 'Classic pillar candle silicone molds in round, square, and oval profiles. Heat-resistant, multiple heights available.'},
            {'product_id': 'cn2', 'name': 'Taper Candle Molds', 'emoji': '🕯️', 'price': 549, 'mrp': 699, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Taper Candle', 'img': 'https://images.unsplash.com/photo-1604480132736-44c188fe4d20?w=600&q=75', 'description': 'Elegant tapered candle molds in classic and twisted styles. Heat-resistant silicone with easy demold release.'},
            {'product_id': 'cn3', 'name': 'Geometric Candle Molds', 'emoji': '🔷', 'price': 849, 'mrp': 1099, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600&q=75', 'description': 'Trendy geometric candle molds — hexagonal, cube, pyramid, and diamond shapes for modern home decor.'},
            {'product_id': 'cn4', 'name': 'Floral Candle Molds', 'emoji': '🌸', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Flower', 'img': 'https://images.unsplash.com/photo-1589881334099-8dfea2a8b6e5?w=600&q=75', 'description': 'Intricate floral and botanical candle molds capturing petals, leaves, and blooms in fine surface detail.'},
            {'product_id': 'cn5', 'name': 'Sphere Candle Molds', 'emoji': '⚪', 'price': 649, 'mrp': 849, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Pillar Candle', 'img': 'https://images.unsplash.com/photo-1545930731-64d1e3b4ff9c?w=600&q=75', 'description': 'Perfect-sphere and half-sphere candle molds in multiple sizes. Ideal for luxury ball candle collections.'},
            {'product_id': 'cn6', 'name': 'Column Candle Molds', 'emoji': '🏛️', 'price': 599, 'mrp': 799, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Pillar Candle', 'img': 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=600&q=75', 'description': 'Tall column and tower candle molds with smooth and ribbed surface textures for statement pieces.'},
            {'product_id': 'cn7', 'name': 'Tea Light Molds', 'emoji': '🕯️', 'price': 449, 'mrp': 599, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Pillar Candle', 'img': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600&q=75', 'description': 'Multi-cavity tea light candle molds. Standard 38mm diameter cavity, 12 or 24 per sheet.'},
            {'product_id': 'cn8', 'name': 'Novelty Shape Molds', 'emoji': '⭐', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1571818765-e3e3c44ece1e?w=600&q=75', 'description': 'Fun novelty candle molds — stars, hearts, animals, and seasonal shapes perfect for gifting and events.'},
        ],
    },
    'candlejars': {
        'name': 'Candle Jar Molds',
        'icon': '🫙',
        'filters': ['All','Round','Square','Hexagonal','Faceted','Apothecary','Tumbler','Wide-Mouth'],
        'description': 'High-clarity silicone molds for crafting decorative candle jars, containers, and wax vessels in any style.',
        'products': [
            {'product_id': 'cj1', 'name': 'Round Jar Molds', 'emoji': '🫙', 'price': 899, 'mrp': 1199, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Round', 'img': 'https://images.unsplash.com/photo-1601049676869-702ea24cfd58?w=600&q=75', 'description': 'Classic round candle jar silicone molds in 4oz, 8oz, and 12oz capacities. Smooth interior finish.'},
            {'product_id': 'cj2', 'name': 'Square Jar Molds', 'emoji': '⬜', 'price': 849, 'mrp': 1099, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Square', 'img': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=75', 'description': 'Modern square and rectangular candle container molds. Sharp corners and flat base for professional results.'},
            {'product_id': 'cj3', 'name': 'Hexagonal Jar Molds', 'emoji': '⬡', 'price': 999, 'mrp': 1299, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Hexagonal', 'img': 'https://images.unsplash.com/photo-1569569970363-df7b6160d111?w=600&q=75', 'description': 'Trendy hexagonal jar molds for candles and wax melts. Six-sided geometry, multiple heights.'},
            {'product_id': 'cj4', 'name': 'Faceted Crystal Jar Molds', 'emoji': '💎', 'price': 1199, 'mrp': 1499, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Faceted', 'img': 'https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?w=600&q=75', 'description': 'Crystal-faceted jar molds with multi-angle flat surfaces. Creates a gemstone-like appearance when filled.'},
            {'product_id': 'cj5', 'name': 'Apothecary Jar Molds', 'emoji': '🧪', 'price': 1099, 'mrp': 1399, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Apothecary', 'img': 'https://images.unsplash.com/photo-1550159930-40066082a4fc?w=600&q=75', 'description': 'Vintage apothecary and pharmacy-inspired jar molds with wide mouth and slight taper design.'},
            {'product_id': 'cj6', 'name': 'Tumbler Molds', 'emoji': '🥃', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Tumbler', 'img': 'https://images.unsplash.com/photo-1607363309071-c2de9e59e9f2?w=600&q=75', 'description': 'Straight-sided tumbler and drinking glass shaped candle molds in 6oz, 9oz, and 12oz sizes.'},
            {'product_id': 'cj7', 'name': 'Wide-Mouth Bowl Molds', 'emoji': '🍵', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Wide-Mouth', 'img': 'https://images.unsplash.com/photo-1518972559570-7cc1309f3229?w=600&q=75', 'description': 'Wide-mouth bowl and tin-style candle molds for decorative container candles and wax melts.'},
        ],
    },
    'chocolates': {
        'name': 'Chocolate Molds',
        'icon': '🍫',
        'filters': ['All','Festive / Holiday','Flower','Teddy Bear','Birds & Animal','Foliage','Ornamental Patterns','Slab','Alphabet','Number'],
        'description': 'High-gloss polycarbonate and food-grade silicone molds for artisan chocolates, pralines, truffles, and confectionery.',
        'products': [
            {'product_id': 'ch1', 'name': 'Chocolate Bar Molds', 'emoji': '🍫', 'price': 1299, 'mrp': 1699, 'material': 'Polycarbonate', 'badge': 'best', 'filter_tag': 'Slab', 'img': 'https://images.unsplash.com/photo-1481391243133-f96216dcb5d2?w=600&q=75', 'description': 'Classic and custom-break chocolate bar molds. High-gloss polycarbonate for mirror-finish chocolates.'},
            {'product_id': 'ch2', 'name': 'Bonbon & Praline Molds', 'emoji': '🍬', 'price': 1499, 'mrp': 1899, 'material': 'Polycarbonate', 'badge': 'best', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1548365328-8c6db3220e4c?w=600&q=75', 'description': 'Professional bonbon and praline molds in round, oval, and square cavities.'},
            {'product_id': 'ch3', 'name': 'Truffle Molds', 'emoji': '🫘', 'price': 899, 'mrp': 1199, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1571819358766-df571eeff0b3?w=600&q=75', 'description': 'Round and half-sphere truffle molds for hand-rolled and molded chocolate truffles.'},
            {'product_id': 'ch4', 'name': 'Chocolate Tablet Molds', 'emoji': '🟫', 'price': 749, 'mrp': 999, 'material': 'Polycarbonate', 'badge': '', 'filter_tag': 'Slab', 'img': 'https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=600&q=75', 'description': 'Flat chocolate tablet and bark molds with textured surfaces — geometric, floral, and abstract patterns.'},
            {'product_id': 'ch5', 'name': 'Lollipop Molds', 'emoji': '🍭', 'price': 649, 'mrp': 849, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1582750433449-648ed127bb54?w=600&q=75', 'description': 'Chocolate lollipop molds with integrated stick channel. Round, heart, and star cavities. 12-cavity sheets.'},
            {'product_id': 'ch6', 'name': 'Chocolate Letter Molds', 'emoji': '🔤', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Alphabet', 'img': 'https://images.unsplash.com/photo-1621939514649-280e2ee25f60?w=600&q=75', 'description': 'Full alphabet and number chocolate letter molds. Personalise messages in chocolate for gifting.'},
            {'product_id': 'ch7', 'name': 'Filled Chocolate Molds', 'emoji': '🍮', 'price': 1199, 'mrp': 1499, 'material': 'Polycarbonate', 'badge': '', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=600&q=75', 'description': 'Two-part filled chocolate shell molds for ganache, caramel, and nut-filled chocolates.'},
            {'product_id': 'ch8', 'name': 'Mini Chocolate Molds', 'emoji': '✨', 'price': 549, 'mrp': 699, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1599599810769-bcde5a160d32?w=600&q=75', 'description': 'Multi-cavity mini chocolate and candy molds — bite-size hearts, stars, coins, and seasonal shapes.'},
            {'product_id': 'ch9', 'name': "Men's Gym Set - Silicone Mold", 'emoji': '💪', 'price': 730, 'mrp': 730, 'material': 'Food-grade Silicone', 'badge': 'new', 'filter_tag': 'Ornamental Patterns', 'img': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=600&q=75', 'description': "Premium food-grade silicone mold set for gym-themed chocolates. 1 mold with 6 unique gym equipment designs per set. Size: 3.6cm x 1.6cm depth. Perfect for fitness brands, gifting, and sports events."},
        ],
    },
    'decor': {
        'name': 'Home & Office Decor Molds',
        'icon': '🏠',
        'filters': ['All','Frames','Vases','Trays','Organizers','Coasters','Wall Art','Clocks','Bookends'],
        'description': 'Premium silicone molds for crafting decorative home and office pieces — trays, frames, vases, and more.',
        'products': [
            {'product_id': 'd1', 'name': 'Picture Frame Molds', 'emoji': '🖼️', 'price': 999, 'mrp': 1299, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Frames', 'img': 'https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=600&q=75', 'description': 'Decorative picture frame molds in classic and ornate styles for resin and concrete casting.'},
            {'product_id': 'd2', 'name': 'Vase & Planter Molds', 'emoji': '🏺', 'price': 1299, 'mrp': 1699, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Vases', 'img': 'https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=600&q=75', 'description': 'Elegant vase and planter molds in round, tapered, and geometric shapes for concrete and resin.'},
            {'product_id': 'd3', 'name': 'Decorative Tray Molds', 'emoji': '🍽️', 'price': 1199, 'mrp': 1499, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Trays', 'img': 'https://images.unsplash.com/photo-1567016432779-094069958ea5?w=600&q=75', 'description': 'Large decorative serving tray molds in rectangular and oval shapes with smooth or textured finish.'},
            {'product_id': 'd4', 'name': 'Pen & Desk Organizer Molds', 'emoji': '✏️', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Organizers', 'img': 'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600&q=75', 'description': 'Desk organizer and pen holder molds for concrete and resin. Round, square, and honeycomb designs.'},
            {'product_id': 'd5', 'name': 'Coaster Molds', 'emoji': '☕', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Coasters', 'img': 'https://images.unsplash.com/photo-1534430794739-5bd31157b65b?w=600&q=75', 'description': 'Round, square, and hexagonal coaster molds. 4mm cavity depth, 10-12cm diameter. Set of 4.'},
            {'product_id': 'd6', 'name': 'Wall Art Panel Molds', 'emoji': '🎨', 'price': 1499, 'mrp': 1899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Wall Art', 'img': 'https://images.unsplash.com/photo-1526312426976-c539d67c6d67?w=600&q=75', 'description': 'Abstract and geometric wall art panel molds for resin pours and concrete casting.'},
            {'product_id': 'd7', 'name': 'Clock Face Molds', 'emoji': '🕐', 'price': 1099, 'mrp': 1399, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Clocks', 'img': 'https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=600&q=75', 'description': 'Round clock face molds for concrete and resin with mechanism hole. Roman numeral and minimalist styles.'},
            {'product_id': 'd8', 'name': 'Bookend Molds', 'emoji': '📚', 'price': 899, 'mrp': 1199, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Bookends', 'img': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=600&q=75', 'description': 'Matched-pair bookend molds in geometric, animal, and abstract designs for concrete and resin.'},
        ],
    },
    'concrete': {
        'name': 'Concrete / Jesmonite / Eco Resin Molds',
        'icon': '🏺',
        'filters': ['All','Festive / Holiday','Candle Jar','Candle Holder','Bowl','Tray','Plant Pots','Incense Holder','Diffuser','Ornamental Novelty','Coaster','Lamp Base','Clock','Tealight Holder','Office Accessory','Vase','Rangoli'],
        'description': 'Premium silicone molds engineered for concrete, jesmonite, and eco-resin — candle jars, holders, bowls, trays, plant pots, incense holders, coasters, and more.',
        'products': [
            {'product_id': 'co1', 'name': 'Candle Jar Molds', 'emoji': '🫙', 'price': 899, 'mrp': 1199, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Candle Jar', 'img': 'https://images.unsplash.com/photo-1589401494341-3df7d24a1cf4?w=600&q=75', 'description': 'Round, square, and hexagonal candle jar molds — ideal for concrete and jesmonite vessels.'},
            {'product_id': 'co2', 'name': 'Candle Holder Molds', 'emoji': '🕯️', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Candle Holder', 'img': 'https://images.unsplash.com/photo-1590439471364-192aa70c0b53?w=600&q=75', 'description': 'Pillar and tealight holder molds for concrete and resin. Multiple sizes and cavity depths.'},
            {'product_id': 'co3', 'name': 'Bowl Molds', 'emoji': '🥣', 'price': 1099, 'mrp': 1399, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Bowl', 'img': 'https://images.unsplash.com/photo-1577083552431-6e5fd01988ec?w=600&q=75', 'description': 'Deep and shallow bowl molds for concrete jesmonite casting. Smooth interior finish.'},
            {'product_id': 'co4', 'name': 'Tray Molds', 'emoji': '🍽️', 'price': 1199, 'mrp': 1499, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Tray', 'img': 'https://images.unsplash.com/photo-1445462870255-0c2d7b2a5fc0?w=600&q=75', 'description': 'Rectangular and oval decorative tray molds for concrete and resin with smooth or textured base.'},
            {'product_id': 'co5', 'name': 'Plant Pot Molds', 'emoji': '🪴', 'price': 999, 'mrp': 1299, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Plant Pots', 'img': 'https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=75', 'description': 'Round and faceted plant pot molds for concrete and resin. Multiple heights with drainage slot.'},
            {'product_id': 'co6', 'name': 'Incense Holder Molds', 'emoji': '🪔', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Incense Holder', 'img': 'https://images.unsplash.com/photo-1604014237800-1c9102c219da?w=600&q=75', 'description': 'Incense stick and cone holder molds in minimalist and ornamental designs for concrete.'},
            {'product_id': 'co7', 'name': 'Diffuser Molds', 'emoji': '🌿', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Diffuser', 'img': 'https://images.unsplash.com/photo-1595341888016-a392ef81b7de?w=600&q=75', 'description': 'Reed diffuser base molds for concrete and resin. Sleek, weighted profiles.'},
            {'product_id': 'co8', 'name': 'Coaster Molds', 'emoji': '☕', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Coaster', 'img': 'https://images.unsplash.com/photo-1560185892-5b0f0be3e741?w=600&q=75', 'description': 'Round, square, and hexagonal coaster molds for concrete, resin, and jesmonite.'},
            {'product_id': 'co9', 'name': 'Lamp Base Molds', 'emoji': '💡', 'price': 1499, 'mrp': 1899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Lamp Base', 'img': 'https://images.unsplash.com/photo-1540932239986-30128078f3c5?w=600&q=75', 'description': 'Tall and wide lamp base molds for concrete casting with cord channel.'},
            {'product_id': 'co10', 'name': 'Clock Face Molds', 'emoji': '🕐', 'price': 1099, 'mrp': 1399, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Clock', 'img': 'https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=600&q=75', 'description': 'Round clock face molds with mechanism hole for concrete and resin — roman numeral and minimalist.'},
            {'product_id': 'co11', 'name': 'Tealight Holder Molds', 'emoji': '🕯️', 'price': 649, 'mrp': 849, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Tealight Holder', 'img': 'https://images.unsplash.com/photo-1602252253699-94778ce98c2d?w=600&q=75', 'description': 'Multi-cavity tealight holder molds for concrete and resin. Standard 38mm cavity.'},
            {'product_id': 'co12', 'name': 'Office Accessory Molds', 'emoji': '✏️', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Office Accessory', 'img': 'https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=600&q=75', 'description': 'Pen holders, phone stands, and desk organizer molds for concrete and resin.'},
            {'product_id': 'co13', 'name': 'Vase Molds', 'emoji': '🏺', 'price': 1299, 'mrp': 1699, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Vase', 'img': 'https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=600&q=75', 'description': 'Tall and short vase molds in round, tapered, and geometric shapes for concrete and resin.'},
            {'product_id': 'co14', 'name': 'Rangoli Pattern Molds', 'emoji': '🎨', 'price': 849, 'mrp': 1099, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'Rangoli', 'img': 'https://images.unsplash.com/photo-1597733336794-12d05021d510?w=600&q=75', 'description': 'Traditional and modern rangoli pattern molds for resin casting — perfect for festival decor.'},
        ],
    },
    'festive': {
        'name': 'Festive / Holiday Molds',
        'icon': '🎊',
        'filters': ['All',"Makar Sankranti","Valentine's Day",'Holi','Ramadan',"Mother's Day",'Rakhi',"Father's Day","Teacher's Day",'Ganesh Chaturthi','Diwali','Christmas','New Year'],
        'description': "Seasonal silicone molds for all major Indian and international festivals — Diwali, Christmas, Valentine's Day, Holi, Rakhi, and more.",
        'products': [
            {'product_id': 'fv1', 'name': 'Makar Sankranti / Lohri Molds', 'emoji': '🪁', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Makar Sankranti', 'img': 'https://images.unsplash.com/photo-1540820658029-a71bcbb29a36?w=600&q=75', 'description': 'Kite, sesame, and traditional motif molds for Makar Sankranti and Lohri celebrations.'},
            {'product_id': 'fv2', 'name': "Valentine's Day Molds", 'emoji': '❤️', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': 'best', 'filter_tag': "Valentine's Day", 'img': 'https://images.unsplash.com/photo-1518895312237-a9e23508077d?w=600&q=75', 'description': "Heart, rose, and love-themed chocolate and candle molds for Valentine's Day gifting."},
            {'product_id': 'fv3', 'name': 'Holi Molds', 'emoji': '🌈', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Holi', 'img': 'https://images.unsplash.com/photo-1519681393784-d120267933ba?w=600&q=75', 'description': 'Pichkari, flower, and rang motif molds for Holi-themed chocolates and candles.'},
            {'product_id': 'fv4', 'name': 'Ramadan / Eid Molds', 'emoji': '🌙', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Ramadan', 'img': 'https://images.unsplash.com/photo-1584543427661-7e5c0f9b99ab?w=600&q=75', 'description': 'Crescent, star, and lantern motif molds for Ramadan and Eid celebrations.'},
            {'product_id': 'fv5', 'name': "Mother's Day Molds", 'emoji': '💐', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': "Mother's Day", 'img': 'https://images.unsplash.com/photo-1589881334099-8dfea2a8b6e5?w=600&q=75', 'description': "Floral, heart, and love-themed molds for Mother's Day chocolates, candles, and soaps."},
            {'product_id': 'fv6', 'name': 'Rakhi Molds', 'emoji': '🪢', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Rakhi', 'img': 'https://images.unsplash.com/photo-1601314912309-2a1e0a02bd4f?w=600&q=75', 'description': 'Rakhi and thread motif molds for brother-sister festival chocolates and sweets.'},
            {'product_id': 'fv7', 'name': "Father's Day Molds", 'emoji': '👔', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': "Father's Day", 'img': 'https://images.unsplash.com/photo-1530748030476-7e7bb8e24519?w=600&q=75', 'description': "Tie, moustache, and star motif molds for Father's Day gifting."},
            {'product_id': 'fv8', 'name': "Teacher's Day Molds", 'emoji': '📚', 'price': 699, 'mrp': 899, 'material': 'Silicone', 'badge': '', 'filter_tag': "Teacher's Day", 'img': 'https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=600&q=75', 'description': "Apple, pencil, and book motif molds for Teacher's Day chocolate gifts."},
            {'product_id': 'fv9', 'name': 'Ganesh Chaturthi Molds', 'emoji': '🐘', 'price': 849, 'mrp': 1099, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Ganesh Chaturthi', 'img': 'https://images.unsplash.com/photo-1603475518949-a8c4e5800c65?w=600&q=75', 'description': 'Ganesha and modak motif molds for Ganesh Chaturthi celebrations and prasad.'},
            {'product_id': 'fv10', 'name': 'Diwali Molds', 'emoji': '🪔', 'price': 849, 'mrp': 1099, 'material': 'Silicone', 'badge': 'best', 'filter_tag': 'Diwali', 'img': 'https://images.unsplash.com/photo-1574126154517-d1e0d89ef734?w=600&q=75', 'description': 'Diya, lotus, and firecracker motif molds for Diwali chocolates, candles, and sweets.'},
            {'product_id': 'fv11', 'name': 'Christmas Molds', 'emoji': '🎄', 'price': 799, 'mrp': 999, 'material': 'Silicone', 'badge': '', 'filter_tag': 'Christmas', 'img': 'https://images.unsplash.com/photo-1543598832-1cf9c98d43e8?w=600&q=75', 'description': 'Christmas tree, Santa, snowflake, and bell molds for festive chocolates and candles.'},
            {'product_id': 'fv12', 'name': "New Year's Day Molds", 'emoji': '🎆', 'price': 749, 'mrp': 999, 'material': 'Silicone', 'badge': 'new', 'filter_tag': 'New Year', 'img': 'https://images.unsplash.com/photo-1546587348-d12660c30c50?w=600&q=75', 'description': 'Champagne, star, and celebration motif molds for New Year chocolates and candle gifting.'},
        ],
    },
}

BANNERS = [
    {'title': 'Premium Silicone Molds', 'subtitle': 'Craft candles, chocolates & more with precision-grade molds', 'cta_text': 'Shop Now', 'cta_link': '#', 'order': 1},
    {'title': 'Chocolate Molds', 'subtitle': 'High-gloss polycarbonate & food-grade silicone for artisan confectionery', 'cta_text': 'Explore', 'cta_link': '#', 'order': 2},
    {'title': 'Candle Molds', 'subtitle': 'Pillar, taper, geometric, and floral designs — heat-resistant silicone', 'cta_text': 'Shop Candles', 'cta_link': '#', 'order': 3},
    {'title': 'Festive Collection', 'subtitle': "Diwali, Christmas, Valentine's Day and all major festival molds", 'cta_text': 'View Festive', 'cta_link': '#', 'order': 4},
    {'title': 'Concrete & Resin Molds', 'subtitle': 'Bowls, trays, vases, and home decor in premium silicone', 'cta_text': 'Discover', 'cta_link': '#', 'order': 5},
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
