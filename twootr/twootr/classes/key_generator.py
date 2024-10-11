import bcrypt
from typing import Union, Optional


class KeyGenerator:

    __SALT_LEN: int = 16

    def hash_(self, password: Union[str, bytes], salt: Optional[bytes] = None) -> bytes:
        if salt is None:
            salt = bcrypt.gensalt(self.__SALT_LEN)
        encoded_password: bytes = password.encode() if type(password) is str else password
        return bcrypt.hashpw(encoded_password, salt=salt)
