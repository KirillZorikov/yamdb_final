from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class IsModerator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator


IsAdminOrReadOnly = ReadOnly | (IsAuthenticated & IsAdmin)
IsAuthorOrStaffOrReadOnly = ReadOnly | (
    IsAuthenticated & (IsAuthor | IsAdmin | IsModerator)
)
