class UserMiddleware(object):

    def process_request(self, request):
        user_type = "guest"
        if request.user.is_authenticated():
            # user_type = request.user.type_str
            request.user.username='abdulshukoor'
            print 'hello'
        print 'world'
        # request.layout = "layouts/" + user_type + ".html"
        # request.nav = "navs/" + user_type + ".html"
