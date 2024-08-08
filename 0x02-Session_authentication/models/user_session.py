#!/usr/bin/env python3
from models.base import BaseModel

class UserSession(BaseModel):
    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.get("user_id")
        super().__init__(*args, **kwargs)
