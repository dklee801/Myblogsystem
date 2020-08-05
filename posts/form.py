from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','contents'] # 모델을 기반으로 입력칸 생성