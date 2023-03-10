# BABE_API
Django API for BABE APP
BACKEND INSTALL:
1. Clone this repository to your PC
2. Run windows.bat file
In the new opened terminal with (myvenv) go back to thr root folder (BABE_API) and run poetry install 
3. From the root directory (BABE_API) run python manage.py migrate
4. From the root directory (BABE_API) run python manage.py runserver


The backend side you can use as API, making requests to:
1. Create new user - POST - http://127.0.0.1:8000/api-auth-djoser/users/ (required fields: email, username, password,re_password)
2. Login user with jwt token - POST - http://127.0.0.1:8000/api-auth-djoser/token/login/ (required fields: username, password)- will receive TOKEN
3. Update user profile-PATCH - http://127.0.0.1:8000/api/user/profile/<int:id>/ (required header:Authorization Token ........)
4. Logout -POST- http://127.0.0.1:8000/api-auth-djoser/token/logout/ (required header:Authorization Token ........)
5. Get user Info -GET- http://127.0.0.1:8000/api-auth-djoser/users/me/ (required header:Authorization Token ........)
6. Get profile info by user ID - GET - http://127.0.0.1:8000/api/profiles/<int:id>/  (required header:Authorization Token ........)
7. Create pet member for authorized user - POST -  http://127.0.0.1:8000/api/listings/create/ (required header:Authorization Token ........)
8. Update pet member for authorized user - PATCH - http://127.0.0.1:8000/api/listings/update/<int:id>/  (required header:Authorization Token ........)
9. Delete pet member for authorized user - DELETE - http://127.0.0.1:8000/api/listings/delete/<int:id>/ (required header:Authorization Token ........)
10. See pet member information that includes user (owner) information - GET - http://127.0.0.1:8000/api/listings/info/<int:id>/
