INSTALLERS

Mock up for a web-based scheduling system for a fictional installation company.

As opposed to the other projects in this course, this project contains several differences in key areas such as user models and views. One of these main differences is that there are multiple types of users. Both user types (installer and customer) have different permissions, and view/access the same routes/pages in different ways. Another type of user is the superuser or admin, which can update and edit appointments as well as give other users permissions. Another key area which differentiates this project is the way certain functions are used such as "monthrange()", which helps to find out how many days are in a month. Also there is a function which in short allows the web app to always know what month it is, and return that data to the user; it does this by referencing an array of months and converting an integer to a string and using that value in the monthrange() function.

This project also makes use of media queries, which none of the other projects did. Additionally, on the front end, the project makes use of pop-ups or modals, as well as redirects to enhance the user experience. The calendar which is used to schedule appointments is interactive as well, and makes use of template for-loops to display the correct number for each respective day. This calendar also automatically updates to the correct month.

Users or "customers" are able to create accounts, log in and schedule an installation date from a calendar. Users can also cancel existing appointments as well as see the name of the installer they've been assigned for future appointments. Calendar automatically updates based on the month, every time a user views the schedule route. As mentioned before, superusers can change user permissions to "installer". Users classified as installers, would theoretically be assigned to employees of the fictional company, and logging in would allow them to see any upcoming projects they've been assigned to, as well as any extra details. Installers CANNOT schedule appointments.

Views.py contains the main logic to the scheduling app. The register, login and logout views facilitate all user logins and account creations. The profile view first check to see if a user is classified as an "installer" or a normal user. Installers are redirected to the installer view, where they can see upcoming installations as well as cancel or mark installations as complete. If the user is a normal user, this page is where they see all their scheduled projects, as well as make cancellations. The schedule view is where the main scheduling occurs. This is also where the app makes use of the monthrange() function, to return the correct info to users. The "months" array is also used in this view, in order to return the correct month name to the user. The appointments view is another way to view any upcoming appointments.

Urls.py has all the available routes which users can access. The urls.py file which exists in the Capsone directory ensures the paths within installers.urls are all accessible to users.

Models.py contains the two main models in which user data and schedule dates are stored. This also contains the user permission functionality which is a BooleanField (which hasnt been used in any of the past projects).

Admin.py has been modified to allow superusers to log into the sites admin dashboard for further management of schedules and user types.

All templates are stored in the templates/installers directory.

In the static/installers directory are main.js and style.css. Main.js contains the functionality for the modals/popups, as well as aiding in the redirects which are used throughout the app. Style.css contains all style code which includes media queries, which have not been used in any of the past projects.
