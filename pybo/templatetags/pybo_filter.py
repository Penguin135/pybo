from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg

@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

"""
mark함수는 markdown 모듈과 mark_safe함수를 이용하여 입력된 문자열을 HTML코드로 변환해 주는 필터함수이다. 마크다운은 몇 가지 확장기능이 있는데 파이보는 위처럼 "nl2br"과 "fenced_code"를 사용하도록 설정하였다.
※ nl2br 은 줄바꿈 문자를 <br> 로 바꾸어 준다. 이 extension을 사용하지 않을 경우 줄바꿈을 하기 위해서는 공백문자, 즉 스페이스(' ')를 두개 연속으로 입력해야 한다. fenced_code는 위에서 살펴본 소스코드 기능을 사용하기 위해 필요하다.

마크다운의 더 많은 확장기능은 다음 URL을 참고
https://python-markdown.github.io/extensions/
"""