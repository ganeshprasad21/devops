import os

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # This points to monitoring_backend/
APPS = ["metrics", "logs", "alerts"]

FILES = {
    "metrics": [
        "models.py",
        "services.py",
        "views.py",
        "serializers.py",
        "urls.py",
        "tests.py",
        "collectors/__init__.py",  # Directory for different metric collectors
    ],
    "logs": ["models.py", "views.py", "serializers.py", "urls.py"],
    "alerts": ["models.py", "views.py", "serializers.py", "urls.py"],
}

# Function to create app directories if they don't exist
def create_app_dirs():
    for app in APPS:
        app_path = os.path.join(BASE_DIR, app)
        os.makedirs(app_path, exist_ok=True)  # Create the app directory if missing
        print(f"Ensured directory exists: {app_path}")

# Function to create files inside each app
def create_files(app_name, files):
    app_path = os.path.join(BASE_DIR, app_name)
    for file in files:
        file_path = os.path.join(app_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create subdirectories
        with open(file_path, "w") as f:
            f.write("# " + file.split("/")[-1] + "\n")  # Add a comment in each file
        print(f"Created: {file_path}")

# Generate structure
if __name__ == "__main__":
    create_app_dirs()  # Ensure app directories exist before creating files
    for app in APPS:
        create_files(app, FILES[app])

    print("✅ Django structure created successfully!")
