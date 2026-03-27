from django.shortcuts import get_object_or_404, redirect, render
from .models import Movie, Feedback, Comment, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def movie_list(request):
    movies = Movie.objects.filter(published=True).order_by('-movie_rating')
    return render(request, 'movie.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = movie.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            text = request.POST.get('comment')
            if text:
                Comment.objects.create(film=movie, user=request.user, text=text)
                return redirect('movie_detail', pk=pk)
        else:
            return redirect('login')

    return render(request, 'movie_detail.html', {'movie': movie, 'comments': comments})


@login_required(login_url="/login/")
def feedback(request):
    if request.method == 'POST':
        username = request.user
        email = username.email
        message = request.POST.get('message')
        if message:
            Feedback.objects.create(name=username, email=email, message=message)
            return redirect('feedback')

    return render(request, 'feedback.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})


