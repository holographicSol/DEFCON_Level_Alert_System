# DEFCON_Level_Alert_System

A Nuke alarm.

Pulls down DEFCON levels and military news from https://www.defconlevel.com/ and stores the data locally in case offline.

Also pulls down data from NASA pertaining to annual mean global temperature and climate change.

(This system uses my advanced GUI template which is heavy duty and took me a lot of time to create).

Executable and source code:
https://drive.google.com/drive/folders/1jZ5BSDSzS3y-XOmMqLBpdVosY758MLKy?usp=sharing


Testing DEFCON 1 can be achieved by editing any DEFCON level in defcon_level.txt while disconnected
from internet.

All writes are protected to a certain degree to prevent existing data from being overwritten unecessarily/with-invalid-data, this is primarily to preserve existing stored data. This makes the need for a program update/upgrade more likely in the event that something on the server (defconlevel.com) changes and is preferrable to preserve exisiting data and attempt to prevent 'junk' from entering the front end and stored data.

Please be polite with the sychronize timings.
Defaults: DEFCON=3minutes, NASA=1hour.
