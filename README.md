# Django To-Do App 📝

This is a simple full-stack To-Do List web application built using **Django** (Python framework).  
It allows users to:

✅ Add new tasks  
✅ Mark tasks as completed or not completed  
✅ Edit tasks  
✅ Delete single or all tasks  
✅ Filter tasks (Completed / Not Completed / All)  
🎨 Styled using basic CSS

## 🔧 Tech Stack

- Python 3
- Django
- HTML, CSS
- SQLite (default Django DB)

## 📂 Project Structure

- `todo/` – The main app for task management  
- `myproject/` – Django project settings  
- `manage.py` – Django command-line tool  

## 🚀 How to Run Locally

```bash
git clone https://github.com/shivasai322/django-todo-app.git
cd django-todo-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
