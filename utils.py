import os
import typer

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
    
    typer.echo(f"{new_file_path.split(os.sep)[-1]} has been generated and saved in {new_file_path}.")


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
