from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, follower):
        user = self.context['request'].user

        if user == follower:
            raise serializers.ValidationError(
                'подписываться на самого себя нельзя'
            )

        return follower


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
