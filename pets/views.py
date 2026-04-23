import os
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .ml.image_matcher import match_image
from django.conf import settings
from django.contrib.auth.models import User
from .forms import LostPetForm, ImageSearchForm
from .models import Pet
from .ml.image_matcher import match_image



def gallery(request):
    pets = Pet.objects.filter(is_lost=False)
    return render(request, 'pets/gallery.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('gallery')
        else:
            return render(request, 'pets/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'pets/login.html')



login_required
def user_profile(request):
    user = request.user
    user_pets = Pet.objects.filter(owner=user)

    return render(request, 'pets/profile.html', {
        'user': user,
        'pets': user_pets
    })



@login_required
def add_lost_pet(request):
    if request.method == 'POST':
        form = LostPetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.is_lost = True
            pet.save()
            return redirect('profile')
    else:
        form = LostPetForm()

    return render(request, 'pets/add_lost_pet.html', {'form': form})




@login_required
def search_pet(request):
    result = None
    matched_pet = None
    score = None

    if request.method == 'POST':
        form = ImageSearchForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_image = form.cleaned_data['image']

            # ✅ Save uploaded image temporarily
            temp_path = os.path.join(settings.MEDIA_ROOT, 'temp_search.jpg')
            with open(temp_path, 'wb+') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

            # ✅ Build gallery paths AND mapping
            pets = Pet.objects.all()
            print("Number of gallery pets:", pets.count())

            gallery_path_to_pet = {}
            gallery_paths = []

            for pet in pets:
                img_path = pet.image.path
                gallery_paths.append(img_path)
                gallery_path_to_pet[img_path] = pet

            # ✅ Run ML matching
            matched, best_path, score = match_image(
                temp_path,
                gallery_paths
            )

            if matched:
                matched_pet = gallery_path_to_pet.get(best_path)
                result = f"✅ Match Found (Similarity: {score:.2f})"
            else:
                result = "❌ No Match Found"

    else:
        form = ImageSearchForm()

    return render(request, 'pets/search_pet.html', {
        'form': form,
        'result': result,
        'matched_pet': matched_pet,
        'score': score
    })
