# mapp

## How to Run the Project:

To run your Flask project, ensure that your virtual environment is activated. If you haven't created a virtual environment yet, you can do so using the following command (make sure you are in the main folder of your project):

```bash
python -m venv venv
```

## Next, activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```

After activating the virtual environment, you can run your Flask application. Typically, in a Flask project, you will run the wsgi.py file to start the server.

## You can do this as follows:

Navigate to the "app" directory (cd app) and run:

```bash
python wsgi.py
```

Your Flask application will run and be available at the following local address: http://127.0.0.1:5000/. You can access it from your web browser or make HTTP requests to your routes.

## **Starting in an Empty Folder**
Initialize the folder as a Git repository:

```bash
$ git init
```

Add a remote repository:

```bash
$ git remote add origin https://github.com/19Mega/mapp.git
```

Rename the current branch to "main":

```bash
$ git branch -m "main"
```

Pull changes from the "main" branch:

```bash
$ git pull origin main
```

## **Branch Management**
Create a new branch, for example, "ft-new-branch":

```bash
$ git branch -b "ft-new-branch"
```

Switch to a different branch, e.g., "ft-switch-branch":

```bash
$ git checkout ft-switch-branch
```

List available branches:

```bash
$ git branch
```

## Database

Inside the "app" directory, a folder named "instance/" will be created where the database will be located.