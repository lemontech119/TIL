## DRF 궁금한 점 정리



#### class Meta의 의미??

``` python
## 공식 문서 나와 있는 코드입니다.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
# Create your models here.

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    ## 이 친구의 의미가 무엇일까?
    class Meta:
        ordering = ['created']
```

> Meta 옵션이란 다음과 같이 inner class로 상위 클래스에서 meta data를 제공하는 것
>
> 여러 옵션을 줄 수 있습니다. 

- verbose_name 옵션: 모델 자체의 이름 (단수형)

- verbose_name_plural: 복수형

  - 해당 옵션은 정의되지 않았으면, 자동으로 뒤에 s하나를 붙여준다.

- ordering 옵션: 모델의 정렬 순서를 지정하며 여러 개를 지정할 경우 필드 이름을 리스트로 나열한다. 기본값은 오름차순으로 정렬하고 - 를 붙이면 내림차순으로 정렬한다. 

  - ``` python
    ordering = ['-created', 'test']
    ```

  - 위의 예시는 created 필드 기준 내림차순으로 정렬하고 다시 test 필그를 기준으로 오름차순으로 정렬



#### serializers 역할

- cs에서 데이터구조나 오브젝트를 저장하고 재구성 할 수 있는 포맷으로 만드는 역할을 수행