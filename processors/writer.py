import json

def round6(x: float):
    return round(x, 6)

def write_output(path: str, bars: dict):
    try:
        items = sorted(bars.items())
        with open(path, "w") as f:
            for (instrument, bucket), bar in items:

                vwap = bar["pv_sum"] / bar["volume"]

                record = {
                    "instrument": instrument,
                    "minute_bucket": bucket.strftime("%Y-%m-%dT%H:%M:00Z"),
                    "open": round6(bar["open"]),
                    "high": round6(bar["high"]),
                    "low": round6(bar["low"]),
                    "close": round6(bar["close"]),
                    "vwap": round6(vwap),
                    "volume": int(bar["volume"]),
                    "ticks": int(bar["ticks"]),
                }

                f.write(json.dumps(record) + "\n")
    except Exception as e:
        print("Exception with writing to file: {}".format(e))