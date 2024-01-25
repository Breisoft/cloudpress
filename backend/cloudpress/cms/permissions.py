
from rest_framework import permissions


class CreateBlogPostPermissions(permissions.BasePermission):
    """
    Check for permissions to blog posts
    Intentionally designed so that it can be swapped out with other business logic in the future
    in case we decide that non-admin users should also be allowed to make blog posts
    """

    def has_permission(self, request, view):
        return request.user.is_superuser
