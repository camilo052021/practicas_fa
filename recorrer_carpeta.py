import os

folder_path = "C:/Users/caman/OneDrive/python"
file_list = os.listdir(folder_path)

for file_n in file_list:
    file_path=os.path.join(folder_path, file_n)
    if os.path.isfile(file_path):
        print(file_n)
