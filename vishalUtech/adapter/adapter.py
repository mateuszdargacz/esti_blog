from allauth.account.adapter import DefaultAccountAdapter

__author__ = 'opel'

class MyAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        next = request.GET['next'] + '#comments'
        return next
