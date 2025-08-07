from pathlib import Path
from . import constant
import shutil 
import os

def get_extension(file_name):
  file = str(file_name)
  for i in range(len(file) -1, -1, -1):
    if file[i] == '.':
      print(file)
      print(file[i:])
      return file[i:]
  
def group_by_type(files_path):
  files_path = Path(files_path) 
  TARGET_PATH = files_path / "WFM_Organized"
  if os.path.exists(TARGET_PATH):
    print("the WFM_Orfanized already exist... abortint")
    return
  
  os.makedirs(TARGET_PATH, exist_ok=True)
  for inner in files_path.iterdir():
    if inner.is_file():
      extension = get_extension(inner.name)
      if (extension in constant.SLIDE_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/slides_files", exist_ok=True)
        move_file(inner,(TARGET_PATH/"other_files/slides_files"))
      elif (extension in constant.DOC_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/docs_files", exist_ok=True)
        move_file(inner,(TARGET_PATH/"other_files/docs_files"))
      elif (extension in constant.COMPRESS_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/compress_files", exist_ok=True)
        move_file(inner,(TARGET_PATH/"other_files/compress_files"))
      elif (extension in constant.CODE_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/code_files", exist_ok=True)
        move_file(inner, (TARGET_PATH/"other_files/code_files"))
      elif (extension in constant.EXECUTABLE_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/executable_files", exist_ok=True)       
      elif (extension in constant.SHEET_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/sheet_files", exist_ok=True)        
        move_file(inner, (TARGET_PATH/"other_files/sheet_files"))
      elif (extension in constant.PDF_EXTENSION):
        os.makedirs(TARGET_PATH/"pdf_files", exist_ok=True)
        move_file(inner, (TARGET_PATH/"pdf_files"))
      elif (extension in constant.MEDIA_EXTENSION):
        os.makedirs(TARGET_PATH/"other_files/media", exist_ok=True)
        move_file(inner, (TARGET_PATH/"other_files/media"))


def move_file(file_to_move, target_directory):
  try:
    shutil.move(file_to_move, target_directory)
    print('SUCCES!!!')
  except Exception as e:
    print(f"Error moving file: {e}")




