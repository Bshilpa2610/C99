import os
import shutil
import time
path="/Users/Kunal/Desktop/python class/C99/new"
days=30
#current time
def main():
    seconds=time.time()
    deleted_folder_count=0
    deleted_file_count=0
    if os.path.exists(path):
    # print(os.walk(path))
        for root_folder, folders, files in os.walk(path):
            for name in files:
                print(os.path.join(root_folder,name))
            print("/n")
            for name in folders:
                print(os.path.join(root_folder,name))

        for root_folder, folders, files in os.walk(path):
        # for removing root_folder if age>30
            if seconds>=get_file_or_folder_age(root_folder):
                #remove_folder(root_folder)
                print('remove folder command')
                deleted_folder_count+=1
                break
            else:
                # check folders inside root folder
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        #remove_folder(root_folder)
                        print("remove folder command folder")
                        deleted_folder_count += 1
            
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if seconds>=get_file_or_folder_age(file_path):
                        #remove_folder(root_folder)
                        print("remove folder command file")
                        deleted_file_count += 1
    else:
        # file/folder is not found
        print(f'"{path}" is not found')
        deleted_file_count +=1

    print(f"Total folders deleted: {deleted_folder_count}")
    print(f"Total files deleted: {deleted_file_count}")

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)

def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)

def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	main()

