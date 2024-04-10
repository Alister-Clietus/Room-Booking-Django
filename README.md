# Room-Booking-Django

# Installing Django in Windows using Virtual Environment

This guide will walk you through the steps to install Django on a Windows operating system using a virtual environment.

## Prerequisites

Before you start, ensure you have the following installed:

- Python (3.x recommended)
- pip (Python package manager)

## Step 1: Create a Virtual Environment

Open a command prompt and navigate to the directory where you want to create your Django project.

```bash
cd path/to/your/directory

Step 2: Activate the Virtual Environment
Navigate to the Scripts directory inside your virtual environment:

bash
Copy code
cd myenv\Scripts
Activate the virtual environment by running the activate script:

bash
Copy code
activate
You should see (myenv) appear at the beginning of your command prompt, indicating that the virtual environment is active.

Step 3: Install Django
With your virtual environment activated, you can now install Django using pip:

bash
Copy code
pip install django
This will install the latest version of Django in your virtual environment.

Step 4: Verify Installation
To verify that Django has been installed correctly, you can check the version:

bash
Copy code
python -m django --version
This command should display the installed Django version.

Step 5: Create a Django Project
Now, you can create a new Django project by running the following command:

bash
Copy code
django-admin startproject myproject
Replace myproject with the name you want to give to your Django project.

Step 6: Run the Development Server
Navigate into the newly created project directory:

bash
Copy code
cd myproject
Start the Django development server:

bash
Copy code
python manage.py runserver
You should see a message indicating that the development server is running.

You can now access your Django project by opening a web browser and navigating to http://127.0.0.1:8000/.
