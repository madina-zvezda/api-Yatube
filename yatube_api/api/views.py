from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS
from rest_framework.exceptions import PermissionDenied
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
)
from posts.models import Group, Post, Comment
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = (IsAuthenticated, IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied('Изменение чужого контента запрещено!')
    #     super(PostViewSet, self).perform_update(serializer)

    # def perform_destroy(self, instance):
    #     if instance.author != self.request.user:
    #         raise PermissionDenied('Удаление чужого контента запрещено!')
    #     super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = (IsAuthenticated, IsAuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get("id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get("id")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied('Изменение чужого контента запрещено!')
    #     super(CommentViewSet, self).perform_update(serializer)

    # def perform_destroy(self, instance):
    #     if instance.author != self.request.user:
    #         raise PermissionDenied('Удаление чужого контента запрещено!')
    #     super(CommentViewSet, self).perform_destroy(instance)
