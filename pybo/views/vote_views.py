from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer

@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)

"""
본인 추천을 방지하기 위해 로그인한 사용자와 추천하려는 질문의 글쓴이가 동일할 경우에는 추천시 오류가 발생하도록 하였다.

Question 모델의 vorter는 여러사람을 추가할 수 있는 ManyToManyField이므로 question.voter.add(request.user) 처럼 add 함수를 사용하여 추천인을 추가해야 한다.

※ 동일한 사용자가 동일한 질문을 여러번 추천하더라도 추천수가 증가하지는 않는다. ManyToManyField를 사용하더라도 중복은 허락되지 않는다.
"""

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id = answer.question_id)