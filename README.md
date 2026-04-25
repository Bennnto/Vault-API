# Vault-API

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Usage Examples](#usage-examples)

### Overview
Vault API is a RESTful API for document management with filtering function and user authentication. It provides a secure, scalable platform for individuals to store, organize, and retrieve important documents and data. Built with Django REST Framework, it offers a modern RESTful API and secure user access by JWT (JSON Web Token) authentication, real-time filtering capabilities, CRUD (Create, Read, Update, Delete) interface that ease of use for managing items/data in storage and oranizing items/data with tagging system.


### Features 
- 📄 **Document Storage** - Upload and store files (images, PDFs, documents)
- 🏷️ **Tag Management** - Organize documents with custom tags
- 🔐 **User Authentication** - JWT token-based authentication
- 🔍 **Advanced Filtering** - Filter documents by tags
- 📱 **RESTful API** - Clean and intuitive API endpoints
- 📚 **Interactive API Docs** - Scalar API Reference documentation
- 🎨 **Customizable Theme** - Dark/Light/Kepler theme support
- 📤 **File Upload** - Secure file uploads with size validation (10MB limit)

### Tech Stack
 **Django** 6.0.4
- **Django REST Framework** (DRF)
- **Python** 3.14+
- **SQLite3** (Database)
- **JWT Authentication** (rest_framework_simplejwt)
- **Scalar** (API Documentation)
- **django-filter** (Advanced Filtering)

#### Dependencies 
```
Django==6.0.4
djangorestframework==3.14.0
django-filter==23.5
drf-spectacular==0.27.0
rest_framework_simplejwt==5.3.0
Pillow==10.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

### API Endpoints

#### Authentication
- `POST /api/token/` - Get JWT tokens (email & password)
- `POST /api/token/refresh/` - Refresh access token

#### Storage (Documents)
- `POST /api/storage/create_storage/` - Create a new document
- `GET /api/storage/get_storage/` - List all documents (filtered by user)
- `GET /api/storage/get_storage_id/` - Get a specific document by ID
- `PATCH /api/storage/update_storage/` - Update a document
- `DELETE /api/storage/delete_storage/` - Delete a document

#### Tags
- `POST /api/tags/create_tag/` - Create a new tag
- `GET /api/tags/list_all_tag/` - List all tags
- `GET /api/tags/get_tag_by_id/` - Get a specific tag
- `PATCH /api/tags/update_tag/` - Update a tag
- `DELETE /api/tags/delete_tag/` - Delete a tag


