# NerdHub - E-commerce Platform

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-5.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

NerdHub is a modern e-commerce platform built with Django, designed for selling tech products and geek merchandise. The platform features a complete administrative panel for product management, user management, and order processing.

## 🚀 Features

### Customer Frontend
- Responsive design for all devices
- Product catalog with detailed views
- Shopping cart functionality
- User authentication and profiles
- About and support pages

### Administrative Panel
- **Product Management**
  - Create, edit, and delete products
  - Manage product categories
  - Upload product images (main and gallery)
  - Set pricing and inventory levels
  - Detailed product specifications (brand, model, dimensions, etc.)
  - Unique SKU generation for easy product identification
  
- **User Management**
  - View and manage customer accounts
  - Admin user permissions
  
- **Order Management**
  - Track and process customer orders
  - Order status management

- **Dashboard**
  - Sales analytics and reporting
  - Key metrics visualization

## 🛠️ Tech Stack

- **Backend**: Django 5.2
- **Database**: SQLite (local), PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Tailwind CSS, JavaScript
- **Deployment**: Railway.app
- **Static Files**: WhiteNoise
- **Web Server**: Gunicorn

## 📁 Project Structure

```
nerdhub/
├── nerdhub/           # Main project settings
├── nucleo/            # Core frontend application
├── painel/            # Administrative panel application
├── TPU-DPS/           # Design prototypes and layouts
├── staticfiles/       # Static assets
├── media/             # Uploaded media files
├── requirements.txt   # Python dependencies
├── Procfile           # Deployment configuration
└── runtime.txt        # Python runtime version
```

## 🎯 Product Editing Features

The product editing interface includes:

### Product Information
- **Title**: Product name
- **Gallery**: Main image and additional photos
- **Main Information & Price**: Core product details and pricing
- **Detailed Technical Specifications**: Comprehensive specs in bullet points
- **Commercial Description**: Persuasive product copy
- **Unique Identification Code**: SKU for quick search

### Gallery Requirements
- **Main Image**: Primary product showcase (in use or isolated with neutral background)
- **Secondary Images**:
  - Different angles of the product
  - Close-ups of important details, materials, or textures
  - Product in use (when applicable)
  - Specification labels or tags
  - Dimension scales (with common objects for reference)

### Mandatory Information
- **Category**: Hierarchical classification (e.g., Electronics > Smartphones > iPhone)
- **Brand**: Manufacturer name (e.g., Apple, Samsung, Nike)
- **Detailed Technical Specifications**:
  - Model
  - Dimensions (Height × Width × Depth / Weight)
  - Construction materials
  - Available colors
  - Main features
  - Package contents
  - Industry-specific specs (driver, frequency, impedance for headphones; fabric composition for clothing)

### Unique Identification Code
- **Purpose**: Alphanumeric code for unambiguous product identification
- **Format**: `[BRAND_ABBREVIATION]-[CATEGORY_ABBREVIATED]-[UNIQUE_NUMBER]`
- **Example**: `APP-SMART-15PRO-256-AZ` (iPhone 15 Pro 256GB Blue)
- **Visibility**: Clearly displayed with "Reference Code" title and note: "Use this code in the search field to find this product quickly."

## 🚀 Getting Started

### Prerequisites
- Python 3.12
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nerdhub.git
cd nerdhub
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

### Access Points
- **Frontend**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Custom Panel**: http://127.0.0.1:8000/painel/

## 🌐 Deployment

The application is configured for deployment on Railway.app:

1. Connect your GitHub repository to Railway
2. Set environment variables:
   - `DJANGO_SECRET_KEY`: Your Django secret key
   - `DJANGO_ALLOWED_HOSTS`: Your domain names
   - `DEBUG`: Set to "false" for production

3. During deployment, Railway will automatically:
   - Execute the release phase which handles:
     - Database migrations
     - Static file collection
   - Start the web server using the Procfile

## 🔧 Troubleshooting

### Database Migration Issues
If you encounter "no such table" errors:
1. Ensure migrations have been run: `python manage.py migrate`
2. Check that the release phase in Procfile is being executed during deployment

### Authentication Flow
- Regular users logging in through `/painel/login/` will be redirected to the main site
- Admin/staff users will be redirected to the administrative panel

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Development Team** - *Initial work*

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## 🆘 Support

For support, email support@nerdhub.com or open an issue in the repository.