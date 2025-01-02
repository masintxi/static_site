import os
import shutil
from markdown_to_html import markdown_to_html

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
            logger(f"Created public directory at --> {pub_dir}")

    delete_files(pub_dir)
    delete_folders(pub_dir)
    copy_files(stat_dir, pub_dir)

def delete_files(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
            logger(f"deleting file --> {item_path}")
        else:
            delete_files(item_path)

def delete_folders(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if len(os.listdir(item_path)) == 0:
            os.rmdir(item_path)
            logger(f"deleting directory --> {item_path}")
        else:
            delete_folders(item_path)

def copy_files(path, to_path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        item_to_path = os.path.join(to_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, item_to_path)
            logger(f"copying file --> {item_to_path}")
        else:
            os.mkdir(item_to_path)
            logger(f"copying directory --> {item_to_path}")
            copy_files(item_path, item_to_path)

def logger(msg):
    log_dir = os.path.join(os.getcwd(), "log.txt")
    with open(log_dir, "a") as log:
        log.write(f"{msg}\n")

def extract_title(markdown):
    if markdown[0:2] != "# ":
        raise Exception("No title found")
    return markdown.split("\n")[0][1:].strip()

def generate_page(from_path, template_path, dest_path):
    msg = f"Generating page from {from_path} to {dest_path} using {template_path}"
    print(msg)
    logger(msg)
    with open(from_path, "r") as file:
        markdown = file.read()
        logger(f"reading the markdown file: {from_path}")
    with open(template_path, "r") as file:
        template = file.read()
        logger(f"reading the template file: {template_path}")
    html_title = extract_title(markdown)
    html_string = markdown_to_html(markdown).to_html()
    template = template.replace("{{ Title }}", html_title)
    template = template.replace("{{ Content }}", html_string)
    with open(dest_path, "w") as file:
        file.write(template)
        logger(f"writing the HTML: {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        if os.path.isfile(item_path):
            if not os.path.exists(dest_dir_path):
                os.mkdir(dest_dir_path)
                logger(f"Created new directory at --> {dest_dir_path}")
            generate_page(item_path,
                          template_path, 
                          os.path.join(dest_dir_path, f"{item[:-3]}.html"))
        else:
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(item_path, template_path, new_dest_dir_path)

def main():
    site_prepare(os.getcwd())
    generate_pages_recursive(
        os.path.join(os.getcwd(), "content"), 
        os.path.join(os.getcwd(), "template.html"), 
        os.path.join(os.getcwd(), "public")
        )


main()
