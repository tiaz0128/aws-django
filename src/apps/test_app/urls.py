from django.urls import path
from .views import hello_world  # 같은 디렉토리 내의 views.py 파일에서 뷰를 임포트

# 어플리케이션의 이름을 지정해 URL namespace를 설정할 수 있습니다.
app_name = "test"

urlpatterns = [
    # URL 패턴과 뷰 함수를 매핑합니다.
    # 예를 들어, "hello_world" 뷰 함수를 /hello/ URL에 매핑합니다.
    path("hello/", hello_world, name="hello_world"),
    # 더 많은 URL 패턴을 추가할 수 있습니다.
    # path('another_view/', views.another_view, name='another_view'),
]
