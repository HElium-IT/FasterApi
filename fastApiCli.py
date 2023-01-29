import os
import subprocess
import typer

import inflect
infl_eng = inflect.engine()
pluralize = infl_eng.plural

from utils import generate_file_from_template, modify_file, get_templates_dir, ModifyFileObj, APP_FOLDER, delete_generated_files, revert_modified_files
from error_handling_typer import ErrorHandlingTyper

app = ErrorHandlingTyper()


@app.error_handler(Exception)
def on_error(e):
    """
    This function is called when an error occurs
    """
    typer.echo("An error has occurred")

    typer.echo("Deleting generated files...")
    delete_generated_files()

    typer.echo("Reverting modified files...")
    revert_modified_files()

    typer.echo("The error was:")
    typer.echo(e)

    typer.echo("Exiting...")

@app.command()
def generate_router(router_name: str, class_name: str, output_path: str = None, api_version: str = "v1", auto_import: bool = True, template_type: str = None):
    pluralized_router_name = pluralize(router_name.split(".")[0])
    new_file_name = f"{pluralized_router_name}.py"
    if not output_path:
        output_path = os.path.join(
            APP_FOLDER, "api", f"api_{api_version}", "endpoints", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='router.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
            "class_name": class_name,
            "pluralized_router_name": pluralized_router_name,
        }
    )
    if auto_import:
        modify_file(
            os.path.join(APP_FOLDER, "api", f"api_{api_version}", "api.py"),
            ModifyFileObj(
                looking_for_string=f"from app.api.api_{api_version}.endpoints",
                to_add_string=f"from app.api.api_{api_version}.endpoints import {pluralized_router_name}",
            ),
            ModifyFileObj(
                looking_for_string=f"api_router = APIRouter()",
                to_add_string=f"api_router.include_router({pluralized_router_name}.router, prefix=\"/{pluralized_router_name}\", tags=[\"{pluralized_router_name}\"])",
            )
        )


@app.command()
def generate_crud(router_name: str, class_name: str, output_path: str = None, auto_import: bool = True, template_type: str = None):
    new_file_name = f"crud_{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "crud", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='crud.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
            "class_name": class_name
        }
    )
    if auto_import:
        modify_file(
            os.path.join(APP_FOLDER, "crud", "__init__.py"),
            ModifyFileObj(
                looking_for_string=None,
                to_add_string=f"from .crud_{router_name} import {router_name}",
            )
        )


@app.command()
def generate_schema(router_name: str, class_name: str, output_path: str = None, auto_import: bool = True, template_type: str = None):
    new_file_name = f"{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "schemas", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
        
    generate_file_from_template(
        template_file_name='schema.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "class_name": class_name
        }
    )
    if auto_import:
        modify_file(
            os.path.join(APP_FOLDER, "schemas", "__init__.py"),
            ModifyFileObj(
                looking_for_string=None,
                to_add_string=f"from .{router_name} import {class_name}, {class_name}Create, {class_name}Update, {class_name}InDBBase",
            )
        )


@app.command()
def generate_model(router_name: str, class_name: str, output_path: str = None, auto_import: bool = True, template_type: str = None):
    pluralized_router_name = pluralize(router_name)
    new_file_name = f"{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "models", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='model.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "class_name": class_name,
            "pluralized_router_name": pluralized_router_name,
        }
    )
    if template_type == "item":
        modify_file(
            os.path.join(APP_FOLDER, "models", "user.py"),
            ModifyFileObj(
                looking_for_string="if TYPE_CHECKING:",
                to_add_string=f"    from .{router_name} import {class_name}",
            ),
            ModifyFileObj(
                looking_for_string='items: List["Item"]',
                to_add_string=f'    {pluralized_router_name}: List["{class_name}"] = relationship("{class_name}", back_populates="owner")'
            )
        )
    if auto_import:
        modify_file(
            os.path.join(APP_FOLDER, "models", "__init__.py"),
            ModifyFileObj(
                looking_for_string=None,
                to_add_string=f"from .{router_name} import {class_name}",
            )
        )
        


@app.command()
def generate_router_test(router_name: str, api_version: str = None, output_path: str = None, template_type: str = None):
    new_file_name = f"test_{router_name}.py"
    if not api_version:
        api_version = "v1"
    if not output_path:
        output_path = os.path.join(
            APP_FOLDER, "tests", "api", f"api_{api_version}", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='test_router.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
            "api_version": api_version
        }
    )


@app.command()
def generate_crud_test(router_name: str, output_path: str = None, template_type: str = None):
    new_file_name = f"test_{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "tests", "crud", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='test_crud.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
        }
    )


@app.command()
def generate_utils_test(router_name: str, class_name: str, output_path: str = None, template_type: str = None):
    new_file_name = f"test_{router_name}.py"

    if not output_path:
        output_path = os.path.join(APP_FOLDER, "tests", "utils", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}.py"
    generate_file_from_template(
        template_file_name='test_utils.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
            "class_name": class_name,
        }
    )


@app.command()
def generate_tests(router_name: str, class_name: str = None, api_version: str = None, output_path: str = None, router: bool = True, crud: bool = True, template_type: str = None):
    if not class_name:
        class_name = router_name.title().replace("_", "")

    if router:
        generate_utils_test(router_name=router_name, class_name=class_name,
                            output_path=output_path, template_type=template_type)
        generate_router_test(router_name=router_name, api_version=api_version,
                             output_path=output_path, template_type=template_type)
    if crud:
        generate_crud_test(router_name=router_name,
                           output_path=output_path, template_type=template_type)


@app.command()
def generate_base():
    repo_url =  "https://github.com/HElium-IT/fastApiBase.git"
    repo_name = repo_url.split(os.sep)[-1].split(".")[0]
    os.chdir(os.getcwd())
    subprocess.run(["git", "clone", repo_url])
    print(f"Repository {repo_name} clonato con successo.")


@app.command()
def generate_bundle(router_name: str, class_name: str = None, output_path: str = None, auto_import: bool = True, router: bool = True, model: bool = True, schema: bool = True, crud: bool = True, template_type: str = None):
    if not class_name:
        class_name = router_name.title().replace("_", "")

    if router:
        generate_router(router_name=router_name, class_name=class_name,
                        output_path=output_path, auto_import=auto_import, template_type=template_type)
    if model:
        generate_model(router_name=router_name, class_name=class_name,
                       output_path=output_path, auto_import=auto_import, template_type=template_type)
    if schema:
        generate_schema(router_name=router_name, class_name=class_name,
                        output_path=output_path, auto_import=auto_import, template_type=template_type)
    if crud:
        generate_crud(router_name=router_name, class_name=class_name,
                      output_path=output_path, auto_import=auto_import, template_type=template_type)


@app.command()
def generate_bundle_and_tests(router_name: str, class_name: str = None, output_path: str = None, api_version: str = None, template_type: str = None):
    generate_bundle(router_name=router_name, class_name=class_name, output_path=output_path,
                    auto_import=True, router=True, model=True, schema=True, crud=True, template_type=template_type)
    generate_tests(router_name=router_name, class_name=class_name, api_version=api_version,
                   output_path=output_path, router=True, crud=True, template_type=template_type)


if __name__ == "__main__":
    app()
