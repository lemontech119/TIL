## DRF 튜토리얼 Chapter 4: Authentication & Permissions(인증&권한)

현재까지 진행한 API에서는 누구나 데이터를 편집하거나, 삭제하는데 있어 아무 제한이 없다. 
다음과 같은 사항을 확실히 하기 위해 더 나은 기능을 추가해보자

- 데이터는 항상 생성자와 연관되어 있다. 
- 인증받은 사용자만이 데이터를 생성할 수 있다. 
- 작성자만이 수정하거나 삭제할 수 있다.
- 인증받지 않은 사용자는 읽기 전용만 가능하다. 



#### Adding information to our model

snippet모델에서 몇가지를 추가할 것 입니다. 먼저 몇가지 필드를 추가합니다. 필드 중 하나는 생성한 사용자를 나타내는데 사용하고, 다른 필드는 HTML의 하이라이트 부분을 저장하는데 사용한다. 

``` python
owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()
```

다음 라이브러리들을 import 합니다.

``` python
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
```

그러면 save 메소드를 우리의 model에 추가할 수 있습니다.

``` python
def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Snippet, self).save(*args, **kwargs)
```

그리고 데이터 베이스를 업데이트를 해줍니다. 

``` bash
rm -f db.sqlite3
rm -r snippets/migrations
python manage.py makemigrations snippets
python manage.py migrate
## api 테스트를 위해 createsuperuser 생성
python manage.py createsuperuser
```



#### Adding endpoints for our User models

사용자를 추가했으니 사용자를 보여주는 api를 추가해보자 

serializers.py에 아래 내용을 추가해줍니다.

``` python
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
```

snippets는 User모델과 역방향 관계이기 때문에, Modelserializer 클래스를 이용할 때 기본적으로 포함되어 있지 않습니다.

그렇기 때문에 명시적으로 필드를 지정해줘야 합니다.  

---

사용자와 관련된 읽기 전용 view만 사용하게 되므로, generic class 기반 view 중 LIstAPIView와 RetrieveAPIView를 사용합니다.

아래 내용을 views.py에 추가합니다. 

``` python
from django.contrib.auth.models import User
## serializer는 SnippetSerializer까지는 있을거기 때문에 뒤에 UserSerializer만 추가해줍니다. 
from snippets.serializers import SnippetSerializer, UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

마지막으로 이러한 view들을 URL conf에서 참조해 API에 추가해야 한다. 

``` python
path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
```



#### Associating Snippets with Users

데이터를 생성했지만, 데이터를 생성한 생성자와 연결할 방법이 없었고, 이를 해결하기 위해 perform_create 메서드를 오버라이딩합니다. 

이 메서드는 인스턴스 저장 방법을 관리하고, 들어오는 요청이나 요청된 url에서 들어온 정보를 처리합니다. 

views.py의 SnippetList 클래스에 다음 내용을 추가합니다.

``` python
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

- serializer의 create 메서드는 데이터와 함께 owner 필드가 함께 전달된다. 



#### Updating our serializer

이제 데이터와 이를 만든 사용자가 연결되어 있으므로 SnippetSerializer응 업데이트를 해줍니다.

아래의 내용을 serializers.py의 class SnippetSerializer에 추가해줍니다. 

``` python
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']
```

- ReadOnlyField는 source인자를 이용해 특정 필드를 지정할 수 있습니다. 
- 이 필드는 타입이 CharField, BooleanField와 달리 타입이 없으며, 항상 읽기 전용이므로 모델의 인스턴스를 업데이트할 때는 사용할 수 없습니다.
- CharField(read_only=True)도 동일한 기능을 수행합니다.



#### Adding required permissions to views

이제 사용자와 데이터가 연결 되었으므로, 인증받은 사용자만이 데이터를 생성/ 업데이트/ 삭제할 수 있습니다. 

REST framework에는 주어진 view에 접근할 수 있는 사용자를 제한하는 데 사용할 수 있는 많은 클래스를 제공합니다. 

여기서 사용되는 IsAuthenticatedOrReadOnly는 인증된 요청에 읽기, 쓰기 권한이 부여되고 인증되지 않은 요청에는 읽기 전용 권한이 부여됩니다. 

우선 views.py에 다음 내용을 추가합니다.

``` python
from rest_framework import permissions
```

그리고 SnippetList class와 SnippetDetail class에 다음 속성을 추가합니다. 

``` python
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

- 여기서 IsAuthenticatedOrReadOnly는 아래와 같이 구성되어 있습니다. 

``` python
class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

```



#### Adding login to the Browsable API

- 이 시점에 브라우저에서 API에 접속한다면 데이터가 생성되지 않는 것을 알 수 있습니다.
- 이 문제를 해결하기 위해 사용자 로그인 기능이 필요합니다.
- urls.py를 수정해 API에 로그인 view를 추가해줘야 합니다. 

``` python
from django.conf.urls import include

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
```

이제 <http://localhost:8000/snippets/> 에 재 접속을 하게 되면 우측 상단에 Log in 버튼이 보일 겁니다. 

앞서 createsuperuser로 만들어준 아이디, 패스워드를 입력하여 들어갑니다. 

그럼 이제 데이터를 생성할 수 있으니, 몇 개의 테스트 데이터를 생성합니다. 

그리고 <http://localhost:8000/users/> 에 접속을 하게 되면 추가 된 것을 확인할 수 있습니다. 



#### Object level permissions

- 생성된 데이터들은 누구나 볼 수 있어야 하지만, 만든 사용자만이 업데이트와 삭제를 할 수 있어야 합니다.
  - 현재는 만든 사용자가 아니더라도 로그인을 했을 경우 업데이트와 삭제가 가능합니다.
- 이를 위해 permissions.py 파일을 만들어 사용자 지정 권한을 작성합니다. 

``` python
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
```

그리고 views.py에 추가해주고,

``` python
from snippets.permissions import IsOwnerOrReadOnly
```

SnippetDetail의 permission_classes에 해당 사용자 지정 권한을 추가해줍니다. 

``` Python
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
```

이제 브라우저를 열면, 데이터를 만든 사용자에게만 삭제 수정이 보이는 것을 알 수 있습니다. 