import jinja2
import webapp2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

from Service import Service
from myuser import AnagramUser
from personD import PersonD

JINJA_ENVIRONMENT= jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

def sort(n):
   ordered = ''.join(sorted(n))
   return ordered

class MainPage(webapp2.RequestHandler):

    def get(self):

        title = "Home Page"

        self.response.headers['Content-Type'] = 'text/html'

        url = ''
        url_string = ''

        user = users.get_current_user()

        if user:
            url = users.create_logout_url(self.request.uri)
            url_string = 'logout'

            myuser_key = ndb.Key('PersonD', user.user_id())
            myuser = myuser_key.get()

            if myuser == None:
                myuser = PersonD(id=user.user_id(),
                                email_address=user.email(),
                                Anagram_Count=0,
                                WordCount=0
                                )
                myuser.put()

        else:

            url = users.create_login_url(self.request.uri)
            url_string = 'login'

        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
            'title': title,
        }
        template = JINJA_ENVIRONMENT.get_template('HomePage.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content - Type'] = 'text / html'



class AnagramPage(webapp2.RequestHandler):
    def get(self):
        title = "Anagram Page"

        user = users.get_current_user()

        if user:

            myUser_key = ndb.Key("PersonD", user.user_id())
            my_user = myUser_key.get()


            wordList = AnagramUser.query(my_user.email_address == AnagramUser.email)

            search = self.request.get(" input_search_word ").lower()

            sorted_k = Service().sorted_key(word=search)

            anagram_k = user.user_id() + sorted_k

            if self.request.GET.get("search_button") == "Search Word":

                Query = AnagramUser.query(ndb.OR(search == AnagramUser.words))

                # wordList = wordList.filter(search == AnagramUser.words)

                wordsQuery = Query.fetch()

            else:
                wordsQuery = wordList.fetch()


        template_values = {

            'title': title,
            'query': wordsQuery

        }
        template = JINJA_ENVIRONMENT.get_template('anagram.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers["Content-Type"] = "text/html"



class AddWordPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        title = "Add Word Page"


        template_values = {
            'title': title,
        }
        template = JINJA_ENVIRONMENT.get_template('AddWord.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content - Type'] = 'text / html'

        if self.request.get("add_button") == "Add Word":

            user = users.get_current_user()

            anagramWord = self.request.get("add_word").lower()

            word_length = len(anagramWord)

            sorted_key = Service().sorted_key(word=anagramWord)

            anagram_key =user.user_id()+sorted_key

            if  anagramWord == "" :
                self.redirect('/AddWord.html')
                return

            wordKey = ndb.Key(AnagramUser, anagram_key)
            wordRetrieved = wordKey.get()

            myUser_key = ndb.Key("PersonD", user.user_id())
            my_user = myUser_key.get()

            if wordRetrieved==None:

                device_query = AnagramUser.query(AnagramUser.anagram_word == anagramWord).fetch()

                if len(device_query) > 0:
                    self.redirect('/AddWord.html')
                    return
                else:

                    entered_word = AnagramUser(
                        User_Id=user.user_id(),
                        email = user.email(),
                        anagram_key=anagram_key ,
                        anagram_word=[anagramWord],
                        words = anagramWord,
                        anagram_count=1,
                        word_length=word_length,

                    )
                    entered_word.put()
                    entered_word.input_word.append(anagramWord)

                    Anagram_Count = my_user.Anagram_Count + 1
                    WordCount = my_user.WordCount + 1

                    myUser=PersonD(id=user.user_id(),
                                email_address=user.email(),
                                Anagram_Count=Anagram_Count,
                                WordCount=WordCount
                                )
                    myUser.put()

                    self.redirect('/anagram.html')

            else:

                counter = len(wordRetrieved.input_word) + 1
                wordRetrieved.anagram_count = counter
                wordRetrieved.input_word.append(anagramWord)
                wordRetrieved.put()

                WordCount = my_user.WordCount + 1
                Anagram_Count = my_user.Anagram_Count
                my_user = PersonD(
                    id=user.user_id(),
                    email_address=user.email(),
                    Anagram_Count=Anagram_Count,
                    WordCount=WordCount
                )
                my_user.put()

                self.redirect('/anagram.html')

class SubAnagramPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        title = "Sub Anagram Page"

        user = users.get_current_user()

        my_user_key = ndb.Key('AnagramUser', user.user_id())
        my_user = my_user_key.get()

        sub_anagram = self.request.get('subAnagram_input')

        sorted_key = Service().sorted_key(word=sub_anagram)

        anagram_key = user.user_id() + sorted_key

        resultList = []

        subList = Service().subWordSort(word=sorted_key)

        for key in subList:
            w_key = ndb.Key(Anagram_engine,anagram_key)
            myWord = w_key.get()
            if myWord != None:
                resultList.extend(myWord.anagram_word)
                subCount = my_user.sub_anagram_count + 1
            usera=AnagramUser(
                anagram_key=anagram_key,
                sub_anagram_word=myWord.input_word,
                sub_anagram_count=subCount
            )


        template_values = {

            'title': title,
            'resultList': resultList,
            'subanagramCount':AnagramUser.sub_anagram_count

        }

        template = JINJA_ENVIRONMENT.get_template('SubAnagram.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers["Content-Type"] = "text/html"

        user = users.get_current_user()

        if self.request.get("input_subAnagram") == "Check":
            sub_anagram = self.request.get('subAnagram_input')
            self.redirect('/SubAnagram.html?input_word=' + sub_anagram)


class FileUploadPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        title = "File Upload Page"

        template_values = {

            'title': title
        }
        template = JINJA_ENVIRONMENT.get_template('AddFile.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers["Content-Type"] = "text/html"

        action = self.request.get('UploadButton')

        user = users.get_current_user()
        my_user_key = ndb.Key('PersonD', user.user_id())
        my_user = my_user_key.get()

        file = self.request.get('uploadFile')

        if action == 'Upload':
            openFile = open(file)
            readLine = openFile.readline()
            while readLine:

                AnagramFileWords = (readLine.strip('\n\r')).lower()

                word_length = len(AnagramFileWords)

                sorted_key = Service().sorted_key(word=AnagramFileWords)

                anagram_key = user.user_id() + sorted_key

                wordKey = ndb.Key(AnagramUser, anagram_key)
                wordRetrieved = wordKey.get()

                myUser_key = ndb.Key("PersonD", user.user_id())
                my_user = myUser_key.get()

                if wordRetrieved == None:

                    device_query = AnagramUser.query(AnagramUser.anagram_word == AnagramFileWords).fetch()

                    if len(device_query) > 0:
                        self.redirect('/AddFile.html')
                        return
                    else:

                        entered_word = AnagramUser(
                            User_Id=user.user_id(),
                            email=user.email(),
                            anagram_key=anagram_key,
                            anagram_word=[AnagramFileWords],
                            words=AnagramFileWords,
                            anagram_count=1,
                            word_length=word_length,

                        )
                        entered_word.put()
                        entered_word.input_word.append(AnagramFileWords)

                        Anagram_Count = my_user.Anagram_Count + 1
                        WordCount = my_user.WordCount + 1

                        myUser = PersonD(id=user.user_id(),
                                         email_address=user.email(),
                                         Anagram_Count=Anagram_Count,
                                         WordCount=WordCount
                                         )
                        myUser.put()

                        self.redirect('/anagram.html')

                else:

                    counter = len(wordRetrieved.input_word) + 1
                    wordRetrieved.anagram_count = counter
                    wordRetrieved.input_word.append(AnagramFileWords)
                    wordRetrieved.put()

                    WordCount = my_user.WordCount + 1
                    Anagram_Count = my_user.Anagram_Count
                    my_user = PersonD(
                        id=user.user_id(),
                        email_address=user.email(),
                        Anagram_Count=Anagram_Count,
                        WordCount=WordCount
                    )
                    my_user.put()

                readLine = openFile.readline()

            openFile.close()


app = webapp2.WSGIApplication([('/',MainPage),('/anagram.html',AnagramPage),('/AddWord.html',AddWordPage),('/SubAnagram.html',SubAnagramPage),('/AddFile.html',FileUploadPage)],debug=True)