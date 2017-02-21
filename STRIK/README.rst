===== 
Strik
=====

A simple webstore in development.

1. Add the strikapp to installed appls
INSTALLED_APPS = [
    ....
    'app',
]

2. Include in URLconf
url(r'^app/', include('app.urls)),

3. run 'python manage.py migrate'

4. start server and visit http://127.0.0.1:8000/admin/
to create new posts

5. visit http://127.0.0.1:8000/ to see the posts.