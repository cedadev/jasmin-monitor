JASMIN Monitoring System

Resource consumption monitoring tools for the JASMIN cloud.

***Instructions***

**Database**

The way the model is developed is by having two tables. One called collection and the other one called Resource. Collection table is a collection of all resource records collected during the same 'collection phase'.

First need to create a database using postresql. The instructions i used are from the following link.
"https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04"

**Config File**

Before running the python script in crontab, need to create a folder in the top level called config and in that folder create a file called "r_config.ini"
Enter the following in the file

[config]
syspath : <pathtothesettings>
username : <username>
password : <password>

Make sure you enter the correct path to the django settings file and the username and password for the VCloudDirectory.

**Fake Data**

To run the fake data make sure you make the changes suggested in the models.py file and run the makemigrations and migrate command to update the database. Revert it back once its done and update the database.

**Note**
get_resource_info.py is the file that needs to be setup in crontab to collect data from the VCloud Directory and save it in the database.

If more mertic_type needs to be added, make changes to the Resource class in models.py and also in the main.html file which can be found inside the templates folder in the monitoring_system folder.

