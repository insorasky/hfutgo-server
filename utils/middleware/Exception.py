from django.utils.deprecation import MiddlewareMixin
from utils.response import get_json_response
from hfutgo.settings import DEBUG
import traceback


class ExceptionMiddleWare(MiddlewareMixin):
    def process_exception(self, request, exception):
        if not DEBUG:
            traceback.print_exc()
            return get_json_response('内部错误', 500)
