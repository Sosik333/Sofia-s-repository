import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_f:
        reader = csv.DictReader(input_f)
        records = list(reader)
        with open(OUTPUT_FILENAME, "w") as output_f:
            data = json.dump(records, output_f, indent=4)
    return data


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
