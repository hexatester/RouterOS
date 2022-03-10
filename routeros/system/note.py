import attr


@attr.dataclass
class Note:
    note: str
    show_at_login: bool
