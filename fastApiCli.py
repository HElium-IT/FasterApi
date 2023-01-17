import os
import typer
from utils import ModifyFileObj, generate_file_from_template, modify_file
from config import TEMPLATES_FOLDER, DEFAULT_TEMPLATE_TYPE

APP_FOLDER = os.path.join(os.getcwd())
THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))

app = typer.Typer()

# add a control to manage exceptions

def get_templates_dir(template_type: str = None):
    return os.path.join(THIS_FOLDER, TEMPLATES_FOLDER, template_type or DEFAULT_TEMPLATE_TYPE)

@app.callback()
def main(ctx: typer.Context):
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = True


@app.command()
def generate_router(router_name: str, class_name: str, output_path: str = None, api_version: str = "v1", auto_import: bool = True, template_type: str = None):
    new_file_name = f"{router_name}.py"
    if not output_path:
        output_path = os.path.join(
            APP_FOLDER, "api", f"api_{api_version}", "endpoints", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}"
    generate_file_from_template(
        template_file_name='router.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "router_name": router_name,
            "class_name": class_name
        }
    )
    if auto_import:
        modify_file(
            os.path.join(APP_FOLDER, "api", f"api_{api_version}", "api.py"),
            ModifyFileObj(
                looking_for_string=f"from app.api.api_{api_version}.endpoints",
                to_add_string=f"from app.api.api_{api_version}.endpoints import {router_name}",
            ),
            ModifyFileObj(
                looking_for_string=f"api_router = APIRouter()",
                to_add_string=f"api_router.include_router({router_name}.router, prefix=\"/{router_name}\", tags=[\"{router_name}\"])",
            )
        )


@app.command()
def generate_crud(router_name: str, class_name: str, output_path: str = None, auto_import: bool = True, template_type: str = None):
    new_file_name = f"crud_{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "crud", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}"
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
        output_path = f"{output_path}{os.sep}{new_file_name}"
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
    new_file_name = f"{router_name}.py"
    if not output_path:
        output_path = os.path.join(APP_FOLDER, "models", new_file_name)
    if not output_path.endswith(".py"):
        output_path = f"{output_path}{os.sep}{new_file_name}"
    generate_file_from_template(
        template_file_name='model.tpl',
        templates_dir_path=get_templates_dir(template_type),
        new_file_path=output_path,
        replacements={
            "class_name": class_name
        }
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
        output_path = f"{output_path}{os.sep}{new_file_name}"
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
        output_path = f"{output_path}{os.sep}{new_file_name}"
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
        output_path = f"{output_path}{os.sep}{new_file_name}"
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
