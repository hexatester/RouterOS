import attr


@attr.dataclass
class Clock:
    date: str
    dst_active: bool
    gmt_offset: str
    time: str
    time_zone_autodetect: bool
    time_zone_name: str
