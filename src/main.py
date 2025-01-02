import os
import shutil

def site_prepare(path):
    pub_dir = os.path.join(os.getcwd(), "public")
    stat_dir = os.path.join(os.getcwd(), "static")
    log_dir = os.path.join(os.getcwd(), "log.txt")
    if path == os.getcwd():
        path = pub_dir
        if os.path.exists(log_dir):
            os.remove(log_dir)
            with open(log_dir, "x") as log:
                pass
        if not os.path.exists(pub_dir):
            os.mkdir(pub_dir)
            with open(log_dir, "a") as log:
                log.write(f"Created public directory at --> {pub_dir}\n")

    delete_files(pub_dir)
    delete_folders(pub_dir)
    copy_files(stat_dir, pub_dir)

def delete_files(path):
    log_dir = os.path.join(os.getcwd(), "log.txt")
    for item in os.listdir(path):
        item_path = path + "/" + item
        if os.path.isfile(item_path):
            os.remove(item_path)
            with open(log_dir, "a") as log:
                log.write(f"deleting file --> {item_path}\n")
        else:
            delete_files(item_path)

def delete_folders(path):
    log_dir = os.path.join(os.getcwd(), "log.txt")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if len(os.listdir(item_path)) == 0:
            os.rmdir(item_path)
            with open(log_dir, "a") as log:
                log.write(f"deleting directory --> {item_path}\n")
        else:
            delete_folders(item_path)

def copy_files(path, to_path):
    log_dir = os.path.join(os.getcwd(), "log.txt")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        item_to_path = os.path.join(to_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, item_to_path)
            with open(log_dir, "a") as log:
                log.write(f"copying file --> {item_to_path}\n")
        else:
            os.mkdir(item_to_path)
            with open(log_dir, "a") as log:
                log.write(f"copying directory --> {item_to_path}\n")
            copy_files(item_path, item_to_path)

def main():
    site_prepare(os.getcwd())

main()
