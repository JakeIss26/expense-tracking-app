[33mcommit 29cdceaeb516229b0cde0f1b3d09ad5735f55ef1[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/Jake[m[33m, [m[1;32mJake[m[33m)[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Sun May 18 17:12:18 2025 +0500

    Add unit tests for models and feature tests for views

[33mcommit 6173fb5db3d33d81142b81472798474f64bf907e[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Fri May 16 18:54:33 2025 +0500

    Add income and expense analytics charts by type and category

[33mcommit b9111dfc97a6fd30757ce1aa506ad4c3bdf7b6f7[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Sun Apr 27 17:59:31 2025 +0500

    Added Celery and Redis for background tasks, along with Django Channels and WebSockets for real-time chat and notifications
    Configured Celery with Redis as the message broker for background task execution.
    Implemented a background task to send a welcome email after user registration.
    Set up Django Channels for WebSocket communication.
    Created a WebSocket consumer for a chat with real-time message delivery.
    Implemented notification logic for all users connected to WebSocket through a message channel.

[33mcommit c1e2920b6cc015ac696c750b7feecd2883acb718[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Sun Apr 27 16:04:57 2025 +0500

    Created API for Expense model using Django REST Framework
    Created serializer for Expense model.
    Implemented CRUD operations via ViewSet.
    Set up routes for API endpoints.
    Tested API via Postman for GET, POST, PATCH, DELETE operations.

[33mcommit c3aa90eee50b585083f720278ce10b4493fbaa08[m[33m ([m[1;31morigin/Yaroslav[m[33m, [m[1;32mYaroslav[m[33m)[m
Author: Wwdebil <yarikmalcev096@gmail.com>
Date:   Sat Apr 26 17:33:28 2025 +0500

    Added Registration, Logging in/out, Profiles
    
    Added forms for registration and editing Profiles
    Created views for registration, logging in/out, profile, editing profile
    Added urls for registration, logging in/out, profile, editing profile
    Configured which views could be accessed only be registered users
    Created html templates for registration, logging in, profile, editing profile

[33mcommit 01f23d5355378f30d5834e41afea388e2ad933cf[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Apr 21 10:57:11 2025 +0500

    Fix: correct root URL routing to display expense list

[33mcommit 1693d96336fb5178de95c0d22587453bc6d43dbb[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Apr 21 10:24:37 2025 +0500

    Implement CRUD functionality for Expense model:
    
    Created views for listing, creating, updating, and deleting Expenses.
    Added a form for creating and updating Expenses.
    Developed templates for displaying the list of Expenses, creating/updating an Expense, and confirming deletion.
    Integrated Bootstrap for styling and improved UI.
    Configured URLs for all CRUD operations.
    Ensured proper redirection after successful create, update, and delete actions.

[33mcommit 8ebe33b613ebf066e478a0a31a0e9213cee2a4db[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Apr 21 09:22:10 2025 +0500

    Set up views, URLs, and templates for home and about pages
    Created superuser

[33mcommit eb6b0386d36b98909ca7701294270ca93147fe17[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Apr 14 10:50:58 2025 +0500

    Modified admin.py file

[33mcommit 8ed70f3a3b2ae2e64012adb8dca1a03292ba9d67[m
Author: Wwdebil <yarikmalcev096@gmail.com>
Date:   Mon Apr 7 14:44:17 2025 +0500

    Added records to models
    
    - Added 5 categories to Category model
    - Added 5 categories to Expense model

[33mcommit 624ef6608f263da3d275d9ede86cae35d2526b6d[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Apr 7 10:42:02 2025 +0500

    Created expense_tracker app
    Created Models for app
    Created and applied migrations
    Modified settings.py file

[33mcommit 915c91706f87419e042d09ddeb9771f79aa78ab3[m[33m ([m[1;31morigin/Bogdan[m[33m, [m[1;32mBogdan[m[33m)[m
Author: Jacob Issakov <yakov.issakov@gmail.com>
Date:   Mon Mar 31 10:54:11 2025 +0500

    Initial commit

[33mcommit 3966ca03f4cbf2c00b24747cd4af16ea85fb82d4[m
Author: JakeIss26 <136958746+JakeIss26@users.noreply.github.com>
Date:   Mon Mar 31 10:52:32 2025 +0500

    Initial commit
