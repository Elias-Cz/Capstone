INSTALLERS

Mock up for a web-based scheduling system for a fictional installation company.

As opposed to the other projects in this course, this project contains several key differences in areas such as user models and views. One of these main differences is that there are multiple types of users. Both user types (installer and customer) have different permissions, and view/access the same routes/pages in different ways. Another key area which differentiates this project is the way certain functions are used such as "monthrange()", which in short allows the web app to always know what month it is, and return that data to the user 

Users or "customers" are able to create accounts, log in and schedule an installation date from a calendar. Users can also cancel existing appointments as well as see the name of the installer they've been assigned for future appointments. Calendar automatically updates based on the month, every time a user views the schedule route.

Superusers can change user permissions to "installer". Users classified as installers, would theoretically be assigned to employees of the fictional company, and logging in would allow them to see any upcoming projects they've been assigned to, as well as any extra details. Installers CANNOT schedule appointments.





Other details:

Made use of media queries to change two-column layout to single-column layout on mobile.

Calendar automatically updates using monthrange(), and references a day and month array.

check_perms is used throughout to check if a user is an installer or not, and displays data accordingly.

Made use of random() to randomly select installers for an appointment.
