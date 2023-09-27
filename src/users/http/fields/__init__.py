input_create_user = [
    {
        "field": "username",
        "type": str,
        "required": True
    },
    {
        "field": "password",
        "type": str,
        "required": True
    },
    {
        "field": "email",
        "type": str,
        "required": True,
        "regex_type": "email",
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    {
        "field": "first_name",
        "type": str,
        "required": True
    },
    {
        "field": "last_name",
        "type": str,
        "required": True
    },
    {
        "field": "is_active",
        "type": bool,
        "required": True
    }
]
input_update_user = [
    {
        "field": "username",
        "type": str,
        "required": False
    },
    {
        "field": "password",
        "type": str,
        "required": False
    },
    {
        "field": "email",
        "type": str,
        "required": False,
        "regex_type": "email",
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    {
        "field": "first_name",
        "type": str,
        "required": False
    },
    {
        "field": "last_name",
        "type": str,
        "required": False
    },
    {
        "field": "is_active",
        "type": bool,
        "required": False
    }
]

input_login_user = [
    {
        "field": "username",
        "type": str,
        "required": True
    },
    {
        "field": "password",
        "type": str,
        "required": True
    }
]
