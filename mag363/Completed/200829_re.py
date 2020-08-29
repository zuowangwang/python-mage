# -*- comding:utf-8   -*-
def testzz_z():
    ''' 正则学习 '''
    import re
    #findall  匹配一个列表
    #search,match   匹配一次之后就不匹配了match类型，search匹配有很多正则比较好
    s = '13978962341asdad1497896232212313asdad  0123-67823456  very very vary 192.168.213.123'

    n = re.findall(r'1\d{10}', s )
    print("正则取出来的值：",n , "他的格式:", type(n))
    print('取列表第一个：',n[0], type(n[0]))

    print('--'*10)

    b = re.search(r'1\d{10}', s)   #1开头，后面10位
    print("正则取出来的值：", b ,"他的格式:", type(b))
    print('只取一次：', b.group(),type(b.group()))

    print('--' * 10)
    m = re.findall(r'\d{3,4}-\d{7,8}', s)   #前面3-4位数字，后面7-8位数字
    print(m)

    print('--' * 10)
    w = re.findall(r'(14|13)\d{9}', s)  #['13', '14']
    w1 = re.search(r'(14|19)\d{9}', s)  #<_sre.SRE_Match object; span=(16, 27), match='14978962322'>
    w2 = re.match(r'(14|19)\d{9}', s)
    print(w,w1,w2)

    print('--' * 10)
    m  = re.findall(r'(very)\s+\1', s) #['very']
    m1 = re.search(r'(very)\s+\1', s) #<_sre.SRE_Match object; span=(54, 63), match='very very'>
    m2 = re.match(r'(very)\s+\1', s)
    print(m,m1,m2)

    print('--' * 10)
    m = re.findall(r'1\d{10}(?=123)', s)  #断言，判断后面一定有123
    print(m)

    print('--' * 10)
    m = re.findall(r'(?:(\d{1,3}).){3}(\d{1,3})', s)
    m1 = re.search(r'(?:(\d{1,3}).){3}(\d{1,3})', s)
    m2 = re.match(r'(very)\s+\1', s)
    print(m)
    print(m1)
    
def test_pkip():
     #匹配合法的ip地址
     line = """\
     192.168.1.150
     0.0.0.0
     255.255.255.255
     17.16.52.100
     172.16.0.100
     400.400.999.888
     001.022.003.000
     257.257.255.256 """


     import socket
     for i,ip in enumerate(line.splitlines()):
          print(ip)
          try:
               net = socket.inet_aton(ip)
          except Exception as e :
               print(i , ip , e)
          print(i, net)
import re
def tes_ftp():
     #选出含有ftp的链接,且文件类型是gz或者xz的文件名
     s = 'http://ftp.altlinux.org/pub/people/legion/kbd/kbd-1.15.5.tar.gz'
     m = re.findall(r'ftp.*/(.*\.(?:gz|xz))', s)
     print(m)


def test_zzzz():
     test = '''agsodahkjsd\nasbdas\nasda\wqeq\nAppLE'''

     #每次执行编译一次
     matcher = re.match('ags', test, re.I)   
     print(matcher)

     print('---'*10)

     #先编译，然后执行
     regex = re.compile('b.+', re.S)  #re.S 多行  re.I 忽略大小写 re.M 从多行查找，如果指定了第几位会找不到后面的数据
     matcher = regex.match(test) # 第一个参数，是从什么文本查找
     print(matcher)
     print('---'*10)


     matcher = regex.search(test, 8) #第二个参数是从多少位开始查找  
     print(matcher)
     print('---'*10)

     matcher = regex.fullmatch(test, 9,25) #全匹配
     print(matcher)
     print('---'*10)


     matcher = re.findall('b.+', test) #全文匹配
     print(matcher)
     print('---'*10)


     matcher = re.finditer('b.+', test) #全文匹配
     print(matcher)
     print('---'*10)




     #匹配后替换参数sub
     #匹配正则，替换内容，文本内容，替换次数，立即替换
     print(re.sub('a\w+d', 'www', test, 10).encode())
     print('---'*10)

     #n 的意思是，返回替换成功的值并告诉你替换了几次
     print(re.subn('a\w+d', 'www', test, 10))
     print('---'*10)

     #正则提取分隔
     test = '''asda\n\t (baf)\nasd'''
     regex = re.compile('[\s()]+') #空格分隔
     print(regex.split(test))


     #带有空格，数字等，切割
     test = '''01 asda
     123 asda
     12 asda 
     100 asdas'''
     regex = re.compile('\s+\d+\s+') #空格分隔
     print(regex.split(test))

     regex = re.compile('^\d+\s+|\s+\d+\s+') #空格分隔
     print(regex.split(test))



