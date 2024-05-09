import os
import json
main_directory = 'C:\\Users\\Administrator\\Documents\\SEC-API-Search-Engine\\masteridx'
info = {}
for folder in os.listdir(main_directory):
    for file in os.listdir(main_directory+"\\"+folder):
        file_path = main_directory+"\\"+folder+"\\"+file
        with open(file_path, "r") as file_content:
            l_previous = ""
            for l in file_content:
                if l.startswith("-"):
                    l_previous = l
                elif l_previous.startswith("-"):
                    temp = l.split("|")
                    info[temp[4][0:-1]] = {"CIK": temp[0], "Company Name": temp[1], "Form": temp[2], "Date Filed": temp[3]}
j = json.dumps(info, indent=4)
with open("ListOfFilings.json", "w") as outfile:
    outfile.write(j)