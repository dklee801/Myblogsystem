from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from posts.form import PostForm

# Create your views here.
def p_list(request):
    my_list = Post.objects.all().order_by('-id') # '-id' id역순으로
    context = {'posts':my_list}
    return render(request, 'list.html', context) # html 에 데이터 전달할 때 꼭 dict형태로


def p_create(request):
    # POST 방식으로 호출될 때
    if request.method == 'POST':
        post_form = PostForm(request.POST) #post방식으로 전송된 데이터 전부 postform객체로

        if post_form.is_valid():# 입력된 데이터가 유효하면,
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될 때
    else:
        post_form = PostForm()
        return render(request, 'create.html', {'post_form':post_form})

def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:list')

def p_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # POST 방식으로 호출될 때
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)  # post방식으로 전송된 데이터 전부 postform객체로

        if post_form.is_valid():  # 입력된 데이터가 유효하면,
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될 때
    else:
        post_form = PostForm(instance=post)
        return render(request, 'create.html', {'post_form': post_form})
