***--BUGS AND FIXES:***
  FILE: \backend\app\schemas\token.py
  BUG: sub is not an integer, is a string containing the user_id
  EFFECT: every request returns 403 Forbidden


***--REFACTOR:***

Create a new FileHandling class which methods will be an abstraction of the utils functions, this will allow the class to be used for other projects; this class will use an Options class to manage all the variables that define the main class behaviour.

Refactor modify_file function so that:
- opens, reads and closes file;
- handles the modifications outside the "open" scope;
- opens, writes and closes file.

Optimize generate_file_from_template function so that it just iterates once over the template content instead of using content.replace() on every argument passed to the function.

***--FEATURES:***

Add logging

Add generator for new version of the api

Add a function to revert last generation (there is the need to save the generated/modified files paths statically)

***--NOTES:***

Templates dir will not be handleable for user customization when project will be packaged into a python module.

The cli is working on Windows, but is it working on other operating systems?

The cli is working for python v3.9.13, but is it working for all v3 subversions?
