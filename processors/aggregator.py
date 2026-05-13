from collections import defaultdict
from processors.row_object import RowObj

def minute_bucket(timestamp: str):
    return timestamp.replace(second=0)

def aggregate(rows: list[RowObj]):
    try:
        bars = {}

        for rowObj in rows:
            bucket = minute_bucket(rowObj.timestamp)

            key = (rowObj.instrument, bucket)

            bar = bars.get(key)

            if bar is None:
                bars[key] = {
                    "open": rowObj.price,
                    "high": rowObj.price,
                    "low": rowObj.price,
                    "close": rowObj.price,
                    "first_ts": rowObj.timestamp,
                    "last_ts": rowObj.timestamp,
                    "volume": rowObj.volume,
                    "pv_sum": rowObj.price * rowObj.volume,
                    "ticks": 1,
                }
                continue

            if rowObj.timestamp < bar["first_ts"]:
                bar["first_ts"] = rowObj.timestamp
                bar["open"] = rowObj.price

            if rowObj.timestamp > bar["last_ts"]:
                bar["last_ts"] = rowObj.timestamp
                bar["close"] = rowObj.price

            bar["high"] = max(bar["high"], rowObj.price)
            bar["low"] = min(bar["low"], rowObj.price)

            bar["volume"] += rowObj.volume
            bar["pv_sum"] += rowObj.price * rowObj.volume
            bar["ticks"] += 1
    except Exception as e:
        print("Exception with aggregating data: {}".format(e))

    return bars