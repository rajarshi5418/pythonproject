# reading all the csv file in directory
import os
from glob import glob

def get_csv_files(dir_path, ext):
    os.chdir(dir_path)
    return list(map(lambda x: os.path.join(dir_path, x), glob(f'*.{ext}')))

csv_file_list=get_csv_files(r"C:\Users\USER\PycharmProjects\pythonProject\importing_html\html-table-extraction-main", "csv")
for i in csv_file_list:
    print(i)


