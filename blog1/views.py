from django.shortcuts import render
from . import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage

#main blog1 homepage

def remove(lists):
  spc1 = ''' !@#$%^&*()_+{}|"|:<>?~ '''
  relist = []
  str1 = ''
  for i in lists:
    if i not in spc1:
      relist.append(i)
  return str1.join(relist)


def blog1(request):
	blog_obj = models.blog_model()
	all = models.blog_model.objects.all().order_by('-pub_date')
	return render(request,'blog1/blog.html', {'all':all})

def create_post(request):
	return render(request, 'blog1/create_post.html')



def upload_done(request):
	
	title = request.POST.get('title')
	post = request.POST.get('post')
	auther_name = request.POST.get('auther')
	image = request.FILES['image']
	code_link = request.POST.get('sourcecode')
	file_link = request.POST.get('youtubelink')
	date = datetime.now().strftime("%Y-%m-%d %H:%M")
	slug = remove(title[:5])

	blog = models.blog_model()

	blog.title = title
	blog.post = post
	blog.image = image
	blog.file_link = file_link
	blog.pub_name = auther_name
	blog.pub_date = date
	blog.slug = slug
	blog.save()



	return render(request, 'blog1/upload_done.html')



def blog_det(request, slug):
	#find article slug
	article = models.blog_model.objects.get(slug=slug)
	return render(request, 'blog1/details.html', {'art' : article})


def about(request):
	return render(request, 'blog1/about.html')
