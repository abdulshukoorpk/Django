from rest_framework import permissions


class IsAssignedUser(permissions.BasePermission):

    """
    Custom permission so that only the assigned user can see the test details.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user