#  Versioned Folder Backup Tool
This tiny utility will create versioned zip backups (Inspired by the book 'Automating the boring stuff with python').

- I made it so a user can simply copy the script inside the folder that needed to be backed up.
- The script then will create a zip file in the parent directory and detects the current backups that already exists and increments the file number.
- Then a loop will walk over every file and folder to store a snapshot into one archive file.
