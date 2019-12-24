<h1>FLEXPOINTS STORE</h1>
<p>Flexpoints are the abstract idea of the amount of "credit" a teacher gives to a student. They are aquired through academic perserverance and merit, and are spent automatically by doing actions that would usually detract from a student's theoretical "standing". Basically, with enough of these, you never need to work again!</p>

<p>This is a fun project I did for my backend web class. The requirements were to create an online store with Django that met certain requirements and standards, such as not accidentally exposing secret keys and having RESTFUL api capabilities. This project has full login and upload capabilities as well, and will serve as a template for some future projects.</p>

[proposal.md](https://gist.github.com/HexSeal/5412aee5e6e4c4610a1367f8ab65601a)

[rubric.md](https://gist.github.com/HexSeal/5d98b7e14afd2afcb614fe8b44fdc974)

[Live Deployment!](https://flexpointsapp.herokuapp.com/)


<h4>To install the packages needed to run this project, first create a virtual environment so you don't have to keep anything on your computer you don't need! </h4>
<h5>On Mac:</h5>
First, start by closing the repository:
git clone hhttps://github.com/HexSeal/django_flexpoints_store

Start by installing virtualenv if you don't have it
pip install virtualenv

Once installed access the project folder
cd django_flexpoints_store

Create a virtual environment
virtualenv venv

Enable the virtual environment
source venv/bin/activate

Install the python dependencies on the virtual environment
pip install -r requirements.txt

<h2> HOW TO RUN SERVER </h2>
(Heroku):
==>"heroku open"

<h2> (Local Host): </h2>
==>"python3 manage.py runserver"
