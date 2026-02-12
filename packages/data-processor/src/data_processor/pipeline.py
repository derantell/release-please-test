import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Record:
    index: int
    value: str


def transform(records: list[Record]) -> list[dict]:
    logger.info("Transforming %d records", len(records))
    return [{"index": r.index, "value": r.value.upper()} for r in records]


def filter_empty(records: list[Record]) -> list[Record]:
    result = [r for r in records if r.value.strip()]
    logger.info("Filtered %d -> %d records", len(records), len(result))
    return result
