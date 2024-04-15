from django.shortcuts import render

# Create your views here.
def movie_list(request):
    return render(request, 'apple_tv/list/movie_list.html')

def movie_detail(request, movie_id):
    return render(request, 'apple_tv/detail/movie_detail.html')

def actors_list(request):
    return render(request, 'apple_tv/actors_list.html')

def directors_list(request):
    return render(request, 'apple_tv_directors_list.html')

def genres_list(request):
    return render(request, 'apple_tv/genres_list.html')

def producers_list(request):
    return render(request, 'apple_tv/list/prodecers_list.html')

def movie_list(request):
    return render(request, 'apple_tv/detail/actor_letail.html')

def actor_detail(request):
    return render(request, 'apple_tv/detail/actor_detail.html')

def director_detail(request, director_id):
    return render(request, 'apple_tv/detail/director_detail.html')

def genre_detail(request,  genre_id):
    return render(request, 'apple_tv/detail/genre_detail.html')

def prodecers_detail(request, genre_id):
    return render(request, 'apple_tv/detail/producer-detail.html')













































