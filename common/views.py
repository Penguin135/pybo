from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

"""
signup함수는 POST요청인 경우에는 입력으로 전달받은 데이터를 이용하여 사용자를 생성하고 GET요청인 경우에는 common/signup.html 템플릿을 호출한다.

form.cleaned_data.get 함수는 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수로 위에서는 사용자 등록시 폼으로 전달된 사용자명, 비밀번호등을 얻기 위해 사용되었다.

신규 사용자를 저장한 후에 자동 로그인 될 수 있도록 authenticate와 login함수가 사용되었다. authenticate와 login함수는 django.contrib.auth 패키지의 함수로 사용자 인증과 로그인을 담당한다.
"""