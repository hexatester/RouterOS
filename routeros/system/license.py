import attr


@attr.dataclass
class License:
    features: str
    nlevel: int
    software_id: str
