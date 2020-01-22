from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    # read only allowed for any request
    if request.method in permissions.SAFE_METHODS:
      return True
    
    # write permissions only allowed for author
    return obj.author == request.user