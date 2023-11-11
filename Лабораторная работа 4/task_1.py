# TODO решите задачу
import json


def task() -> float:
    result = 0
    with open("./input.json") as f:
      data = json.load(f)
      for el in data:
        result += el["score"] * el["weight"]
      return round(result, 3)


print(task())
