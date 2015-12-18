jasmin-monitor

Resource consumption monitoring tools for the JASMIN cloud.

Instructions

Before running the python script in crontab, need to create a folder in the top level called config and in that folder create a file called "r_config.ini"
Enter the following in the file
[config]
syspath : <pathtothesettings>
username : <username>
password : <password>
Make sure you enter the correct path to the django settings file and the username and password for the VCloudDirectory.

