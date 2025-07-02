from pathlib import Path

def get_extension(file_name):
  file = str(file_name)
  for i in range(len(file)):
    if file[i] == '.':
      return file[i:]
  

folder = Path("../test_files")
for inner in folder.iterdir():
  print(inner.name)
  print(get_extension(inner.name))
