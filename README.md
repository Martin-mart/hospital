Patient Management System (PMS) - Django MVP
------------------------------------------------
Quick start
1. Create virtualenv
   python -m venv venv
   source venv/bin/activate   (Windows: venv\Scripts\activate)
2. Install requirements
   pip install -r requirements.txt
3. Copy .env.example to .env and update values
4. Create Postgres database and user matching .env
5. Run migrations
   python manage.py makemigrations
   python manage.py migrate
6. Create superuser
   python manage.py createsuperuser
7. Run server
   python manage.py runserver
Notes
- Static files use whitenoise for simple deployments.
- This scaffold gives a working MVP. Add production settings before deploy.
