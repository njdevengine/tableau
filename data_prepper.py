import os
import zipfile
# this file is not part of the assignment, its a series of scripts I used to unzip and combine all the files downloaded from citi
#make directories called "citi" and within that make "data" and within that "join_me"
dir_path = r"/citi//"

for path, dir_list, file_list in os.walk(dir_path):
    for file_name in file_list:
        if file_name.endswith(".zip"):
            abs_file_path = os.path.join(path, file_name)

            # The following three lines of code are only useful if 
            # a. the zip file is to unzipped in it's parent folder and 
            # b. inside the folder of the same name as the file

            parent_path = os.path.split(abs_file_path)[0]
            output_folder_name = os.path.splitext(abs_file_path)[0]
            output_path = os.path.join(parent_path, output_folder_name)

            zip_obj = zipfile.ZipFile(abs_file_path, 'r')
            zip_obj.extractall(output_path)
            zip_obj.close()
            
import os
import pandas as pd
d = r'/citi/data/'
paths = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]
for i in paths:
    x = i+"/"+i.split("/")[3]
    df = pd.read_csv(x)
    date = x.split("-")[2].split("/")[1]
    df.to_csv(d+"/"+date+".csv")

files = os.listdir(r"/citi/data/join_me")
array = []
for i in files:
    df = pd.read_csv(r"/citi/data/join_me/"+i)
    array.append(df)
