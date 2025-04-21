from . import RESOURCES
from app.user.models import User

def has_permission(user:User, resource:str, action:str, data:dict=None):
    """
    Checks if a user has permission to perform a specific action on a resource.
    
    :param user: A dictionary representing the user
    :param resource: The resource type ('comments' or 'todos')
    :param action: The action to perform ('view', 'create', 'update', 'delete')
    :param data: The resource data (optional, only required for conditional permissions)
    :return: True if permission is granted, False otherwise
    """
    roles= [role.name for role in user.roles]
    user = user.model_dump()
    for role in roles:
        role_permissions = RESOURCES.get(resource, {}).get(role, {})
        permission_check = role_permissions.get(action)

        if permission_check is None:
            continue

        if isinstance(permission_check, bool):
            return permission_check

        if callable(permission_check) and data is not None:
            return permission_check(user, data)

    return False
