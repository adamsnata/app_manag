import os

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории, где находится файл с которым работаем
TEST_DIR = os.path.join(CURRENT_DIRECTORY, 'tests') # делаем склейку пути к текущей директории и папки tests
RESOURCES_DIR = os.path.join(TEST_DIR, 'resources') # делаем склейку пути к текущей директории и папки resources
