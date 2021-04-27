from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title')

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # 기존 필드 override

    # 첫 번째 방법 
    # read_only를 안해주면 아래 fields가 전체를 말하므로, 사용자에게 또 따로 값을 받아야한다.
    # 하지만 이 값은 읽기만 하는 fields이기 때문에 해줘야한다.
    # 역참조 모델 매니저 이름은 바꿀 수 있다. -> Models파일에서 related_name으로 ㅇㅇ
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # 두 번째 방법 
    comment_set = CommentListSerializer(many=True, read_only=True)
    # source에 'article.comment_set.count'라고 쓰지 않은 이유는, 이 클래스 자체가 Article을 모델로 하고 있기 때문.
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 오버라이드와 새로 추가된 필드의 경우 read_only를 Meta내에서는 할 수 없다.
    class Meta:
        model = Article
        fields = '__all__'

