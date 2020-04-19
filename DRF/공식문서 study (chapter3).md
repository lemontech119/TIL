#### drf 튜토리얼 스터디 3장

궁금한 내용을 <https://github.com/encode/django-rest-framework/tree/master/rest_framework> 에서 검색해서 정리

- mixins.ListModelMixin: 

  ``` python
  class ListModelMixin:
      """
      List a queryset.
      """
      def list(self, request, *args, **kwargs):
          queryset = self.filter_queryset(self.get_queryset())

          page = self.paginate_queryset(queryset)
          if page is not None:
              serializer = self.get_serializer(page, many=True)
              return self.get_paginated_response(serializer.data)

          serializer = self.get_serializer(queryset, many=True)
          return Response(serializer.data)
  ```

- mixins.CreateModelMixin:

  ```Python
  class CreateModelMixin:
      """
      Create a model instance.
      """
      def create(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          self.perform_create(serializer)
          headers = self.get_success_headers(serializer.data)
          return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

      def perform_create(self, serializer):
          serializer.save()

      def get_success_headers(self, data):
          try:
              return {'Location': str(data[api_settings.URL_FIELD_NAME])}
          except (TypeError, KeyError):
              return {}
  ```

- generics.GenericAPIView:

  ``` python
  class GenericAPIView(views.APIView):
      """
      Base class for all other generic views.
      """
      # You'll need to either set these attributes,
      # or override `get_queryset()`/`get_serializer_class()`.
      # If you are overriding a view method, it is important that you call
      # `get_queryset()` instead of accessing the `queryset` property directly,
      # as `queryset` will get evaluated only once, and those results are cached
      # for all subsequent requests.
      queryset = None
      serializer_class = None

      # If you want to use object lookups other than pk, set 'lookup_field'.
      # For more complex lookup requirements override `get_object()`.
      lookup_field = 'pk'
      lookup_url_kwarg = None

      # The filter backend classes to use for queryset filtering
      filter_backends = api_settings.DEFAULT_FILTER_BACKENDS

      # The style to use for queryset pagination.
      pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

      def get_queryset(self):
          """
          Get the list of items for this view.
          This must be an iterable, and may be a queryset.
          Defaults to using `self.queryset`.
          This method should always be used rather than accessing `self.queryset`
          directly, as `self.queryset` gets evaluated only once, and those results
          are cached for all subsequent requests.
          You may want to override this if you need to provide different
          querysets depending on the incoming request.
          (Eg. return a list of items that is specific to the user)
          """
          assert self.queryset is not None, (
              "'%s' should either include a `queryset` attribute, "
              "or override the `get_queryset()` method."
              % self.__class__.__name__
          )

          queryset = self.queryset
          if isinstance(queryset, QuerySet):
              # Ensure queryset is re-evaluated on each request.
              queryset = queryset.all()
          return queryset

      def get_object(self):
          """
          Returns the object the view is displaying.
          You may want to override this if you need to provide non-standard
          queryset lookups.  Eg if objects are referenced using multiple
          keyword arguments in the url conf.
          """
          queryset = self.filter_queryset(self.get_queryset())

          # Perform the lookup filtering.
          lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

          assert lookup_url_kwarg in self.kwargs, (
              'Expected view %s to be called with a URL keyword argument '
              'named "%s". Fix your URL conf, or set the `.lookup_field` '
              'attribute on the view correctly.' %
              (self.__class__.__name__, lookup_url_kwarg)
          )

          filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
          obj = get_object_or_404(queryset, **filter_kwargs)

          # May raise a permission denied
          self.check_object_permissions(self.request, obj)

          return obj

      def get_serializer(self, *args, **kwargs):
          """
          Return the serializer instance that should be used for validating and
          deserializing input, and for serializing output.
          """
          serializer_class = self.get_serializer_class()
          kwargs['context'] = self.get_serializer_context()
          return serializer_class(*args, **kwargs)

      def get_serializer_class(self):
          """
          Return the class to use for the serializer.
          Defaults to using `self.serializer_class`.
          You may want to override this if you need to provide different
          serializations depending on the incoming request.
          (Eg. admins get full serialization, others get basic serialization)
          """
          assert self.serializer_class is not None, (
              "'%s' should either include a `serializer_class` attribute, "
              "or override the `get_serializer_class()` method."
              % self.__class__.__name__
          )

          return self.serializer_class

      def get_serializer_context(self):
          """
          Extra context provided to the serializer class.
          """
          return {
              'request': self.request,
              'format': self.format_kwarg,
              'view': self
          }

      def filter_queryset(self, queryset):
          """
          Given a queryset, filter it with whichever filter backend is in use.
          You are unlikely to want to override this method, although you may need
          to call it either from a list view, or from a custom `get_object`
          method if you want to apply the configured filtering backend to the
          default queryset.
          """
          for backend in list(self.filter_backends):
              queryset = backend().filter_queryset(self.request, queryset, self)
          return queryset

      @property
      def paginator(self):
          """
          The paginator instance associated with the view, or `None`.
          """
          if not hasattr(self, '_paginator'):
              if self.pagination_class is None:
                  self._paginator = None
              else:
                  self._paginator = self.pagination_class()
          return self._paginator

      def paginate_queryset(self, queryset):
          """
          Return a single page of results, or `None` if pagination is disabled.
          """
          if self.paginator is None:
              return None
          return self.paginator.paginate_queryset(queryset, self.request, view=self)

      def get_paginated_response(self, data):
          """
          Return a paginated style `Response` object for the given output data.
          """
          assert self.paginator is not None
          return self.paginator.get_paginated_response(data)


  # Concrete view classes that provide method handlers
  # by composing the mixin classes with the base view.
  ```

  ​

