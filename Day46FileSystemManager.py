import os
import shutil
import datetime

# CLaude function answer
#  def file_system_manager():
#     "
#     A simple file system manager that demonstrates various os module functions.
#     "
#     # Create a base directory for our exercise
#     base_dir = "file_system_exercise"
    
#     # Check if directory exists, remove if it does
#     if os.path.exists(base_dir):
#         print(f"Removing existing directory: {base_dir}")
#         shutil.rmtree(base_dir)
    
#     # Create the base directory
#     os.mkdir(base_dir)
#     print(f"Created directory: {base_dir}")
    
#     # Change current working directory to our base directory
#     os.chdir(base_dir)
#     print(f"Current working directory: {os.getcwd()}")
    
#     # Create a nested directory structure
#     nested_dirs = os.path.join("data", "logs", "daily")
#     os.makedirs(nested_dirs)
#     print(f"Created nested directories: {nested_dirs}")
    
#     # Create some sample files
#     for i in range(1, 4):
#         file_path = os.path.join("data", f"sample{i}.txt")
#         with open(file_path, "w") as f:
#             f.write(f"This is sample file {i}")
#         print(f"Created file: {file_path}")
    
#     # Create a log file with timestamp
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     log_file = os.path.join("data", "logs", f"log_{timestamp}.txt")
#     with open(log_file, "w") as f:
#         f.write(f"Log created at {timestamp}")
#     print(f"Created log file: {log_file}")
    
#     # List contents of directories
#     print("\nContents of base directory:")
#     for item in os.listdir("."):
#         item_path = os.path.join(".", item)
#         if os.path.isdir(item_path):
#             print(f"  Directory: {item}")
#         else:
#             print(f"  File: {item}")
    
#     print("\nContents of data directory:")
#     for item in os.listdir("data"):
#         item_path = os.path.join("data", item)
#         if os.path.isdir(item_path):
#             print(f"  Directory: {item}")
#         else:
#             print(f"  File: {item}")
    
#     # Rename a file
#     old_path = os.path.join("data", "sample1.txt")
#     new_path = os.path.join("data", "renamed_sample.txt")
#     os.rename(old_path, new_path)
#     print(f"\nRenamed: {old_path} -> {new_path}")
    
#     # Print environment variables
#     print("\nSome environment variables:")
#     print(f"  HOME: {os.environ.get('HOME', 'Not set')}")
#     print(f"  PATH: {os.environ.get('PATH', 'Not set')[:50]}...")  # Truncated for brevity
#     print(f"  PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
    
#     # Display platform information
#     print(f"\nOperating system: {os.name}")
    
#     # Return to original directory
#     os.chdir("..")
#     print(f"\nReturned to directory: {os.getcwd()}")
    
#     # Optional: Clean up the exercise directory
#     # Uncomment the following line to remove the exercise directory when done
#     # shutil.rmtree(base_dir)
#     # print(f"Removed directory: {base_dir}")

def file_system_manager():
    '''
    a simple file system manager that using os modules function
    
    '''
    # Create base directory for our file
    base_dir = "file_system_exercise"

    #Check if directory exists and delete

    if os.path.exists(base_dir):
        print(f"Removing existing directory: {base_dir}")
        shutil.rmtree(base_dir)

    #Create base directory
    os.mkdir(base_dir)
    print(f"Created directory: {base_dir}")

    # Change current directory to our base directory
    os.chdir(base_dir)

    # Create nested directory structure
    nested_dirs = os.path.join("data","logs","daily")
    os.mkdir(nested_dirs)
    print(f"Created nested directory: {nested_dirs}")

    





if __name__ == "__main__":
    file_system_manager()