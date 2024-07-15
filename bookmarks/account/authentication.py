from django.contrib.auth.models import User


class EmailAuthBackend(object):
    """ Authenticates users against email addresses. """

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user_name. """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Retrieve a user based on primary key. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None