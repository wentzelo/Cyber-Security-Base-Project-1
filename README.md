This is a website for the first project of the Cyber Security Base 2026 course. It purposefully has built in security flaws. 

## How to run

1. Clone the repo:

git clone https://github.com/wentzelo/Cyber-Security-Base-Project-1.git

2. `cd` into `pwmanager/`.
3. Create a virtual environment.

python3 -m venv venv
Linux: source venv/bin/activate
Windows: venv\Scripts\Activate.ps1

4. Run:

pip install -r requirements.txt

5. Apply the migrations:

python manage.py migrate

6. Run the server:

python manage.py runserver


There are two accounts:

| Username | Password   |
|----------|------------|
| donald   | bluedragon |
| steve    | unemployed |
