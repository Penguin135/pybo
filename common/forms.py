from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "email")

"""
UserForm은 django.contrib.auth.forms 패키지의 UserCreationForm 클래스를 상속하여 만들었다. 그리고 추가적으로 email 속성을 추가해 주었다. UserForm을 따로 만들지 않고 UserCreationForm을 그대로 사용해도 되지만 이메일등의 부가 속성을 주기 위해서는 이처럼 UserCreationForm을 상속하여 만들어 주어야 한다.

상속한 UserCreationForm은 다음과 같은 속성을 가지고 있다.

속성명	설명
username	사용자이름
password1	비밀번호1
password2	비밀번호2

UserCreationForm은 is_valid() 함수로 폼 체크시 위 3개 속성을 필수값으로 체크한다. 그리고 "비밀번호1"과 "비밀번호2"의 값이 같은지를 체크하고 비밀번호의 값이 비밀번호 생성규칙에 맞는지를 검증한다.
"""