import json
import ContextManager

with ContextManager.my_context_manager('Recipes.txt') as f:
  cook_book = {}
  for line in f:
    dish = line.strip()
    ingridients_number = int(f.readline().strip())
    cook_book[dish] = []
    ingridient_dict = {}
    while ingridients_number:
      ingridient_line = f.readline().strip()
      ingridient = ingridient_line.split(' | ')
      ingridient_dict = {'ingridient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
      cook_book[dish].append(ingridient_dict)
      ingridients_number -= 1
    f.readline()
  print(json.dumps(cook_book, ensure_ascii=False, indent=2))