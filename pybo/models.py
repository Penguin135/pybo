from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # voter 추가
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

"""
null=True의 의미는 modify_date를 데이터베이스에 저장할때 null이 허용된다는 의미이다. blank=True의 의미는 입력 폼 데이터 체크시(form.is_valid()) 값이 없어도 오류를 내지 않는다는 의미이다. 즉, null=True, blank=True을 사용하면 어떤 조건으로든 값을 비워둘수 있음을 의미한다.

수정일시는 수정이 발생할 경우에만 생성되는 데이터이므로 null=True, blank=True 속성을 지정하였다.
"""

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)