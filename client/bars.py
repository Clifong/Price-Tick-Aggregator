import json
from datetime import datetime

ISO_FMT = "%Y-%m-%dT%H:%M:%SZ"

def parse_ts(ts):
    return datetime.strptime(ts, ISO_FMT)

def get_bars(
        path: str,
        instrument: str | None = None,
        start: str | None = None,  # ISO 8601, inclusive
        end: str | None = None,  # ISO 8601, exclusive
) -> list[dict]:
    start_ts = parse_ts(start) if start else None
    end_ts = parse_ts(end) if end else None

    results = []

    with open(path) as f:
        for line in f:
            row = json.loads(line)

            if instrument and row["instrument"] != instrument:
                continue

            ts = parse_ts(row["minute_bucket"])

            if start_ts and ts < start_ts:
                continue

            if end_ts and ts >= end_ts:
                continue

            results.append(row)

    return results