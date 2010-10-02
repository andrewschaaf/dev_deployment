
from dev_deployment import settings

from util.exceptions import exceptionRepr
from dev_deployment.debug import jab


class ExceptionsMiddleware:
    
    def process_exception(self, r, exception):
        
        if settings.DEBUG and settings.EXCEPTION_JABBER is not None:
            jab(
                    exceptionRepr(),
                    settings.EXCEPTION_JABBER['to_account'],
                    settings.EXCEPTION_JABBER['from_account'],
                    settings.EXCEPTION_JABBER['from_password'])
        
        # return HttpResponse ===> Django returns it to browser
        # else                ===> default exception handling
        return None


