import os

# Windows and linux slashes go in opposite directions.
# Uncomment the slash appropriate for your system.
systemslash='/'
# systemslash='\'

def get_list_of_files(inDirectory, container=[]):
    for entry in os.listdir(inDirectory):
        entry = inDirectory+systemslash+entry
        if os.path.isdir(entry):
            get_list_of_files(entry,container)
        filesize = os.path.getsize(entry)
        fileandsize = (filesize, entry)
        container.append(fileandsize)
    return container

Final_List_of_Files = get_list_of_files('/home/ubuntuclient/Downloads/')
Final_List_of_Files.sort(reverse=True)

print Final_List_of_Files[0]
