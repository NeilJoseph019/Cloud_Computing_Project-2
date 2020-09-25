from google.appengine.ext import ndb

class AnagramUser(ndb.Model):

    User_Id =ndb.StringProperty()
    email = ndb.StringProperty()

    anagram_key = ndb.StringProperty()
    anagram_word = ndb.StringProperty(repeated=True)
    words = ndb.StringProperty()
    anagram_count = ndb.IntegerProperty()

    input_word = ndb.StringProperty(repeated=True)

    word_length = ndb.IntegerProperty()
    # word_count = ndb.IntegerProperty()

    sub_anagram_word = ndb.StringProperty(repeated=True)
    sub_anagram_count = ndb.StringProperty()


