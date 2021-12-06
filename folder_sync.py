from dirsync import sync

source_path = input("Enter source path: ")
dest_path = input("Enter destination path: ")

sync(source_path, dest_path, 'sync', purge=True)