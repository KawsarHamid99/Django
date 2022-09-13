from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

'''


            def _make_hash_value(self, user, timestamp: int) -> str:
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))
'''

class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))

token_generator=AppTokenGenerator()


