from rest_framework.views import APIView
from .models import Rank
import json
from django.http import JsonResponse,HttpResponse

def get_one(name,obj):
    for i in obj:
        if i['client'] == name:
            return i

class RankList(APIView):
    data = {
        'code':200,
        'data':[],
    }
    def get(self,request):
        client = f"客户端{request.GET.get('client')}"
        start = request.GET.get('start')
        page_size = request.GET.get('page-size')
        r = Rank.objects.filter(client=client)
        if r:
            r_list = Rank.objects.all().order_by("score").reverse()
            data = [{'rank': r_list, 'client': i.client, 'score': i.score} for i in r_list]
            for i in data:
                i['rank'] = data.index(i) + 1
            if start and page_size:
                num = Rank.objects.all().order_by("score").reverse().count()
                if int(start)+int(page_size) > num:
                    self.data['code'] = 400
                    self.data['data'] = 'error too large size'
                else:
                    self.data['data'] = data[int(start):int(start)+int(page_size)]
            else:
                self.data['data']=data
            self.data['data'].append(get_one(client, data))
            return HttpResponse(json.dumps(self.data, ensure_ascii=False))
        else:
            self.data['code'] = 400
            self.data['data'] = 'no such client'
            return JsonResponse(self.data)



    def post(self,request):

        client = request.data.get('client')
        score = request.data.get('score')
        if int(score) < 1 or int(score)>10000000:
            self.data['code'] = 400
            self.data['data'] = 'error score value'
        else:
            try:
                r = Rank.objects.get(client=client)
            except:
                r = Rank()
                r.score = score
                r.client = client
            else:
                r.score = score
            r.save()
            self.data['data'] = 'seccese'
        return JsonResponse(self.data)
