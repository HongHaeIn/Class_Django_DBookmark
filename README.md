#DBookmark
- project/urls.py -> app/urls.py -> views.py -> -> templates/app/index.html
- admin.py : 관리자 사이트
- form.py : 입력 사이트
- 개발 순서 : models.py, views.py, urls.py, templates
1. startproject DBookmark
   1. python -m pip install django~=3.2
   2. django-admin startproject DBookmark .
   3. python manage.py runserver
2. startapp bookmark
   1. python manage.py startapp bookmark
   2. add 'bookmark', to INSTALLED_APP in settings.py
3. bookmark/models.py Bookmark
   1. python manage.py makemigrations bookmark
      1. models -> DB로 옮기기 위한 py
   2. python manage.py migrate
      1. DB테이블 만들기
   3. bookmark/admin Bookmark
      1. python manage.py createsuperuser
      2. bookmark/models Bookmark \__str\__()
   4. bookmark/views BookmarkListView
   5. bookmark/urls bookmark:list
   6. templates bookmark_list.html
   7. bookmark/views BookmarkCreateView
   8. urls, bookmark/urls bookmark:add
   9. templates boookmark_create.html
