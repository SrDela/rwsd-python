def on_send_twoot(id_: str, user: User, content: str):
    user_id: str = user.get_id()
    twoot: Twoot = Twoot(id_, user_id, content)

    for follower in user.followers:
        if user.is_logged_on():
            follower.receive_twoot(twoot)