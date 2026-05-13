from datetime import datetime
from processors.row_object import RowObj
from pandas import DataFrame

def parse_timestamp(date: str):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

def check_valid_and_depulicate(rows: DataFrame) -> list[RowObj]:
    best = {}
    dropped_rows = 0

    try:
        for row in rows.itertuples():
            try:
                timestamp = parse_timestamp(row[1].strip())
                instrument = row[2].strip()
                
                try:
                    price = float(row[3])
                    if price <= 0:
                        raise Exception("price is <= 0") 
                except:
                    raise Exception("price is not a float")  
                
                try:
                    volume = int(row[4])
                    if volume <= 0:
                        raise Exception("Volume is <= 0") 
                except:
                    raise Exception("Volume is not an integer") 
                
                source = row[5].strip()

                if not instrument:
                    raise Exception("Missing instrument")
                elif not source:
                    raise Exception("Missing source")
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
                dropped_rows += 1
                print("Exception occured for row {}: {}".format(row[0], e))
                pass
    except Exception as e:
        print("Exception with validating and deduplicating rows: {}".format(e))
    
    print("Number of dropped rows: {}".format(dropped_rows))
    return list(best.values())


