INSTALLERS

Mock up for a web-based scheduling system for a fictional installation company.

Users or "customers" are able to create accounts, log in and schedule an installation date from a calendar. Users can also cancel existing appointments as well as see the name of the installer they've been assigned for future appointments. Calendar automatically updates based on the month, every time a user views the schedule route.

Superusers can change user permissions to "installer". Users classified as installers, would theoretically be assigned to employees of the fictional company, and logging in would allow them to see any upcoming projects they've been assigned to, as well as any extra details. Installers CANNOT schedule appointments.



Other details:

Made use of media queries to change two-column layout to single-column layout on mobile.

Calendar automatically updates using monthrange(), and references a day and month array.

check_perms is used throughout to check if a user is an installer or not, and displays data accordingly.

Made use of random() to randomly select installers for an appointment.
