from django.contrib import admin
from django.urls import path
from VaultifyApp import views # Importing the whole views file makes it cleaner
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile_view,name='profile'),
    path('note/',views.notes_view,name='note'),
    path('images/', views.image_gallery, name='image_gallery'),
    path('dashboard/images/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('documents/', views.documents_view, name='documents'),
    path('dashboard/notes/delete/<int:note_id>/', views.delete_note_view, name='delete_note'),
    path('dashboard/documents/delete/<int:doc_id>/', views.delete_document_view, name='delete_document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)