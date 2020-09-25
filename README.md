# Cloud_Computing_Project-2
This application allows users to add anagrams and subanagrams for studying or research or various other purposes.
It portraits the following mechanisms:

1. Login and Logout mechanism.
2. Adding a new anagram or sub-anagram to the system.
3. Viewing the existing anagram and it’s  information.
4. List view of sub-anagrams in the system.
5. Uploading a file.
---
* ## Application Overview
For this project the following directories were created:
* app.yaml
* myuser.py
* MainSystem.py
* HomePage.html
* AddFile.html
* AddWord.html
* anagram.html
* SubAnagram.html
* services.py
---
A.	In app.yaml : 

•	The yaml file is first created as its main responsibility is to keep the Google App Engine informed about the various libraries, handlers and runtime required to run the application. It helps to define where the requests are to be routed amongst the available applications.
•	The Jinja2 library is being specified that is being used to generate html templates that can render dynamic content for the user. We use the latest version of library to avoid as many security vulnerabilities as possible.

•	Various handles are  also specified that informs the Google App Engine which python funtions and objects are responsible for the requests sent to a certain url’s defined in the main python file. Handlers can also control access of url’s by the user, such as should the user not be logged in and more.

B.	In myuser.py :

•	The ndb (that is NoSql Database) client  library is being imported from google.appengine.ext package. ndb is a client library for use with Google Cloud Datastore. It was designed specifically to be used from within the Google App Engine Python runtime. ndb is included in the Python runtime.
•	The classAnagramUser takes in the argument ndb.Model, this will lets all of the datastore operations to be understood , how to store and retrieve in the  classes. It handles the necessary conversions between python and its representation in the Google Cloud Datastore. The various variables are created and it’s StringProperty() and IntegerProperty() as it will take in string or integer values  respectively while its stored in the datastore.

C.	InMainSystem.py :
At first the Jinja variable “JINJA_ENVIRONMENT” is defined as it’s considered to be unchanging. Jinja2 uses a central object called the template Environment . Instances of this class are used to store the configuration and global objects, and are used to load templates from the file system or other locations.
This python code contains totally 5 classes for various functionalities.
The classes are :
•	MainPage
•	AnagramPage
•	AddWordPage
•	SubAnagramPage
•	FileUploadPage


MainPage class :

•	In MainPage class, the get function/method helps in the working of login and logout functionality of the user.
•	This ensures that only the logged in users can add in the anagrams and view the information related to it.
•	This also ensures that every unique user gets an unique id and have his own set of anagrams separately.

AnagramPage class :

•	   The AnagramPage class, in the main page through which the other pages such as anagram addition page , sub anagram page, and file upload page can be accessed. 
•	   Also various details of the anagram can be viewed on this page.

AddWordPage class :

•	   The AddWordPage class, helps with the anagram addition functionality in the application.
•	   The entered anagram is stored in the database using the .put() function.
•	    It also keeps adding the number of anagrams as its entered every time by the user.

SubAnagramPage class :

•	   The SubAnagramPage class, helps with the viewing of sub-anagrams from the database in the application.

FileUploadPage class :

•	   The FileUploadPage class, helps with the file upload functionality in the application.
•	   This class reads the words line to line from the file and enters the words into the database of the currently logged-in user.

D.	In HomePage.html :

•	  This page helps with the login and logout functionality in the application.
•	  It displays the link that directs the user to the login url and also to the logout url.

E.	In AddFile.html :
 
•	   The AddFile page helps with the addition functionality of the files in the application.
•	   It has a button and on clicking it helps the user to browse through his files in the currently using system.
•	   This file selected then is read by the system and the words are fetched line by line from the file and stored in the users database .

F.	In AddWord.html :

•	   The AddFile page helps with the addition functionality of the anagram in the application.
•	   It displays a text box for the user to input the anagram word and also a button to enter so that the word gets stored into the database.
•	   The text box accepts only alphabetic characters and nothing else. If its anything other than the alphabets then it will redirect to the same page.

G.	In anagram.html :

•	This page helps with the connecting functionality between various pages such as add word page, add file page and Sub-anagram search page  in the application.
•	This also displays a few details of the anagrams in the users database such as word count and anagram count.

H.	In SubAnagram.html :

•	   This page helps with the viewing functionality of the sub-anagrams of the word in the database  in the application.
•	   The user is allowed to enter a word into the text box and it displays the word matched in the database along with word entered along with the various sub-anagrams of the anagrams .

I.	In services.py :

•	  This contains the sorting and permutation/combination functions used in the other files in the application.
•	  This contains the sort functionality, which helps in the arranging the letters of the entered word into lexicographical order this will be used as the key.
