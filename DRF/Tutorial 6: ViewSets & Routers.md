## Tutorial 6: ViewSets & Routers

지금까지는 apiview를 활용해서 주로 만들었지만 6장에서는 ViewSets을 이용해서 만드는 법에 대해 튜토리얼을 가집니다. 

ViewSet: CRUD를 만드는 가장 기본적인 방법

View: 자신의 마음대로 코드를 작성할 수 있지만, 중복 코드를 제거하지 못한다. 

---------------

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
## UserList, UserDetail 제거
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

UserViewSet으로 리펙토링 진행

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

--------

``` python
class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
     
    
class RetrieveAPIView(mixins.RetrieveModelMixin,
                      GenericAPIView):
    """
    Concrete view for retrieving a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
```

``` python
class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    """
    A viewset that provides default `list()` and `retrieve()` actions.
    """
    pass
```



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

``` python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```



@action 데코레이터를 사용하여 highlight라는 사용자 정의 액션을 만들었습니다. 이 데코레이터는 기본 create/update/delete 스타일이 아닌 endpoints를 만들 수 있습니다. 

@action 데코레이터를 사용하는 사용자 정의 action은 기본적으로 GET요청에 응답을 합니다. POST요청에 응답을 원한다면 methods 인수를 사용할 수 있습니다.

------

action decorator

``` python
def action(methods=None, detail=None, url_path=None, url_name=None, **kwargs):
    """
    Mark a ViewSet method as a routable action.

    `@action`-decorated functions will be endowed with a `mapping` property,
    a `MethodMapper` that can be used to add additional method-based behaviors
    on the routed action.

    :param methods: A list of HTTP method names this action responds to.
                    Defaults to GET only.
    :param detail: Required. Determines whether this action applies to
                   instance/detail requests or collection/list requests.
    :param url_path: Define the URL segment for this action. Defaults to the
                     name of the method decorated.
    :param url_name: Define the internal (`reverse`) URL name for this action.
                     Defaults to the name of the method decorated with underscores
                     replaced with dashes.
    :param kwargs: Additional properties to set on the view.  This can be used
                   to override viewset-level *_classes settings, equivalent to
                   how the `@renderer_classes` etc. decorators work for function-
                   based API views.
    """
    methods = ['get'] if (methods is None) else methods
    methods = [method.lower() for method in methods]

    assert detail is not None, (
        "@action() missing required argument: 'detail'"
    )

    # name and suffix are mutually exclusive
    if 'name' in kwargs and 'suffix' in kwargs:
        raise TypeError("`name` and `suffix` are mutually exclusive arguments.")

    def decorator(func):
        func.mapping = MethodMapper(func, methods)

        func.detail = detail
        func.url_path = url_path if url_path else func.__name__
        func.url_name = url_name if url_name else func.__name__.replace('_', '-')

        # These kwargs will end up being passed to `ViewSet.as_view()` within
        # the router, which eventually delegates to Django's CBV `View`,
        # which assigns them as instance attributes for each request.
        func.kwargs = kwargs

        # Set descriptive arguments for viewsets
        if 'name' not in kwargs and 'suffix' not in kwargs:
            func.kwargs['name'] = pretty_name(func.__name__)
        func.kwargs['description'] = func.__doc__ or None

        return func
    return decorator

```



---------

핸들러 메서드는 URLConf를 정의 할 때만 액션에 바인딩됩니다. 내부에서 진행중인 작업을 먼저 보려면 먼저 ViewSet에서 명시적으로 일련의 보기를 만듭니다.  

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

이제 리소스를 concreate view로 묶었으므로 평소처럼 URL conf를 사용하여 뷰를 등록할 수 있습니다. 

``` python
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
```



#### Using Routers

View 클래스보다는 ViewSet 클래스를 사용하기 때문에 실제로 URL을 직접 디자인 할 필요가 없습니다. 보기 및 URL에 자원을 연결하는 Router 클래스를 사용하여 자동으로 처리할 수 있습니다. 적절한 view를 라우터에 등록하고 나머지는 그대로 놔두면 됩니다. 

``` python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
```

우리가 사용하고 있는 DefaultRouter 클래스는 자동으로 API 루트 뷰를 생성하기 때문에 view 모듈에 있는 api_root 메소드를 삭제할 수 있습니다. 

----------

> DefaultRouter > SimpleRouter > BaseRouter

``` python
## DefaultRouter
class DefaultRouter(SimpleRouter):
    """
    The default router extends the SimpleRouter, but also adds in a default
    API root view, and adds format suffix patterns to the URLs.
    """
    include_root_view = True
    include_format_suffixes = True
    root_view_name = 'api-root'
    default_schema_renderers = None
    APIRootView = APIRootView
    APISchemaView = SchemaView
    SchemaGenerator = SchemaGenerator

    def __init__(self, *args, **kwargs):
        if 'root_renderers' in kwargs:
            self.root_renderers = kwargs.pop('root_renderers')
        else:
            self.root_renderers = list(api_settings.DEFAULT_RENDERER_CLASSES)
        super().__init__(*args, **kwargs)

    def get_api_root_view(self, api_urls=None):
        """
        Return a basic root view.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)

    def get_urls(self):
        """
        Generate the list of URL patterns, including a default root view
        for the API, and appending `.json` style format suffixes.
        """
        urls = super().get_urls()

        if self.include_root_view:
            view = self.get_api_root_view(api_urls=urls)
            root_url = url(r'^$', view, name=self.root_view_name)
            urls.append(root_url)

        if self.include_format_suffixes:
            urls = format_suffix_patterns(urls)

        return urls
```

``` python
## BaseRouter

class BaseRouter:
    def __init__(self):
        self.registry = []

    def register(self, prefix, viewset, basename=None):
        if basename is None:
            basename = self.get_default_basename(viewset)
        self.registry.append((prefix, viewset, basename))

        # invalidate the urls cache
        if hasattr(self, '_urls'):
            del self._urls

    def get_default_basename(self, viewset):
        """
        If `basename` is not specified, attempt to automatically determine
        it from the viewset.
        """
        raise NotImplementedError('get_default_basename must be overridden')

    def get_urls(self):
        """
        Return a list of URL patterns, given the registered viewsets.
        """
        raise NotImplementedError('get_urls must be overridden')

    @property
    def urls(self):
        if not hasattr(self, '_urls'):
            self._urls = self.get_urls()
        return self._urls

```



