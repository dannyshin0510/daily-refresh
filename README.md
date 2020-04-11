**Description of Project**

The following application notifies users on the various insights and progressions of chosen subjects.
As an example, COVID-19 live tracker is included to illustrate the functionality of the notifier.

**TO USE:**
Create a config.py file in /daily-project with the following format:


EMAIL_ADDRESS = "<<FROM_EMAIL>>" \
PASSWORD = "<<EMAIL_PASSWORD>>" \
EMAIL_DESTINATIONS = ["<<DESTINATION_EMAIL>>"]


* Please note that the destination emails are in the format of an array, allowing multiple recipients.

OBJECT (Format)
The notification is in the format of HTML to maximize the developer's customizability. The file can be edited within: mail.html 

