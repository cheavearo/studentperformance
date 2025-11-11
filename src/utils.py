import os
import sys

from src.exception import StudentPerformanceException
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        
        # 'wb': signifies opening a file for writing in binary mode.
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise StudentPerformanceException(e,sys)

