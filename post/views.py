from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import post
from .forms import postForm

# Create your views here.
#---------------------------------------------------------------
#---------------------------------------------------------------

class HomePageView(ListView):
	model = post
	template_name = 'home.html'

class PostPageView(ListView):
	model = post
	template_name = 'post.html'
	context_object_name = 'post_list'


#---------------------------------------------------------------
#---------------------------------------------------------------

def agregar (request):
	
	data = {
		'form':postForm()
	}

	if request.method == 'POST':
		formulario = postForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='post')
		else:
			data['form'] = formulario

	return render(request, 'agregar.html',data)


def modificar (request, id):

	Post = get_object_or_404(post, id=id)

	data = {
		'form': postForm(instance=Post)
	}

	if request.method == "GET":
		form = postForm()
	else:
		form = postForm(request.POST,request.FILES, instance=Post)
		form.instance.rel_user = request.user
		if form.is_valid():
			form.save()
			return redirect('post')
	return render(request, 'modificar.html', data)


def eliminar (request, id):
	Post = get_object_or_404(post, id=id)
	Post.delete()

	return redirect(to = "post")
