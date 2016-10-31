import tempfile  # временные файлы
import shutil  # операции над деревьями данных
from contextlib import contextmanager
import os


@contextmanager
def tempdir():                                                          # __init__
    outdir = tempfile.mkdtemp()  # создание временного каталога         # __enter__
    try:
        yield outdir
    except:
        pass
    finally:
        shutil.rmtree(outdir)  # удалиние дерева                        # __exit__


print(os.getcwd())  # текущий каталог
with tempdir() as path:
    print(path)
