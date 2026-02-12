# Data Processor

A simple Python-based data processing pipeline component.

## Overview

The `data-processor` package provides a lightweight pipeline for transforming and filtering data records. It is designed to be easily integrated into larger systems or used as a standalone library.

## Features

- **Record Dataclass**: A structured way to represent data with an `index` and a `value`.
- **Transformation**: Convert records into a dictionary format with uppercased values.
- **Filtering**: Remove records that have empty or whitespace-only values.

## Installation

This package is intended to be used within the monorepo structure.

```bash
# From the root of the repository
cd packages/data-processor
pip install -e .
```

## Usage

### Record Structure

```python
from data_processor.pipeline import Record

record = Record(index=1, value="example data")
print(record.index)  # 1
print(record.value)  # "example data"
```

### Pipeline Functions

```python
from data_processor.pipeline import Record, transform, filter_empty

records = [
    Record(index=1, value="hello"),
    Record(index=2, value="  "),
    Record(index=3, value="world")
]

# Filter empty records
filtered = filter_empty(records)
# Result: [Record(index=1, value="hello"), Record(index=3, value="world")]

# Transform to dicts
output = transform(filtered)
# Result: [{"index": 1, "value": "HELLO"}, {"index": 3, "value": "WORLD"}]
```

## Testing

Run the unit tests to verify the pipeline functionality:

```bash
# From the data-processor directory
python3 -m unittest tests.test_pipeline

# Or run all tests
python3 -m unittest discover -s tests
```
