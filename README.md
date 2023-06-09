<<<<<<< HEAD
# CrediCardValidation
=======
# credit_card_validation
Create for practice as homework and little programming challenge 

The Structure of the proyect is the next:

There are two main folders .. Design and --- Backend. The names speak for themselves. 

├── Credit Card Design
│   ├── dist
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   ├── LICENSE.txt
│   └── src
│       ├── index.html
│       └── style.css
├── Python Backend Proyect
│   ├── credit_card.py
│   ├── main.py
│   ├── __pycache__
│   └── venv
│       ├── bin
│       │   ├── activate
│       │   ├── activate.csh
│       │   └── ...
│       ├── include
│       ├── lib
│       │   └── python3.8
│       │       └── site-packages
│       │           ├── anyio
│       │           │   ├── abc
│       │           │   │   ├── ...


In the first folder can be found the structure of FrontEnd with HTML,CSS and JS

In the second folder can be found the API in Python with FastAPI
Note: I have just included the .py files. The rest have been removed in the file .gitignore 

To run the proyect. There are two options

1. Go to Credit Card Design -> Dist -> index.html and open the file on a browser. The API was
    uploaded to Deta Space and now is avaliable for all users. Although the code is still avaliable
    on the directory
    
    Api Public Link: https://apicard-1-v6371899.deta.app/docs

2. Deploy API on your own server. Following all the instructions. 

Prerequisites:
1. Install Python
2. Install Virtual Enviroments
3. Create Virtual enviroment
4. Install dependencies fastAPI, pydantic and uvicorn 
5. Run uvicorn main:app --reload

Connect localhost to view the docs : : http://127.0.0.1:8000/docs

Now Go to the script.js file in Credit Card Design -> Dist -> script.js and modify the next line.

53 fetch('https://apicard-1-v6371899.deta.app/validate_credit_card'),

Change the url with the localhost and voila. Now it should works!!
Dont forget the endpoint

>>>>>>> affbd74ad726fed362cbd580f68b418bc493a958
