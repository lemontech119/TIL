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