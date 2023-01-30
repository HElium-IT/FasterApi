This is a open-source project to speed up fastapi API development.
It uses premade app and customizable templates.

Project generation:
Use "generate-base" command to clone the base of the Api from the repository
https://github.com/HElium-IT/fastApiBase

Bundle generation:
Now go in the "app" folder of your fastapi application and use "generate-bundle"
command to generate router, model, schema, crud, and tests;
everything is auto-imported in the existing app.

Templates type (more will come):
base - default template with a simple class with the id property;
item - additional template, has also got an owner who can manage it.

The templates are in the folder /templates/{template_type}.
The tempaltes are fully editable to satisfy your needs.