# TODO решите задачу
import json


def accumulate_sum_of_products(filename: str) -> float:
    with open(filename, "r") as file:
        data = json.load(file)
        product_list = [float(line['score']) * float(line['weight'])
                        for line in data]
        return float('%.3f' % sum(product_list))


filename = "input.json"
print(accumulate_sum_of_products(filename))
