import os
from pathlib import Path
CURRENT_FILE = Path(__file__).resolve()
CURRENT_DIR = CURRENT_FILE.parent
def ChangeRoot():
  os.chdir(CURRENT_DIR)
  
if __name__=='__main__':
  print(CURRENT_DIR,os.getcwd())
  print(f"Changing directory")
  ChangeRoot()
  
  print(CURRENT_DIR,os.getcwd())
  
  