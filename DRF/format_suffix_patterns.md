## 스터디 준비(format_suffix_patterns)

2장에서 진행했던 내용 중 format_suffix_patterns 에서 이건 어떻게 사용할까의 의문점 조금 해결을 해보자

우선 다들 기본적으로 코딩을 해왔다는 기준을 잡고 진행합니다. 

``` python
def snippet_list(request, format=None):
```

``` python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

테스트를 위해 설치를 진행해야 됩니다. 

``` bash
$ pip install djangorestframework-xml
```

그 다음 settings.py에 아래 내용을 추가해주시면 됩니다.

``` python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    )
}
```

urls.py에 아래 내용을 추가해줍니다. 

``` python
urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "xml"])
```



그 다음 서버를 키고 아래 url로 접속을 하게 되면

> <http://127.0.0.1:8000/users.xml>

xml이 나오게 되는 것을 알 수 있습니다. 

또한 xml 대신 json으로 하게 될 경우 json형태의 데이터셋을 받을 수 있습니다. 



**실습**

- csv로도 나오게 한 번 만들어보자!!!