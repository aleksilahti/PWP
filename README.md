# PWP SPRING 2021
# Aviation Theory quiz application

## Users
* Users can test their knowledge on 9 aviation related topics 
* They can get a randomized N sample of questions from a database collection(1 of 9 topics) for their quiz
* Users get feedback on their results
* Users can comment and report questions featured in quizzes
* users can create, modify and delete their profiles
* users can add/suggest new questions.
* Users can vote review/vote on newly added questions(Should they be added to the question Database)

## Questions
* Questions can have up to 5 options to choose from
* Questions can have only one right answer
* Questions can have a picture added to them
* Question options can have an explanation why the option is or is not correct
* Questions have a comments section specific to that question

# Group information
* Student 1. Aleksi Lahti, alahti@student.oulu.fi
* Student 2. Rainer Laaksonen, ralaakso@student.oulu.fi
* Student 3. Markus Oja, moja19@student.oulu.fi

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__

# Overview of the API #


## installing ##

(Install virtualenv) (virtualenv is not in requirements) (in case with problems on Windows, try  installing with:)

	python -m pip install virtualenv --user

Activate python virtual environment in command line

	virtualenv pwp

Activate virtual environment

	pwp\Scripts\activate.bat

install dependencies

	pip install -r requirements.txt

use populate.py to generate test.db
	
(to refresh the requirements use) 

	python -m pip freeze -l > requirements.txt

# Contents of the repo #
## (root) ##
python stuff:

db.py = database model

populate.py = run this to create test.db

(test.db) = db having the data from populate.py

misc:

.gitignore = gitignore

requirements = reqs for this repo

readme.md = this readme file

license = license of this repo

meetings.md = meetings notes

## pwp ##

if you use "virtualenv pwp", this is where the virtualenv is created

should be ignored

## __pycache__ ##

python cache files

should be ignored

## appendix_for_wiki ##

appendices for the wiki, check the wiki to see these




