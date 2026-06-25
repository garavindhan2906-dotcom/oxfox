# OXFOX Backend — Setup Guide

## Requirements
- Python 3.10+
- MySQL 8.0+

## 1. Create MySQL Database

```sql
CREATE DATABASE oxfox_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'oxfox_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON oxfox_db.* TO 'oxfox_user'@'localhost';
FLUSH PRIVILEGES;
```

## 2. Configure Environment

Copy `.env.example` to `.env` and fill in your values:

```
SECRET_KEY=your-long-random-secret-key
DEBUG=True
DB_NAME=oxfox_db
DB_USER=oxfox_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

## 3. Install Dependencies

```bash
cd backend
python -m pip install -r requirements.txt
```

## 4. Run Migrations

```bash
python manage.py migrate
```

## 5. Create Admin Superuser

```bash
python manage.py createsuperuser
```

## 6. Seed Products (Optional)

```bash
python manage.py seed_products
```

This populates the database with all 55 default OXFOX products across 6 categories.  
Use `--clear` to wipe and re-seed: `python manage.py seed_products --clear`

## 7. Start the Server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/products/` | List all products |
| GET | `/api/products/?category=candles` | Products by category |
| GET | `/api/products/categories/` | List all categories |
| GET | `/api/products/categories/{key}/products/` | Products in a category |
| GET | `/api/products/new-arrivals/` | New arrival products |
| GET | `/api/products/bestsellers/` | Bestseller products |
| GET | `/api/products/banners/` | Active banner slides |
| POST | `/api/auth/register/` | Register new user |
| POST | `/api/auth/login/` | Login (returns JWT tokens) |
| GET | `/api/auth/me/` | Get current user info |
| PATCH | `/api/auth/me/` | Update profile |
| POST | `/api/auth/logout/` | Logout (blacklist token) |
| POST | `/api/analytics/track/` | Track page/product events |
| GET | `/api/analytics/dashboard/` | Analytics dashboard (admin) |
| POST | `/api/orders/` | Place an order |
| GET | `/api/orders/` | List user's orders |
| GET | `/api/orders/discounts/` | Get active category discounts |
| GET | `/api/orders/product-discounts/` | Get active per-product quantity discounts |
| GET | `/admin/` | Django admin panel |

---

## Frontend Integration

The frontend at `oxfox-studio.html` automatically:
- Tries to load extra products from the API on page load
- Sends analytics events to `/api/analytics/track/`
- Falls back to localStorage if the backend is unavailable

Change `API_BASE` in the frontend script if your server runs on a different port.
