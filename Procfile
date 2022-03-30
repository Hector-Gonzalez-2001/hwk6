// Procfile: keep in mind the spacing
// the second "app" in the procfile is actually the name of your flask app
web gunicorn app:app

// to create your requirements.txt file you can either run:
python -m pip freeze > requirements.txt
// or you can pip install pipreqs and run:
python -m pipreqs.pipreqs --encoding=utf-8

// I recommend using pipreqs, unless you're responsible and have a venv for every project
// additionally, add:
gunicorn==20.1.0
// to your requirements.txt file if it's not there (the version doesn't have to be 20.1.0)