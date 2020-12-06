# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from django.http import HttpResponse
# from .models import Question
# from .models import Answer
# from .models import Comment
# from .forms import QuestionForm, AnswerForm, CommentForm
# from django.core.paginator import Paginator # 페이징
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # Create your views here.
# def index(request):
#     """
#     pybo 목록 출력
#     """
#     # 입력 파라미터
#     page = request.GET.get('page', '1') # 페이지
    
#     # 조회
#     question_list = Question.objects.order_by('-create_date')

#     # 페이징처리
#     paginator = Paginator(question_list, 10) # 페이지당 10개식 보여주기
#     page_obj = paginator.get_page(page)

#     context = {'question_list': page_obj}

#     return render(request, 'pybo/question_list.html', context)

# def detail(request, question_id):
#     """
#     pybo 내용 출력
#     """
#     # question = Question.objects.get(id=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     """
#     pybo 답변등록
#     """
#     # question = get_object_or_404(Question, pk=question_id)
#     # #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
#     # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
#     # answer.save()
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def question_create(request):
#     """
#     pybo 질문등록
#     """
#     # 목록조회 화면에서 "질문 등록하기" 버튼을 클릭한 경우에는 http://localhost:8000/pybo/question/create/ 페이지가 GET 방식으로 호출(request.method == 'GET')되어 질문등록 화면이 호출되고 질문등록 화면에서 "저장하기" 버튼을 클릭하면 http://localhost:8000/pybo/question/create/ 페이지가 POST 방식으로 호출(request.method == 'POST')되어 데이터가 저장된다.
#     # form태그의 action속성이 없는 경우는 현재의 페이지로 전송된다.
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             # 폼 저장시 question = form.save(commit=False) 처럼 commit=False라는 옵션을 사용하면 폼에 연결된 모델을 저장하지 않고 생성된 모델 객체만 리턴해 준다. 만약 여기서 form.save(commit=False) 대신 form.save() 를 수행하면 create_date에 값이 없다는 오류가 발생하게 될 것이다.
#             # 이렇게 코드내에서 자동으로 생성되는 값(예:create_date)을 저장하기 위해서는 form.save(commit=False)를 사용해야 한다.
#             question = form.save(commit=False)
#             question.author = request.user  # 추가한 속성 author 적용
#             question.create_date = timezone.now()
#             question.save()
#             return redirect('pybo:index')
#     else:
#         form = QuestionForm()
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)

# def answer_create(request, question_id):
#     """
#     pybo 답변등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     # ---------------------------------------- [edit] ---------------------------------------- #
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user  # 추가한 속성 author 적용
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     """
#     pybo 질문수정
#     question_modify 함수는 로그인한 사용자(request.user)와 수정하려는 질문의 글쓴이(question.author)가 다를 경우에는 "수정권한이 없습니다"라는 오류를 발생시킨다. 이 오류를 발생시키기 위해 messages 모듈을 이용하였다. messages는 장고가 제공하는 함수로 넌필드 오류(non-field error)를 발생시킬 경우에 사용된다.

#     ※ form_error.html 템플릿에서 필드오류와 넌필드오류에 대해서 출력했던 부분을 상기해 보자.
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question_id)

#     if request.method == "POST":
# # GET으로 요청된 경우 질문수정 화면에 조회된 질문의 제목과 내용이 반영될 수 있도록 다음과 같이 폼을 생성해야 한다.

# # form = QuestionForm(instance=question)
# # 폼 생성시 이처럼 instance값을 지정하면 폼에 값이 채워지게 된다. 따라서 질문을 수정하는 화면에서 제목과 내용이 채워진 채로 보여지게 될 것이다.

# # POST로 요청되는 경우는 수정된 내용을 반영해야 하는 케이스이므로 다음처럼 폼을 생성해야 한다.

# # form = QuestionForm(request.POST, instance=question)
# # 위 코드의 의미는 조회된 질문의 내용으로 QuestionForm을 생성하지만 request.POST의 값으로 덮어쓰라는 의미이다. 따라서 질문 수정화면에서 제목 또는 내용을 변경하여 POST로 호출하면 변경된 내용이 QuestionForm에 저장될 것이다.

# # 그리고 질문의 수정일시는 다음처럼 현재일시로 저장되도록 했다.

# # question.modify_date = timezone.now() 
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modify_date = timezone.now() # 수정일시 저장
#             question.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form':form}
#     return render(request, 'pybo/question_form.html', context)

# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     """
#     pybo 질문삭제
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')

# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     """
#     pybo 답변수정
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=answer.question.id)
        
#     if request.method=="POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)

# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     """
#     pybo 답변삭제
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('pybo:detail', question_id=answer.question.id)


# @login_required(login_url='common:login')
# def comment_create_question(request, question_id):
#     """
#     pybo 질문댓글등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.question = question
#             comment.save()
#             return redirect('pybo:detail', question_id = question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)

# @login_required(login_url='common:login')
# def comment_modify_question(request, comment_id):
#     """
#     질문댓글 수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글 수정 권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.question.id)
    
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)

# @login_required(login_url='common:login')
# def comment_delete_question(request, comment_id):
#     """
#     질문 댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글 삭제 권한이 없습니다')
#         return redirect('pybo:detail', question_id = comment.question_id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.question_id)


# @login_required(login_url='common:login')
# def comment_create_answer(request, answer_id):
#     """
#     pybo 답글댓글등록
#     """
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.create_date = timezone.now()
#             comment.answer = answer
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm()
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)


# @login_required(login_url='common:login')
# def comment_modify_answer(request, comment_id):
#     """
#     pybo 답글댓글수정
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)

#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.modify_date = timezone.now()
#             comment.save()
#             return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         form = CommentForm(instance=comment)
#     context = {'form': form}
#     return render(request, 'pybo/comment_form.html', context)


# @login_required(login_url='common:login')
# def comment_delete_answer(request, comment_id):
#     """
#     pybo 답글댓글삭제
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)
#     if request.user != comment.author:
#         messages.error(request, '댓글삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=comment.answer.question.id)
#     else:
#         comment.delete()
#     return redirect('pybo:detail', question_id=comment.answer.question.id)