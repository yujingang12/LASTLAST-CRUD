
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import PostForm
from django.utils import timezone

# Create your views here.

#메인페이지
def main(request):
    posts = Blog.objects
    return render(request, 'blog/main.html', {'posts':posts})
    

#글쓰기페이지
def write(request):
    return render(request, 'blog/write.html')

#글쓰기 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
           form = form.save(commit=False)
           form.pub_date = timezone.now()
           form.save()
           return redirect('main')
    else:
        form = PostForm
        return render(request, 'blog/write.html', {'form':form})


#디테일페이지
def detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    return render(request, 'blog/detail.html', {'post':blog})

#수정페이지
def edit(request, id):
    blog = get_object_or_404(Blog, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
           form.save(commit=False)
           form.save()
           return redirect('main')

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/edit.html', {'form':form})
   

#삭제 함수
def delete(request, id):
    blog = get_object_or_404(Blog, id = id)
    blog.delete()
    return redirect('main')