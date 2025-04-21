todos_permissions = {
    "admin": {
        "view": True,
        "create": True,
        "update": True,
        "delete": True,
    },
    "moderator": {
        "view": True,
        "create": True,
        "update": True,
        "delete": lambda user, todo: todo["completed"],
    },
    "user": {
        "view": lambda user, todo: todo["user_id"]==user["id"],
        "create": True,
        "update": lambda user, todo: todo["user_id"] == user["id"] or user["id"] in todo["invited_users"],
        "delete": lambda user, todo: (todo["user_id"] == user["id"] or user["id"] in todo["invited_users"]) and todo["completed"],
    },
}
