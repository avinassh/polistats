from bson.objectid import ObjectId
from bson.json_util import dumps

import pymongo
import tornado.ioloop
import tornado.web

class PoliStatsHandler(tornado.web.RequestHandler):
    def get(self):
        conn = pymongo.MongoClient()
        db = conn['search_results']

        if self.request.headers.get('Origin', None):
            self.set_header('Access-Control-Allow-Origin', self.request.headers['Origin'])
        self.write(dumps(list(db.search_results.find({}))))
        return

class MainHandler(tornado.web.RequestHandler):
        def get(self):
                self.write("use /polistats for JSON dump")

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/polistats", PoliStatsHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()