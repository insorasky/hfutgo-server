from utils.Request import Request, get_json_response
import json


class Search(Request):
    def post(self, request):
        filters = json.loads(request.body)['filters']
        data = self.stu.request(
            '/http-8080/77726476706e69737468656265737421a2a611d2736526022a5ac7f9/opac/ajax_search_adv.php',
            method='POST',
            headers={
                'Content-Type': 'application/json'
            },
            data={
                "searchWords": [
                    {
                        "fieldList": [
                            {
                                "fieldCode": "any",
                                "fieldValue": request.GET['word']
                            }
                        ]
                    }
                ],
                "filters": filters,
                "limiter": [],
                "sortField": "relevance",
                "sortType": "desc",
                "pageSize": 20,
                "pageCount": int(request.GET['page']),
                "locale": "zh_CN",
                "first": True
            }).json()
        return get_json_response(data)
