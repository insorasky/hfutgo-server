from django.utils.deprecation import MiddlewareMixin
from utils.response import get_json_response
import traceback


class ExceptionMiddleWare(MiddlewareMixin):
    def process_exception(self, request, exception):
        traceback.print_exc()
        return get_json_response('内部错误', 500)
