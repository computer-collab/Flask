import os
from pathlib import Path
CURRENT_FILE = Path(__file__).resolve()
CURRENT_DIR = CURRENT_FILE.parent
PROJECT_ROOT = CURRENT_DIR.parent
def ChangeRoot():
  os.chdir(PROJECT_ROOT)
  return PROJECT_ROOT
  
if __name__=='__main__':
  print(CURRENT_DIR,os.getcwd())
  print(f"Changing directory")
  ChangeRoot()
  
  print(CURRENT_DIR,os.getcwd())
  
  