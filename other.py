from typing import Dict, Any

class Newsession:
    def __init__(self) -> None:
        self.session: Dict[str, Dict[str, Any]] = {}
        self.inheritance = self.Usertime(self.session)

    def user_add(self, user_uuid: str) -> None:
        self.session[user_uuid] = {
            'Room': '',
            'Connected': False,
        }

    def user_delete(self, user_uuid: str) -> None:
        self.session.pop(user_uuid, None)

    def get_user_exist(self, user_uuid: str) -> bool:
        if self.session.get(user_uuid, None) is not None:
            return True
        else:
            return False

    def get_user_room(self, user_uuid: str) -> str | None:
        return self.session.get(user_uuid, {}).get('Room', None)

    def get_user_connected(self, player_uuid: str) -> bool | None:
        return self.session.get(player_uuid, {}).get('Connected', None)



    class Usertime:
        def __init__(self, session,  timelimit: int = 10, time_interval: float | int = 1) -> None:
            self.session = session
            self.time: Dict[str, int | float] = {}
            self.timelimit: int = timelimit
            self.time_interval: float | int = time_interval

        def add_user(self, user_uuid: str) -> None:
            self.time[user_uuid] = 0

        def remove_user(self, user_uuid: str) -> None:
            self.time.pop(user_uuid, None)

        def reset_user_timer(self, user_uuid: str) -> None:
            self.time[user_uuid] = 0

        def user_timer_up(self) -> None:
            for x in self.time:
                if self.user_over_timelimit(x) is False:
                    self.time[x] += self.time_interval

        def user_over_timelimit(self, user_uuid: str) -> bool:
            if self.time[user_uuid] >= self.timelimit:
                return True
            else:
                return False


container = Newsession()
container.user_add("Gamer")
container.get_user_room("")
container.inheritance.add_user("Gamer")
print(container.get_user_connected("Gamer"))
print(container.inheritance.time)