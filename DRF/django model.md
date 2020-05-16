## Django model 작업할때 몰라서 검색했던 내용

- PositiveSmallIntegerField : IntegerField와 같으나 양수 또는 0

  예를 들어 칼로리가있는 음식을 기록하는 경우 음수가되어서는 안됩니다. 이 필드는 유효성 검사를 통해 음수 값을 방지합니다.

- related_name

> `related_name` 속성은 `User` 모델에서 모델로 역방향 관계의 이름을 다시 지정합니다.
>
> `related_name`를 지정하지 않으면 Django는 `_set` 접미사와 함께 모델 이름을 사용하여 자동으로 만듭니다 (예 : `User.map_set.all()`).
>
> 당신 *할 경우* , 예를 들면. `User` 모델에서 `related_name=maps`, `User.map_set`는 여전히 작동하지만 `User.maps.` 구문은 분명히 조금 깨끗하고 덜 복잡합니다. 예를 들어 사용자 객체 `current_user`가있는 경우 `current_user.maps.all()`을 사용하여 `current_user`와 관련이있는 `Map` 모델의 모든 인스턴스를 가져올 수 있습니다.
>
> [Django 문서](https://docs.djangoproject.com/en/dev/topics/db/queries/#backwards-related-objects)