- Why? 

``` python
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

장고 튜토리얼을 따라 하게 되다 보면 여러 위의 방식처럼 여러 클래스들을 가져와서 쓰는 것을 볼 수 있습니다. 위에 정리한 것 처럼 mixins.ListModelMixin은 list 함수를 mixins.CreateModelMixin은 create 함수를 제공해주는 것을 확인할 수 있습니다. 

근데..? generics.GenericAPIView의 역할은 무엇일까?

공식문서에서는 아래와 같이 적혀 있습니다.

> `GenericAPIView` class to provide the core functionality
>
> 핵심 기능을 제공해주는 클래스…? (그래서 뭐..?)

위에 작성한 generics.GenericAPIView를 보게 되면 여러 함수를 선언하지만 튜토리얼에서 사용하지 않습니다. 그래서 해당 내용을 제거 하고 서버를 켜봤습니다. 

결과는 아래와 같습니다. (정말 많은 내용이 있었지만 그나마 이해했던 아래 부분만 확인해보겠습니다.)

``` bash
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/dongwonahn/Documents/GitHub/6th-django-study/env/tutorial/snippets/urls.py", line 6, in <module>
    path('snippets/', views.SnippetList.as_view()),
AttributeError: type object 'SnippetList' has no attribute 'as_view'
```

SnippetList에 as_view 속성이 없다고 에러가 나옵니다. 

as_view를 사용하고 있는것은 urls.py에서 사용중입니다. 

``` Python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

generics.GenericAPIView에는 as_view가 없어서 잘 찾아보니깐 views.APIView를 받아와서 사용하는 걸 알 수 있습니다. 

``` python
class GenericAPIView(views.APIView):
```

views.APIView를 보게 되면 더 많은 함수를 가지고 있지만 여기서 궁금한 내용까지만 보겠습니다.

``` python
class APIView(View):

    # The following policies may be set at either globally, or per-view.
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS
    metadata_class = api_settings.DEFAULT_METADATA_CLASS
    versioning_class = api_settings.DEFAULT_VERSIONING_CLASS

    # Allow dependency injection of other settings to make testing easier.
    settings = api_settings

    schema = DefaultSchema()

    @classmethod
    def as_view(cls, **initkwargs):
        """
        Store the original class on the view function.

        This allows us to discover information about the view when we do URL
        reverse lookups.  Used for breadcrumb generation.
        """
        if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
            def force_evaluation():
                raise RuntimeError(
                    'Do not evaluate the `.queryset` attribute directly, '
                    'as the result will be cached and reused between requests. '
                    'Use `.all()` or call `.get_queryset()` instead.'
                )
            cls.queryset._fetch_all = force_evaluation

        view = super().as_view(**initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs

        # Note: session based authentication is explicitly CSRF validated,
        # all other authentication is CSRF exempt.
        return csrf_exempt(view)

```

