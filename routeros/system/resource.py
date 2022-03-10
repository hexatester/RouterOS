import attr


@attr.dataclass
class Resource:
    architecture_name: str
    bad_blocks: int
    board_name: str
    build_time: str
    cpu: str
    cpu_count: int
    cpu_frequency: int
    cpu_load: int
    factory_software: str
    free_hdd_space: int
    free_memory: int
    platform: str
    total_hdd_space: int
    total_memory: int
    uptime: str
    version: str
    write_sect_since_reboot: int
    write_sect_total: int
