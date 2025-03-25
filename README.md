# Library Management System

## Project Overview
The Library Management System is a web-based application developed using Django. It provides CRUD functionalities for managing books and supports user authentication. This system is designed for two types of users:
- **Admin (Superuser)**: Can manage books and perform administrative tasks.
- **Students (Users)**: Can view the list of available books.

## Features
### Admin Features
1. **Admin Signup**
   - Register as an admin using an email and password.
   - Ensures unique email addresses.

2. **Admin Login**
   - Login with email and password.

3. **Book Management**
   - Add new books.
   - View all books.
   - Update existing book details.
   - Delete books.

4. **Django Admin Panel**
   - Access the admin panel at `/admin` for advanced management.

### Student Features
1. **View Books**
   - Browse the list of available books.

## How to Use the Site
### Admin (Superadmin)
1. **Signup**
   - Navigate to the signup page at `/register`.
   - Enter your email and password to create an admin account.

2. **Login**
   - Navigate to `/login`.
   - Enter your registered email and password to access the admin dashboard.

3. **Manage Books**
   - Use the book management section to:
     - Add a new book by providing details like title, author, publication date, and ISBN.
     - Update existing book details.
     - Delete unwanted books.

4. **Admin Panel**
   - Access advanced features via the Django admin panel at `/admin`.
   - Log in with the superuser credentials created using the `createsuperuser` command.

### Student (User)
1. **View Books**
   - Navigate to the homepage or `/books` to view the list of available books.
   - Students cannot perform CRUD operations.

## Setting Up the Project
### Prerequisites
- Python 3.x
- Django 4.x
- MySQL database

### Installation Steps
1. Clone the Repository:
   ```bash
   git clone <repository-url>
   cd library-management
   ```

2. Create and Activate a Virtual Environment:
   ```bash
   python -m venv env
   source env/bin/activate  
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Create a Superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the Server:
   ```bash
   python manage.py runserver
   ```
   Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Project Structure
- `manage.py`: Django's command-line utility.
- `settings.py`: Contains project configurations.
- `urls.py`: Defines URL patterns.
- `models.py`: Defines the database schema.
- `views.py`: Handles business logic.
- `templates/`: Contains HTML files for the frontend.
- `static/`: Contains CSS, JavaScript, and image files.

## Important Notes
- Ensure you have MySQL running before starting the server.
- Use strong passwords for both admin and superadmin accounts.
- Test the application thoroughly after deployment.

## Future Enhancements
- Implement user registration and login for students.
- Add a search functionality for books.
- Include pagination for the book list.
- Add RESTful APIs for external integrations.

## Contact
For any issues or suggestions, feel free to reach out at [support@librarysystem.com](mailto:support@librarysystem.com).

