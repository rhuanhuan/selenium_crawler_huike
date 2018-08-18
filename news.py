class News(object):
    def __init__(self, title, news_time, news_office, words_number, description):
        self.title = title
        self.news_time = news_time
        self.news_office = news_office
        self.words_number = words_number
        self.description = description

    def to_str(self):
        string = "{\"title\": \"%(title)s\"," \
                 " \"news_time\": \"%(news_time)s\"," \
                 " \"news_office\": \"%(news_office)s\"," \
                 " \"words_number\": \"%(words_number)s\"," \
                 " \"description\": \"%(description)s\"}" % {
                     'title': self.title,
                     'news_time': self.news_time,
                     'news_office': self.news_office,
                     'words_number': self.words_number,
                     'description': self.description
                 }
        return string
