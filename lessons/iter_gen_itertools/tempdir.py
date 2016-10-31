import tempfile  # временные файлы
import shutil  # операции над деревьями данных
from contextlib import contextmanager
import os


@contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()  # создание временного каталога
    try:
        yield outdir
    except:
        pass
    finally:
        shutil.rmtree(outdir)  # удалиние дерева


print(os.getcwd())  # текущий каталог
with tempdir() as path:
    print(path)
