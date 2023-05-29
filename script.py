import os
import time
from fire import Fire


def add_config(file_path, text):
  open(file_path, 'w+').write(text)
