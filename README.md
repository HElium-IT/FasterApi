# FasterApi

This is a open-source project to speed up fastapi API development. It uses premade app and customizable templates.

## Environment setup

To setup python environment just run this 3 commands inside the cloned repository folder.

```
python3 -m venv venv\
.\venv\Scripts\activate
python3 -m pip install -r requirements.txt
```

## Usage

To use the cli use:

```
python3 {path to fasterApi.py} {command}".
```

If you are in the project folder, try getting help like this:

```
python3 ./fasterApi.py --help
```

WIP: Later the cli will have the capability to be installed and used with "fasterapi {command}"

## Project Generation

Use "generate-base" command to clone the base of the Api from the repository https://github.com/HElium-IT/fastApiBase .

```
python3 ./fasterApi.py generate-base
```

## API Start

To start the API open a new terminal in the "fastApiBase" folder and run:

```
docker compose up
```

After the build is finished and you read " INFO: Application startup complete." you can go to http://localhost:8000/docs .

## Bundle generation

From the "app" folder of your fasterApi application use "generate-bundle" command to generate router, model, schema, crud, and tests; everything is auto-imported in the existing app.

Example (from cloned repository folder):

```
cd .\fastApiBase\backend\app
python ..\..\..\fasterApi.py generate-bundle group
```

## Template types (more will come):

- base: default template with a simple class with the id property;
- item: additional template, class with a linked owner who can manage it.

The templates are in the folder /templates/{template_type} and are fully editable to satisfy your needs.
