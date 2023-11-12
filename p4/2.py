# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def convert_csv_to_json(input_filename, output_filename) -> None:
    with open(input_filename, 'r') as file:
        reader = csv.DictReader(file)  # TODO считать содержимое csv файла
        reader = list(reader)
    with open(output_filename, 'w') as file:
        intent = 4
        json.dump(reader, file, indent=intent)  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    convert_csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
