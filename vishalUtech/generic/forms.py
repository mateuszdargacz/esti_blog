from django.forms import forms, HiddenInput

__author__ = 'opel'

from mezzanine.generic.forms import ThreadedCommentForm as ThreadedCommentFormOld


class ThreadedCommentForm(ThreadedCommentFormOld):
    def __init__(self, request, *args, **kwargs):
        super(ThreadedCommentForm, self).__init__(request, *args, **kwargs)
        ## Own form hidding useless data
        self.fields['name'].widget = HiddenInput()
        self.fields['email'].widget = HiddenInput()
        self.fields['url'].widget = HiddenInput()
        self.fields['honeypot'].widget = HiddenInput()
        self.fields['honeypot'].label = ''
        self.fields['comment'].label = ''
        if not request.user.is_authenticated():
            self.fields['comment'].widget.attrs['onfocus'] = "$('#comment_login').modal('show')"
