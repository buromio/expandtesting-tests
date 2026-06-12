BASE_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["success", "status", "message"],
    "properties": {
        "success": {"type": "boolean"},
        "status": {"type": "integer"},
        "message": {"type": "string"},
    },
    "additionalProperties": True,
}

ERROR_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["success", "status", "message"],
    "properties": {
        "success": {"const": False},
        "status": {"type": "integer"},
        "message": {"type": "string"},
    },
    "additionalProperties": False,
}

NOTE_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "title",
        "description",
        "category",
        "completed",
        "created_at",
        "updated_at",
        "user_id",
    ],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "category": {"enum": ["Home", "Work", "Personal"]},
        "completed": {"type": "boolean"},
        "created_at": {"type": "string"},
        "updated_at": {"type": "string"},
        "user_id": {"type": "string", "minLength": 1},
    },
    "additionalProperties": False,
}

NOTE_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["success", "status", "message", "data"],
    "properties": {
        "success": {"const": True},
        "status": {"type": "integer"},
        "message": {"type": "string"},
        "data": NOTE_SCHEMA,
    },
    "additionalProperties": False,
}

NOTES_LIST_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["success", "status", "message", "data"],
    "properties": {
        "success": {"const": True},
        "status": {"type": "integer"},
        "message": {"type": "string"},
        "data": {"type": "array", "items": NOTE_SCHEMA},
    },
    "additionalProperties": False,
}
