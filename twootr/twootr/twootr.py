from __future__ import annotations
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .classes import SenderEndpoint, ReceiverEndpoint


class Twootr:

    def on_logon(
        self,
        user_id: str,
        password: str,
        receiver: ReceiverEndpoint
    ) -> Optional[SenderEndpoint]:
        pass
