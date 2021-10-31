## NO MORE PROXY
Its the project made by team ERROR 404 for hackathon HACKNITR 3.0.
Idea of our project is to use face recognition technology to mark the attendence of students for the classes in the college. We store all the details of the students of the college in the database and then maintain all the courses and student enrolled in that course. Details include Name, Roll No., Courses enrolled and a reference image for the the facial recognition to compare against.

While marking attendence, a photo will be snapped which will be tested against reference images in the database. If system recognizes the face of the student, it will mark attendence in attendence database.
We have also implemented a feature in which a professor can register his course's class to be held on a particular day. We implemented this using a user input form which we then convert to a text file and save locally. This locally saved file can then be used ny the python script in order to make the required changes in our original database

Technologies used:

- OpenCv
- MySQL
- Flask
- Javascript

Main file for backend : facial.py

Main File for frontend: frontend_2/homepage.html

PS: there's a little incoherence between frontend and backend as the images and form are stored locally by the user and then run against the python script. We aim to fix that soon and implement a completely automated version of this :).



