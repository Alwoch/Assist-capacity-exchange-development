# Assist-capacity-exchange-development
A bug reporting app created with django. It allows users to create a bug, view all reported bugs and view the details of a particular bug
### Getting started
1. clone the repository
   ```
   git clone https://github.com/Alwoch/Assist-capacity-exchange-development.git
   ```
2. enter the project directory
   ```
   cd Assist-capacity-exchange-development.git
   ```
3. Create a virtual environment
   ```
   python3 -m venv venv
   ```
4. activate the virtual environment
   ```
   source venv/bin/activate
   ```
5. Install project dependencies
   ```
   pip install -r requirements.txt
   ```
6. create a `.env` file in the root of your project and add your secret key
   ```
   SECRET_KEY=<your_secret_key>
   ```
7. start the server
   ```
   python3 manage.py runserver
   ```
8. In your browser's address bar, type `localhost:8000/bug/` to navigate to the bug app and `localhost:8000/admin` to access the admin interface

### Tasks:

- **Task 1** : [create a django project with an app called bug](https://github.com/Alwoch/Assist-capacity-exchange-development/tree/dfecaf12c4300dccf7c70729810726ebdad34530)
- **Task 2** : [structure the database and create a model](https://github.com/Alwoch/Assist-capacity-exchange-development/pull/5) </br>
  a bug successfully created from the admin panel can be seen in the image below:
  ![bugs successfully created from the admin panel](https://github.com/Alwoch/Assist-capacity-exchange-development/assets/83899148/b01f8e35-c498-488c-803f-25068bbe7bb8)
- **Task 3** : [Add views and templates](https://github.com/Alwoch/Assist-capacity-exchange-development/commit/1f3ee4448795c81dedd23330c066c8f3fb9d43b0)
- **Task 4** : [create automated unit tests](https://github.com/Alwoch/Assist-capacity-exchange-development/commit/dae9765f7348a1d816fe6f7f0656a505f0ba08fa)

