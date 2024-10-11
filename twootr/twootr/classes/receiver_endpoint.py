from .twoot import Twoot


class ReceiverEndpoint:

    def on_twoot(self, twoot: Twoot) -> None:
        pass
