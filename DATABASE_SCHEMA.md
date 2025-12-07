# NerdHub Database Schema

This document describes the database structure for the NerdHub e-commerce platform. This schema should be used when setting up the database on Railway with PostgreSQL.

## Database Technology
- **Local Development**: SQLite
- **Production (Railway)**: PostgreSQL

## Tables Structure

### 1. Authentication Tables (Django Built-in)

#### `auth_user`
Stores user account information.

```sql
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL
);
```

#### `auth_group`
Stores user groups.

```sql
CREATE TABLE auth_group (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL
);
```

#### `auth_user_groups`
Many-to-many relationship between users and groups.

```sql
CREATE TABLE auth_user_groups (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id),
    group_id INTEGER REFERENCES auth_group(id),
    UNIQUE (user_id, group_id)
);
```

#### `auth_permission`
Stores permissions.

```sql
CREATE TABLE auth_permission (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    content_type_id INTEGER NOT NULL,
    codename VARCHAR(100) NOT NULL,
    UNIQUE (content_type_id, codename)
);
```

#### `auth_group_permissions`
Many-to-many relationship between groups and permissions.

```sql
CREATE TABLE auth_group_permissions (
    id SERIAL PRIMARY KEY,
    group_id INTEGER REFERENCES auth_group(id),
    permission_id INTEGER REFERENCES auth_permission(id),
    UNIQUE (group_id, permission_id)
);
```

#### `auth_user_user_permissions`
Many-to-many relationship between users and permissions.

```sql
CREATE TABLE auth_user_user_permissions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES auth_user(id),
    permission_id INTEGER REFERENCES auth_permission(id),
    UNIQUE (user_id, permission_id)
);
```

### 2. Content Types Table

#### `django_content_type`
Tracks Django models for permissions.

```sql
CREATE TABLE django_content_type (
    id SERIAL PRIMARY KEY,
    app_label VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    UNIQUE (app_label, model)
);
```

### 3. Sessions Table

#### `django_session`
Stores user session data.

```sql
CREATE TABLE django_session (
    session_key VARCHAR(40) PRIMARY KEY,
    session_data TEXT NOT NULL,
    expire_date TIMESTAMP WITH TIME ZONE NOT NULL
);
```

### 4. Admin Log Table

#### `django_admin_log`
Records admin actions.

```sql
CREATE TABLE django_admin_log (
    id SERIAL PRIMARY KEY,
    action_time TIMESTAMP WITH TIME ZONE NOT NULL,
    object_id TEXT,
    object_repr VARCHAR(200) NOT NULL,
    action_flag SMALLINT NOT NULL,
    change_message TEXT NOT NULL,
    content_type_id INTEGER REFERENCES django_content_type(id),
    user_id INTEGER REFERENCES auth_user(id) NOT NULL
);
```

### 5. Application Tables (Painel App)

#### `painel_category`
Stores product categories.

```sql
CREATE TABLE painel_category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    slug VARCHAR(50) UNIQUE NOT NULL
);
```

#### `painel_product`
Stores product information.

```sql
CREATE TABLE painel_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT NOT NULL,
    main_image VARCHAR(100),
    stock INTEGER NOT NULL CHECK (stock >= 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category_id INTEGER REFERENCES painel_category(id),
    sku VARCHAR(50) UNIQUE,
    brand VARCHAR(100),
    model VARCHAR(100),
    dimensions VARCHAR(100),
    weight DECIMAL(8, 2),
    materials VARCHAR(200),
    colors VARCHAR(200),
    main_features TEXT,
    package_contents TEXT
);
```

#### `painel_productimage`
Stores additional product images.

```sql
CREATE TABLE painel_productimage (
    id SERIAL PRIMARY KEY,
    image VARCHAR(100) NOT NULL,
    product_id INTEGER REFERENCES painel_product(id) ON DELETE CASCADE
);
```

## Railway PostgreSQL Setup Instructions

1. **Create a PostgreSQL Database on Railway:**
   - Go to your Railway dashboard
   - Click "New Project"
   - Select "Provision PostgreSQL"
   - Wait for the database to be provisioned

2. **Configure Environment Variables:**
   Add these environment variables to your Railway application:
   
   ```
   DATABASE_URL=postgresql://username:password@host:port/database_name
   DJANGO_SECRET_KEY=your_secret_key_here
   DJANGO_ALLOWED_HOSTS=your-domain.railway.app,localhost
   DEBUG=false
   ```

3. **Update Django Settings:**
   The `settings.py` file is already configured to work with PostgreSQL when deployed to Railway.

4. **Run Migrations:**
   After deploying, run these commands in the Railway console:
   
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

5. **Create Superuser:**
   Create an admin user:
   
   ```bash
   python manage.py createsuperuser
   ```

## Notes

- The database schema will be automatically created when you run migrations
- File paths for images are stored as strings in the database
- All timestamp fields use timezone-aware datetimes
- Foreign key relationships use appropriate ON DELETE behaviors
- String length limits match the Django model definitions
- Decimal precision is optimized for currency and weights

This schema represents the current state of your Django application and should be used as a reference when setting up your Railway deployment.