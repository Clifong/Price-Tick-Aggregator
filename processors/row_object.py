import datetime

class RowObj:
    def __init__(self, timestamp: datetime, price: float, volume: int, instrument: str, source: str):
        self.timestamp = timestamp
        self.price = price 
        self.volume = volume
        self.instrument = instrument
        self.source = source