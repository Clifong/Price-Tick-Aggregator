import pandas as pd 
from processors.row_validator import check_valid_and_depulicate
from processors.writer import write_output
from processors.aggregator import aggregate

INPUT = "./data/public_input.csv"
OUTPUT = "./data/output/output.ndjson"

def main():

    try:
        res = pd.read_csv(INPUT)
        filtered_rows = check_valid_and_depulicate(res)
        bars = aggregate(filtered_rows)
        write_output(OUTPUT, bars)
    except Exception as e:
        print("Exception with main process: {}".format(e))

if __name__ == "__main__":
    main()