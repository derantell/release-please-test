from dataclasses import dataclass


@dataclass
class Record:
    id: int
    value: str


def transform(records: list[Record]) -> list[dict]:
    return [{"id": r.id, "value": r.value.upper()} for r in records]


def filter_empty(records: list[Record]) -> list[Record]:
    return [r for r in records if r.value.strip()]
