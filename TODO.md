**--BUGS AND FIXES:



**--REFACTOR:

Move functions from utils into a new class that will handle files.

Refactor modify_file so that it opens file just to read/write and handles the modifications outside the "open" scope.

**--FEATURES:

Add logging

Add generator for new version of the api

Add a function to revert last generation (there is the need to save the generated/modified files paths statically)
