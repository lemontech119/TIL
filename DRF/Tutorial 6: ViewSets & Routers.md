## Tutorial 6: ViewSets & Routers

 DRF에는 개발자가 API의 상태 및 상호 작용을 모델링하는데 집중하고 일반적인 규칙에 따라 URL구성을 자동으로 처리 할 수 있도록 해주는 ViewSets을 다루는 추상화가 포함되어 있습니다. 

ViewSet 클래스는 read, update와 같은 작업을 제공하며, get, put과 같은 메서드 핸들러가 아니라는 점을 제외하면 View 클래스와 거의 동일합니다. 

-----

> 3장에서의 View 클래스에서는 아래와 같은 방식으로 get, put 메서드를 가져와서 썼습니다. 

``` python
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```



#### Refactoring to use ViewSets

현재의 view들을 리팩토링을 진행합니다. 먼저 UserList, UserDetail을 single UserViewSet으로 리팩토링을 할 것입니다. 

UserList, UserDetail를 제거하고 하나의 클래스로 대체 할 수 있습니다. 

``` python
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

여기에서는 ReadOnlyModelViewSet 클래스를 사용하여 자동으로 기본 읽기 전용 작업을 제공합니다. 우리는 여전히 일반 view를 사용할 때와 마찬가지로 queryset 및 serializer_class 특성을 설정하지만 더 이상 2개의 별도 클래스에 동일한 정보를 제공할 필요가 없습니다. 



다음으로 SnippetList, SnippetDetail, SnippetHighlight 클래스를 제거하고, 단일 클래스로 변경합니다. 

```python
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    
    action(detail=True, renderers_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

이번에는 ModelViewSet 클래스를 사용하여 완전한 기본 읽기 및 쓰기 작업 기능을 가져왔습니다.

@action 데코레이터를 사용하여 highlight라는 사용자 정의 액션을 만들었습니다. 이 데코레이터는 기본 create/update/delete 스타일이 아닌 endpoints를 만들 수 있습니다. 

@action 데코레이터를 사용하는 사용자 정의 action은 기본적으로 GET요청에 응답을 합니다. POST요청에 응답을 원한다면 methods 인수를 사용할 수 있습니다. 

> snippets/urls.py 파일에 ViewSet 클래스를 바인딩 합니다. 

``` python
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
```

