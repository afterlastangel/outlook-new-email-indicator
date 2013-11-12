outlook-new-email-indicator
=================

This app make Notification when received email from outlook on different machine.
Need python packages:
appindicator
pynotify
Test on ubuntu 12.04.3

How to use: 
Add python script into  startup application:  python ~/check_outlook.py
Add new VBA for Outlook (On Outlook use Alt + F11)
Change URL to the correct IP and port of notification machine
Add new rule for every email receive in Outlook with action Run a script.


