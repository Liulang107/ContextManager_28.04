from datetime import datetime

# 1 вариант: с применением класса

class my_context_manager:
  def __init__(self, file_path):
    self.file_path = file_path
    self.create_time = datetime.now()

  def __enter__(self):
    self.file = open(self.file_path)
    return self.file

  def __exit__(self, exc_type, exc_vl, exc_tb):
    self.file.close()
    self.end_time = datetime.now()
    self.difference = self.end_time - self.create_time
    print(f'\nВремя запуска менеджера контекста: {self.create_time}')
    print(f'Время окончания работы менеджера контекста: {self.end_time}')
    print(f'Время работы менеджера контекста: {self.difference}')


# 2 вариант: с применением декоратора

from contextlib import contextmanager

@contextmanager
def my_open(file_path):
  try:
    file = open(file_path, 'w')
    start_time = datetime.now()
    yield file
  finally:
    end_time = datetime.now()
    difference = end_time - start_time
    file.write(f'\nВремя запуска менеджера контекста: {str(start_time)}\n')
    file.write(f'Время окончания работы менеджера контекста: {str(end_time)}\n')
    file.write(f'Время работы менеджера контекста: {str(difference)}')
    file.close()


if __name__ == '__main__':
  with my_open('Fibonacci.txt') as file:
    user_input = input('Введите длину последовательности Фибонначи n: ')
    file.write(f'Последовательность Фибонначи длиной {str(user_input)}:\n')
    a, b = 0, 1
    while a < int(user_input):
      file.write(f'{str(a)}\n')
      a, b = b, a + b
    print('Файл Fibonacci.txt записан')