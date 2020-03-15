from django.shortcuts import render
from blogin.models import Post


def blog(request):
	allPosts=Post.objects.all()
	context={'allPosts':allPosts}
	return render(request, 'blogin/blog.html',context)

def blogPost(request,slug):
	post=Post.objects.filter(slug=slug)[0] 
	context={'post':post}

	return render(request, 'blogin/blogPost.html',context)
# Create your views here.
