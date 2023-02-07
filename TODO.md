***--BUGS AND FIXES:***



***--REFACTOR:***

Create a new class for file handling which methods will be an abstraction of the utils function, this will allow the class to be used for other projects; this class will use the options file to manage variables that define the class behaviour.

Refactor modify_file function so that:
- opens, reads and closes file;
- handles the modifications outside the "open" scope;
- opens, writes and closes file.

Optimize generate_file_from_template function so that it just iterates once over the template content instead of using content.replace() on every argument passed to the function.

***--FEATURES:***

Add logging

Add generator for new version of the api

Add a function to revert last generation (there is the need to save the generated/modified files paths statically)
