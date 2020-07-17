from time import sleep
from datetime import datetime
from os import mkdir
from shutil import copy2

# Change these 3 lines to match your setup
PATH_TO_SAVE_FILE = '/home/USER/.steam/steam/steamapps/compatdata/374320/pfx/drive_c/users/steamuser/Application Data/DarkSoulsIII/0110000105b534ec/DS30000.sl2'
PATH_TO_BACKUP_FOLDER = '/run/media/USER/6801aa22-ffad-491f-a93e-f4d44c0ec73c/FolderHoldingSaves'
SAVE_TIMER = 5  # In Minutes


def create_new_save_folder(date):
    """
        Creates a folder with the name as 'date' to 'PATH_TO_BACKUP_FOLDER'.  
        Returns path to that new folder
    """
    path = PATH_TO_BACKUP_FOLDER + date
    mkdir(path)
    return path


def get_time():
    """
        Returns datetime.now() in format of YEAR-MONTH-DAY--HOUR:MINUTE:SECOND
    """
    return datetime.now().strftime("%Y-%m-%d--%H:%M:%S")


def copy():
    date = get_time()
    new_folder_path = create_new_save_folder(date)
    copy2(PATH_TO_SAVE_FILE, new_folder_path)
    print(f"{date}: Saved copy")


def main():
    while(True):
        copy()
        print(f"Waiting {SAVE_TIMER} minutes...")
        sleep(SAVE_TIMER * 60)


if __name__ == "__main__":
    main()
