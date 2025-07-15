📝 Django To-Do List App
A fully-featured To-Do List web app built with Django.
Users can register, log in, and manage their own personal tasks with filtering, editing, and search support.

🚀 Features
✅ User Registration and Login (Authentication)
➕ Add tasks with optional due date and priority
🖊️ Edit and update existing tasks
✅ Mark tasks as completed
🗑️ Delete tasks
🔍 Search tasks by title
📁 Filter tasks (All, Completed, Pending)
👤 User-specific task list (only see your own tasks)
🎨 Clean UI with Bootstrap 5

📸 Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e7cff60b-2ccd-422a-ad0a-011d595d2818" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6341befc-5f86-407e-9f67-9db1e88aa16f" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9291cefa-e0b0-455a-8f8a-03f3a62802da" />


🛠️ Tech Stack
Backend: Django 5
Frontend: HTML, Bootstrap 5
Database: SQLite (default)

📦 Installation & Setup
# Clone the repo
git clone https://github.com/JayaSurya08-dev/todo-django.git
cd todo-django

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the server
python manage.py runserver

🔐 Superuser (Optional)
python manage.py createsuperuser

✨ Future Ideas
Task notifications/reminders
Task categories or labels
API support (Django REST Framework)
Dark mode toggle 🌙

🙌 Credits
Built with 💻 by [Jayasurya08-Dev]