# match、search函数可以返回match对象；findall返回字符串列表；finditer返回一个个match对象
# 如果pattern中使用了分组，如果有匹配的结果，会在match对象中
# 1. 使用group(N)方式返回对应分组，1到N是对应的分组，0返回整个匹配的字符串
# 2. 如果使用了命名分组，可以使用group('name')的方式取分组
# 3. 也可以使用groups()返回所有组
# 4. 使用groupdict() 返回所有命名的分组


     #匹配邮箱地址

     testeail = '''
     test@hot-mail.com
     v-ip@magedu.com
     web.manager@magedu.com.cn
     super.user@google.com
     ashdajjlkj@163.com
     ahsdkl@qq.com
     qweiqpowei@aadsad.cn
     123981273981@qq.com
     a@w-a-com
     '''
     regex = re.compile(r'[-\w.]+@[-\w.]+\.\w+') 
     matcher = regex.findall(testeail) 
     print(matcher)

     #匹配html标记内的内容


     str1 =  """<a href='http://www.magedu.com/index.html' target='_blank'>马哥教育</a>
     <div><a> mag Cspan color- 'red'> edu</span> </a></div>
     """

     regex = re.compile(r'<a[^<>]*>(.*)</a>')    #<(div)[^<>]*>( .*)</\1>   分组div  变量第一个分组\1  ，可以改a,或者其他标签
     matcher = regex.findall(str1) 
     print(matcher)


     #匹配URL

     testurl = '''
     http://www.magedu.com/index.html
     https://login.magedu.com
     file:///ect/sysconfig/network
     '''
     regex = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')  
     matcher = regex.findall(testurl) 
     print(matcher)


     #匹配二代中国身份证ID
     testid = '''
     321105700101003
     321105197001010030
     11210020170101054X
     17位数字+1位校验码组成
     前6位地址码，8位出生年月，3位数字，1位校验位（0-9或X）
     '''
     regex = re.compile(r'\d{17}[\dxX]|\d{15}')  
     matcher = regex.findall(testid) 
     print(matcher)

    #判断密码强弱
    # 要求密码必须由 10-15位 指定字符组成：
    # 十进制数字
    # 大写字母
    # 小写字母
    # 下划线
    # 要求四种类型的字符都要出现才算合法的强密码
    # 例如：Aatb32_67mnq，其中包含大写字母、小写字母、数字和下划线，是合格的强密码
     testsfz = ''' Aatb32_67mnq
     '''

     regex = re.compile(r'^[a-zA-Z0-9_]{10,15}$')  
     matcher = regex.findall(testsfz) 
     print(matcher)


# //密码强弱程度（我把原来正则表达式后面的g都去掉了）
#     //弱
#     var week = /^([a-zA-Z]){6,16}$|^(\d){6,16}$|^((?=[\x21-\x7e]+)[^A-Za-z0-9]){6,16}$|^(?!\2+$)(?!\1+$)[\2\1]{6,7}$|^(?!\3+$)(?!\1+$)[\3\1]{6,7}$|^(?!\3+$)(?!\2+$)[\2\3]{6,7}$|^(?=.*\3)(?=.*\1)(?=.*\2)[a-zA-Z\x21-\x7e\d]{6,7}$/;
#     //中：字母+数字
#     var middle1 = /^(?!\d+$)(?![a-zA-Z]+$)[\dA-Za-z]{8,16}$/;
#     //中：字母+字符
#     var middle2 = /^(?!((?=[\x21-\x7e]+)[^A-Za-z0-9])+$)(?![a-zA-Z]+$)[^\u4e00-\u9fa5\d]{8,16}$/;
#     //中：数字+字符
#     var middle3 = /^(?!((?=[\x21-\x7e]+)[^A-Za-z0-9])+$)(?!\d+$)[^\u4e00-\u9fa5a-zA-Z]{8,16}$/;
#     //强
#     var strong = /^(?=.*((?=[\x21-\x7e]+)[^A-Za-z0-9]))(?=.*[a-zA-Z])(?=.*[0-9])[^\u4e00-\u9fa5]{8,13}$/;
#     //最强
#     var strongest = /^(?=.*((?=[\x21-\x7e]+)[^A-Za-z0-9]))(?=.*[a-zA-Z])(?=.*[0-9])[^\u4e00-\u9fa5]{14,16}$/;





# 1、用户名正则

# //用户名正则，4到16位（字母，数字，下划线，减号）
# var uPattern = /^[a-zA-Z0-9_-]{4,16}$/;

# 2、Email正则

# //Email正则
# var ePattern = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

# 3、手机号正则

# //手机号正则
# var mPattern = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;

# 4、身份证正则

# //身份证号（18位）正则
# var cP = /^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/;
# 5、IPV4地址正则

# //ipv4地址正则
# var ipP = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
# 6、QQ号正则

# //QQ号正则，5至11位
# var qqPattern = /^[1-9][0-9]{4,10}$/;

# 7、微信号正则

# //微信号正则，6至20位，以字母开头，字母，数字，减号，下划线
# var wxPattern = /^[a-zA-Z]([-_a-zA-Z0-9]{5,19})+$/;

# 8、车牌号正则

# //车牌号正则
# var cPattern = /^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$/;

# 9、包含中文正则

# //包含中文正则
# var cnPattern = /[\u4E00-\u9FA5]/;



     # #单词统计

     chekword = '''\
     host
     maowe
     asdaksd
     host
     '''
     regex = re.compile('[^\w-]+')  
     def makekey3(line:str):
          for word in regex.split(line):
               if len(word):
                    yield word

     for i in makekey3(chekword):
          print(i)



# 邮箱
# \w+[-. \w]*@[\w-]+(\.[\w-]+)+
# html提取
# <[^<>]+>(.*)<[^<>]+>
# 如果要匹配标记a
# r'<(\W+)[^<>]+>(.*)(</\1>)'
# URL提取
# (\w+)://([^\s]+)
# 身份证验证
# 身份证验证需要使用公式计算,最严格的应该实名验证。
# \d{17}[0-9xX]|\d{15}
# 强密码
# Aatb32_ _67mnq
# Aatb32_ _67m. nq
# 中国是一个伟大的国家aA_ 8
# 10-15位，其中包含大写字母、小写字母、数字和下划线
# ^\W{10,15}$
# 如果测试有不可见字符干扰使用^\W{10,15}\r?$
# 看似正确，但是,如果密码有中文呢?
# ^[a-ZA-Z0-9_ ]{10,15}$


