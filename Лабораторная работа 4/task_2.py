
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline='\n') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(row) for row in csv_reader]
    with open(OUTPUT_FILENAME, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, encoding="UTF-8") as output_f:
        for line in output_f:
            print(line, end="")
