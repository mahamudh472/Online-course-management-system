# My Course - Online course management system

## Overview
MyCourse is a web application that allows user to browse purchase and manage online courses. The platform offers an intuitive UI and structured course content to enhance the learning experience.

## Features
- User friendly Interface
- Secure user authentication
- Course listing and filtering
- Course purchase and enrollment
- Video and text based lessons
- Admin panel for course management

## Technologies used
- **Backend:** Django
- **Frontend:** Html, JS, Bootsrap
- **Database:** Sqlite3
- **Hosting:** render   

## Installation
1. Clone the repository:
```bash
git clone https://github.com/mahamudh472/Online-course-management-system.git
cd Online-course-management-system
```
2. Create virtual environmet:
```bash
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Apply migrations:
```bash
python manage.py migrate
```
5. Run the development server:
```bash
python manage.py runserver
```
6. Access the application at `http://127.0.0.1:8000/`

## API endpoints
> Not available yet

## Deployment guide
1. Set up production database (e.g., Postgesql).
2. Configure `settings.py` for production.
    - Set `DEBUG = False`
    - Configure `ALLOWED_HOSTS`
    - User environment variables for sensitive settings.
3. Collect Static.
```bash
python manage.py collectstatic
```
4. Deploy to your desired hosting with the hosting nessesary files.

## Contributors
- **Md Mahmud Hasan** - [Github](https://github.com/mahamudh472)

## License
The project is licensed under the MIT License.