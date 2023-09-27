input_create_task = [
    {
        "field": "title",
        "type": str,
        "required": True
    },
    {
        "field": "expiration_date",
        "type": str,
        "required": True
    },
    {
        "field": "status",
        "type": str,
        "required": True,
        "options": ["TODO","IN_PROGRESS", "DONE"]
    },
    {
        "field": "user_id",
        "type": int,
        "required": False
    }
]
input_update_task = [
    {
        "field": "title",
        "type": str,
        "required": False
    },
    {
        "field": "expiration_date",
        "type": str,
        "required": False
    },
    {
        "field": "status",
        "type": str,
        "required": False,
        "options": ["TODO","IN_PROGRESS", "DONE"]
    },
    {
        "field": "user_id",
        "type": int,
        "required": False
    }
]
