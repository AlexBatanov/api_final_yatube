from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import filters

from posts.models import Group, Post
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, FollowSerializer)
from .permissions import IsOwnerOrReadOnly
from .mixins import ListCreateViewSet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))

        return post.comments.all()


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.all()
