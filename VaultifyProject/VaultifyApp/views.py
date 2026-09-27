import os

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Note, Images, Documents

def register_view(request):
    if request.method == 'POST':
        username_data = request.POST.get('username')
        password_data = request.POST.get('password')

    
        if User.objects.filter(username=username_data).exists():
             messages.error(request, "That username is already taken!")
             return render(request, 'register.html')
        
        # Create and save user securely
        new_user = User.objects.create_user(username=username_data, password=password_data)
        new_user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login') # Moves directly to login page name
        
    # If request is GET, just show the page
    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        username_data = request.POST.get('username')
        password_data = request.POST.get('password')

        user = authenticate(request, username=username_data, password=password_data)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
            
    # If request is GET, just show the page
    return render(request, 'login.html')


# Dashboard View
@login_required(login_url='login')
def dashboard_view(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'dashboard.html', context)

#logout
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

#profile_view
@login_required(login_url='login')
def profile_view(request):
    return render(request,'profile.html')

#Note
@login_required(login_url='login')
def notes_view(request):
    if request.method == 'POST':
        title_data = request.POST.get('title')
        content_data = request.POST.get('content')
        
        # Save the note, explicitly attaching it to the logged-in user
        Note.objects.create(
            user=request.user, 
            title=title_data, 
            content=content_data
        )
        return redirect('note') # Refresh the page to show the new note
        
    # User isolation: ONLY fetch notes matching the current logged-in user
    user_notes = Note.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'note.html', {'notes': user_notes})

@login_required(login_url='login')
def delete_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('note')

#imagefield
@login_required(login_url='login')
def image_gallery(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image_file')
        title = request.POST.get('title')
        
        if image_file:
            Images.objects.create(
                user=request.user,
                title=title,
                image_file=image_file
            )
            messages.success(request, "Image uploaded securely to your vault!")
            return redirect('image_gallery')
        else:
            messages.error(request, "Please select a valid image file to upload.")

    images = Images.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'images.html', {'images': images})

@login_required(login_url='login')
def delete_image(request, image_id):
    if request.method == 'POST':
        # Ensures a user can only delete their own images
        image = get_object_or_404(Images, id=image_id, user=request.user)
        
        # Deletes the actual file from storage media, then removes the database entry
        image.image_file.delete()
        image.delete()
        
        messages.success(request, "Image permanently removed from your vault.")
    return redirect('image_gallery')

@login_required(login_url='login')
def documents_view(request):
    if request.method == 'POST':
        title_data = request.POST.get('title')
        uploaded_file = request.FILES.get('document_file') 

        if uploaded_file:
            Documents.objects.create(
                user=request.user,
                title=title_data or uploaded_file.name, # Fallback to file name if title is empty
                file=uploaded_file
            )
            return redirect('documents')

    # Security / Isolation: Filter down exclusively to the active user's documents
    user_docs = Documents.objects.filter(user=request.user).order_by('-uploaded_at')
    
    return render(request, 'documents.html', {'documents': user_docs})

@login_required(login_url='login')
def delete_document_view(request, doc_id):
    doc = get_object_or_404(Documents, id=doc_id, user=request.user)
    
    if doc.file and os.path.exists(doc.file.path):
        os.remove(doc.file.path)
        
    doc.delete()
    return redirect('documents')
