# -*- comding:utf-8   -*-



from logzero import logger
import ast
import requests

#查找k , v 值路径方法
class HandleJson():
    def __init__(self, data):
        if data == None:
            logger.error('请输入json格式数据')
            exit()

        if isinstance(data, str):
            try:
                self.data = ast.literal_eval(data)
            except:
                logger.error('请输入正确的json格式数据')
                exit()
        elif isinstance(data, dict):
            self.data = data

    def __paths(self, data, path=''):
        '''
        用于遍历json树
        :param data: 原始数据，或者key对应的value值
        :param path: key值字符串，默认值为''
        :return:
        '''
        if isinstance(data, dict):
            for k, v in data.items():
                tmp = path + "['%s']" % k
                yield (tmp, v)
                yield from self.__paths(v, tmp)

        if isinstance(data, list):
            for k, v in enumerate(data):
                tmp = path + '[%d]' % k
                yield (tmp, v)
                yield from self.__paths(v, tmp)

    def find_key_path(self, key):
        '''
        查找key路径
        :param key: 需要查找路径的key值
        :return: 包含key值路径的list
        '''
        result = []
        for path, value in self.__paths(self.data):
            if path.endswith("['%s']" % key):
                result.append(path)
        with open('../path.txt', 'w+', encoding='utf-8') as f:
            list(map(lambda line: f.write(line + '\r'), result))
        return result

    def find_value_path(self, key):
        '''
        查找某个值的路径
        :param key: 需要查找的值，限制为字符串，数字，浮点数，布尔值
        :return:
        '''
        result = []
        for path, value in self.__paths(self.data):
            if isinstance(value, (str, int, bool, float)):
                if value == key:
                    result.append(path)
        with open('../path.txt', 'w+', encoding='utf-8') as f:
            list(map(lambda line: f.write(line + '\r'), result))
        return result

def  find_XC_PT():
    url = "https://flights.ctrip.com/itinerary/api/12808/products"

    payload = "{\"flightWay\":\"Oneway\",\"classType\":\"ALL\",\"hasChild\":false,\"hasBaby\":false,\"searchIndex\":1,\"isfull\":\"\",\"airportParams\":[{\"dcity\":\"wuh\",\"acity\":\"szx\",\"dcityname\":\"武汉\",\"acityname\":\"深圳\",\"date\":\"2020-10-18\"}],\"selectedInfos\":null,\"army\":false,\"token\":\"31e42509f8db85e0b717af221ada0c51\"}"
    headers = {
      'Host': 'flights.ctrip.com',
      'Connection': 'keep-alive',
      'Content-Length': '288',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
      'Content-Type': 'application/json',
      'Accept': '*/*',
      'Origin': 'https://flights.ctrip.com',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Dest': 'empty',
      'Referer': 'https://flights.ctrip.com/itinerary/oneway/wuh-szx?date=2020-10-18&isfull=',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cookie': 'abtest_userid=8cef430c-28bb-4a62-b1ea-720db142b154; _RGUID=3a8cf9a3-d28f-433d-bef1-10f6d779430c; _RDG=2855cc4c76264a29182e8df041ce9e8d2b; _RSG=zCqZIFQ.Cg3CCKUNRF4nxB; _RF1=121.201.121.142; MKT_CKID=1591005078914.ardji.c437; _ga=GA1.2.382488139.1591005080; nfes_isSupportWebP=1; StartCity_Pkg=PkgStartCity=477; GUID=09031091113303287852; appFloatCnt=1; login_uid=2F328364505C95D729E5B827ECF17852; login_type=0; cticket=8C11CB789164C1AA895BEB4B39705859156ABC2AB19143B7AF1B2B70B4C72BC6; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=%D7%F3%CD%FB%CD%FA&NoReadMessageCount=2; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojLnhPeG6ac5VkEBgi3rWnw3SmFEAAgtAcIzx2+9yg7+7PBFALnNQ71rjPioYOyPtH582WYZG8ZlcXSA9GQltrKDDT9vgQXummbmVqGqFXorsccKdNhcHshSNTJRXuI3rB/obmcPP1zfkmzLfrh3Qi3HZOTTCG1pgDBw8BYnDiuibAHqmnLrj5cb0wSoX7/cC3+8b/gtmPqVaH9ICCU88rfGG8Jnk2o7Pa2piL+MvZpAt1FfzTOc+WMS3gvFI2NogSiaolYiM4PAw=; DUID=u=2F328364505C95D729E5B827ECF17852&v=0; IsNonUser=F; UUID=C5C1A34B5CB9406FB7EC198ACAEDA5C4; IsPersonalizedLogin=F; Session=SmartLinkCode=tianxun&SmartLinkKeyWord=&SmartLinkQuary=_UTF.&SmartLinkHost=www.tianxun.com&SmartLinkLanguage=zh; MKT_CKID_LMT=1599017007837; _gid=GA1.2.566586870.1599017119; MKT_Pagesource=PC; _jzqco=%7C%7C%7C%7C1599017118880%7C1.596777396.1591005078912.1599017278516.1599017372279.1599017278516.1599017372279.undefined.0.0.37.37; __zpspc=9.10.1599017007.1599017372.5%233%7Cwww.tianxun.com%7C%7C%7C%7C%23; _bfa=1.1591005076106.37bo1o.1.1597216517430.1599017007701.14.126.10650016819; _bfs=1.10; _bfi=p1%3D10320673302%26p2%3D10320673302%26v1%3D126%26v2%3D125'
    }

    response = requests.request("POST", url, headers=headers, data = payload.encode())

    # print(response.text.encode('utf8'))
    cc = response.json()
    return cc   #返回接口返回的数据



data = find_XC_PT()
hj = HandleJson(data)
res = hj.find_key_path('price')  #查找key
print(res)
res = hj.find_value_path('CZ3912') #查找该次查询这天，这个航班的路径
print(res)


print(data['data']['routeList'][9]['legs'][0]['flight']['flightNumber'])
print(data['data']['routeList'][9]['legs'][0]['cabins'][0]['price']['price'])



