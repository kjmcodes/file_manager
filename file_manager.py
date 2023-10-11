import os, shutil

root_folder = os.path.dirname(os.path.realpath(__file__))
root_folder = root_folder.replace("\\","/")
downloaded_items = os.listdir (root_folder)

for item in downloaded_items:
    name, type = os.path.splitext (item)

    type = f"{type[1:].upper()}s"
    new_folder = f"{root_folder}/{type}"

    if os.path.exists (new_folder):
            shutil.move(f"{root_folder}/{item}", f"{new_folder}/{item}")
    else:
            os.makedirs (new_folder)
            shutil.move (f"{root_folder}/{item}", f"{new_folder}/{item}")