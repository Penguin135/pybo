from django import forms
from pybo.models import Question, Answer, Comment

#장고의 폼은 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 있는데 모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 수 있게 된다. 모델 폼은 class Meta 라는 내부(Inner) 클래스가 반드시 필요하다. Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 한다.

# QuestionForm은 Question이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # Meta클래스에 widgets 속성을 지정하면 폼 입력 항목에 부트스트랩의 클래스를 추가할 수 있다.
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }

        # 장고 폼(form)에 대한 보다 자세한 내용은 다음 URL 참고 https://docs.djangoproject.com/en/3.0/topics/forms/

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }