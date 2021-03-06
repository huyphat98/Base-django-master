from jwt import ExpiredSignatureError, DecodeError
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings

from apps.authentication.utils import jwt_decode_handler
from apps.user.models import User, Token


class JWTAuthentication(JSONWebTokenAuthentication):
    keyword = api_settings.JWT_AUTH_HEADER_PREFIX

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            else:
                return None

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            raise NotAuthenticated()

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise AuthenticationFailed(msg)

        return token

    def authenticate(self, request):
        token = self.get_jwt_value(request)
        if token is None:
            raise NotAuthenticated()
        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        try:
            payload = jwt_decode_handler(token)
        except ExpiredSignatureError:
            raise AuthenticationFailed('Token Expired!')
        except DecodeError:
            raise AuthenticationFailed('Invalid Token!')
        except Exception:
            raise AuthenticationFailed('Invalid token.')

        try:
            token = Token.objects.select_related('user').get(
                user_id=payload.get('user_id'),
                token=payload.get('orig_iat')
            )
        except Token.DoesNotExist:
            raise AuthenticationFailed('No user matching this token was found.')

        return token.user, token
