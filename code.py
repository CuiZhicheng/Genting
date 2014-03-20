import web
# Create a template operator
render = web.template.render('./templates/')
#db = web.database(dbn='mysql', user='root', pw='123456', db='blog_test')

urls = (
	'/', 'index',
	)

class index:
    def GET(self):
        return render.index()
if __name__=="__main__":
    app = web.application(urls, globals())
    app.run()
