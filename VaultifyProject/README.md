# Vaultify 🔒

**Vaultify** is a secure, personal digital vault web application built with Django. It provides users with an isolated and private workspace to securely manage personal notes, gallery images, and confidential documents with complete user data isolation and disk media cleanup upon deletion.

---

## 🌟 Key Features

- **🔐 Authentication & Access Control**
  - User Registration & Secure Password Hashing (Django `create_user`).
  - Login / Logout session management.
  - `@login_required` protected routes & dashboard navigation.

- **🛡️ Strict User Data Isolation**
  - Every note, image, and document is filtered strictly by `request.user`. Users can only access and delete their own vault items.

- **📝 Notes Vault**
  - Create, store, and manage personal rich notes.
  - Delete notes with instantaneous dashboard updates.

- **🖼️ Image Gallery Vault**
  - Upload custom images directly to secure media storage (powered by `Pillow`).
  - Interactive gallery grid showcasing titles and upload timestamps.
  - Physical file removal from storage when an image is deleted.

- **📄 Document Vault**
  - Upload personal documents (PDFs, DOCX, TXT, etc.).
  - Automatic fallback to original file name if custom title is omitted.
  - Clean filesystem deletion of stored files upon item deletion.

- **⚙️ Configurable Environment**
  - Dynamic loading of secret keys and app configurations via `.env` file powered by `python-dotenv`.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, Django 6.1.1
- **Database:** SQLite3 (Django ORM)
- **Media & File Processing:** Pillow
- **Environment Handling:** `python-dotenv`
- **Frontend:** HTML5, CSS3, JavaScript (Django Templates)

---

## 📁 Project Structure

```text
VaultifyProject/
│
├── VaultifyApp/                 # Main Django Application
│   ├── migrations/              # Database schema migrations
│   ├── admin.py                 # Django Admin register configs
│   ├── apps.py                  # App configuration
│   ├── models.py                # Database models (Note, Images, Documents)
│   ├── tests.py                 # Unit and integration tests
│   └── views.py                 # Business logic, vault handlers & security checks
│
├── VaultifyProject/             # Project Settings & Routing
│   ├── __init__.py
│   ├── asgi.py                  # ASGI deployment config
│   ├── settings.py              # Main project settings
│   ├── urls.py                  # Global URL pattern definitions
│   └── wsgi.py                  # WSGI deployment config
│
├── media/                       # Uploaded media root (vault_images/, vault_docs/)
├── static/                      # Static assets (CSS, JS, Images)
├── templates/                   # HTML Templates (dashboard, login, note, images, etc.)
│
├── .env.example                 # Environment variables template
├── db.sqlite3                   # Local SQLite database
├── manage.py                    # Django management script
└── requirements.txt             # Project python dependencies
```

---

## 🚀 Getting Started

Follow these instructions to set up and run the Vaultify project locally.

### 1. Prerequisites

Make sure you have installed:
- [Python 3.10+](https://www.python.org/downloads/)
- `pip` (Python package manager)

### 2. Clone the Repository & Navigate

```bash
git clone https://github.com/msinan22/Vaultify.git
cd Vaultify/VaultifyProject
```

### 3. Create & Activate a Virtual Environment

- **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```

- **Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

1. Copy `.env.example` to create `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your `DJANGO_SECRET_KEY`:
   ```env
   DJANGO_SECRET_KEY=your-custom-secret-key-here
   ```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional - Admin Portal Access)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📌 Available Routes

| URL Path | View Function | Access Level | Description |
| :--- | :--- | :--- | :--- |
| `/` | `login_view` | Public | User login page |
| `/register/` | `register_view` | Public | User registration page |
| `/logout/` | `logout_view` | Authenticated | Logs out user and destroys session |
| `/dashboard/` | `dashboard_view` | Authenticated | Main user dashboard summary |
| `/profile/` | `profile_view` | Authenticated | User profile management view |
| `/note/` | `notes_view` | Authenticated | Create & view private personal notes |
| `/images/` | `image_gallery` | Authenticated | Upload & view vault image gallery |
| `/documents/` | `documents_view` | Authenticated | Upload & view confidential documents |
| `/dashboard/notes/delete/<id>/` | `delete_note_view` | Authenticated | Delete a specific note |
| `/dashboard/images/delete/<id>/` | `delete_image` | Authenticated | Delete image (database entry & file on disk) |
| `/dashboard/documents/delete/<id>/` | `delete_document_view` | Authenticated | Delete document (database entry & file on disk) |
| `/admin/` | `admin.site.urls` | Admin / Superuser | Django administration portal |

---

## 🔒 Security Measures

- **Data Privacy:** Users can only query, modify, or delete records associated with their `request.user` ID.
- **Physical File Removal:** Deleting image/document assets explicitly triggers filesystem cleanup (`file.delete()`, `os.remove()`) to prevent orphaned files on disk.
- **Environment Isolation:** Secrets are kept out of source code by retrieving values dynamically via `python-dotenv`.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an Issue or submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.
