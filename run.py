import pandas as pd 
from row_validator import check_valid_and_depulicate
from writer import write_output
from aggregator import aggregate

INPUT = "./data/public_input.csv"
OUTPUT = "./data/output/output.ndjson"

def main():
    res = pd.read_csv(INPUT)
    filtered_rows = check_valid_and_depulicate(res)
    bars = aggregate(filtered_rows)
    write_output(OUTPUT, bars)

if __name__ == "__main__":
    main()