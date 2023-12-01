# Appidscanner
At the best of my knowledge, the current Apps manager of a certain software does not allow users to scan for their currently existing apps within the applist folder. Because I often leave my Applist folder untouched with the old ones, and because managing them can be lengthy, I made this python script which
scans for the files and displays their names by extracting the information from the Steam public API. It's not perfect, for some odd reasons it might not find the ID which is why I added a custom text to be printed that indicates it.


## Dependencies:
requests https://github.com/psf/requests

## How to use:

Simply put the file with the Redacted software folder and let it run. I did not add a check to see if you have the folder since I assumed anyone who use Redacted will have the folder inside, but feel free to change through the variable folderpath, leave everything else intact and run it.
