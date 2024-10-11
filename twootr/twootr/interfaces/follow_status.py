from enum import Enum


class FollowStatus(Enum):
    SUCCESS: int = 1
    INVALID_USER: int = 2
    ALREADY_FOLLOWING: int = 3
