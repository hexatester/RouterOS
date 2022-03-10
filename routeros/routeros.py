import attr


@attr.dataclass
class RouterOS:
    username: str
    password: str
    url: str
