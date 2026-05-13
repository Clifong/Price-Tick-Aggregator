from datetime import datetime
from processors.row_object import RowObj
from pandas import DataFrame

def parse_timestamp(date: str):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

def check_valid_and_depulicate(rows: DataFrame) -> list[RowObj]:
    best = {}
    for row in rows.itertuples():
        try:
            timestamp = parse_timestamp(row[1].strip())
            instrument = row[2].strip()
            price = row[3]
            volume = row[4]
            source = row[5].strip()

            if not isinstance(price, float) or price <= 0:
                continue 
            elif not isinstance(volume, int) or volume <= 0:
                continue 
            elif not instrument or not source:
                continue 
            elif len(row) != 6: 
                continue
            
            rowObj = RowObj(
                    timestamp=timestamp,
                    instrument=instrument,
                    price=price,
                    volume=volume,
                    source=source
                )
            key = (timestamp, instrument)
            existing = best.get(key)
            if existing is None:
                best[key] = rowObj
                continue

            if rowObj.volume > existing.volume:
                best[key] = rowObj
        except Exception as e:
            pass
    return list(best.values())


