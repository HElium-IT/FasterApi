import os
import typer

from config import TEMPLATES_FOLDER, DEFAULT_TEMPLATE_TYPE
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))
APP_FOLDER = os.getcwd()


generated_file_paths = []
def delete_generated_files(*args):
    """
    > This function deletes the generated files from the dir_path
    
    :param file_names: The names of the files to delete
    :type file_names: list
    :param dir_path: The path to the folder where the files are stored
    :type dir_path: str
    """
    for file_path in generated_file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            typer.echo(f"{file_path} has been deleted.")

modified_files = []
def revert_modified_files():
    """
    > This function reverts the modified files to their original state
    """
    for file_path, original_content in modified_files:
        if os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(original_content)
            typer.echo(f"{file_path} has been reverted to its original state.")

def generate_file_from_template(*args, template_file_name: str, new_file_path: str, replacements: dict, env_key_char: str = None, templates_dir_path: str = None):
    """
    > This function takes a template file, replaces the placeholders with the values in the replacements
    dictionary, and saves the new file in the new_file_path
    
    :param template_file_name: The name of the template file to use
    :type template_file_name: str
    :param new_file_path: The path to the new file that will be generated
    :type new_file_path: str
    :param replacements: a dictionary of key-value pairs that will be replaced in the template file
    :type replacements: dict
    :param env_key_char: This is the character that will be used to identify the keys in the template
    file, defaults to $$ (optional)
    :param templates_dir_path: The path to the folder where the template files are stored
    :type templates_dir_path: str
    """
    if not env_key_char:
        env_key_char = "$$"
    
    if os.path.exists(new_file_path):
        typer.confirm(f"{new_file_path} already exists, do you want to overwrite it?", abort=True)
        os.remove(new_file_path)

    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    
    with open(os.path.join(templates_dir_path, template_file_name), 'r') as f:
        content = f.read()

    for key, item in replacements.items():
        content = content.replace(f"{env_key_char}{key}{env_key_char}", item)
    
    with open(os.path.join(new_file_path), 'w') as f:
        f.write(content)
    
    generated_file_paths.append(new_file_path)
    typer.echo(f"'{new_file_path.split(os.sep)[-1]}' has been generated and saved in '{new_file_path}'.")


class ModifyFileObj:
    looking_for_string:str
    to_add_string:str
    add_before:bool
    def __init__(self, looking_for_string:str, to_add_string:str, add_before:bool = False):
        self.looking_for_string = looking_for_string
        self.to_add_string = to_add_string
        self.add_before = add_before

def modify_file(file_path:str, *args):
    """
    It takes a file path and a list of objects that have a string to add and a string to look for. If
    the string to look for is not found, the string to add is added to the top of the file. If the
    string to look for is found, the string to add is added either before or after the string to look
    for
    
    :param file_path: The path to the file you want to modify
    :type file_path: str
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")

    with open(file_path, "r+") as f:
        content = f.read()
        modified_files.append((file_path, content))
        lines = content.splitlines()
        for obj in args:
            if not obj.looking_for_string:
                lines.insert(0, obj.to_add_string)
                continue
            for i, line in enumerate(lines):
                if line.startswith(obj.looking_for_string):
                    if obj.add_before:
                        lines.insert(i, obj.to_add_string)
                    else:
                        lines.insert(i + 1, obj.to_add_string)
                    break
            else:
                if obj.add_before:
                    lines.insert(0, obj.to_add_string)
                else:
                    lines.append(obj.to_add_string)
        f.seek(0)
        f.write("\n".join(lines))
    typer.echo(f"{file_path} has been modified.")


def get_templates_dir(template_type: str = None):
    return os.path.join(THIS_FOLDER, TEMPLATES_FOLDER, template_type or DEFAULT_TEMPLATE_TYPE)