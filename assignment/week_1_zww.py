#-*- comding:utf-8   -*-

'''
python环境安装

yum  install git -y

yum -y install git gcc make patch zlib-devel gdbm-devel openssldevel sqlite-devel bzip2-devel readline-devel mysql-devel gcc-devel python-devel   安装基本库

useradd python    后面环境建议不要用root  避免全局操作
echo python | passwd python  --stdir

curl -L https://raw.githubusercontent.com/yyuu/pyenvinstaller/master/bin/pyenv-installer | bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer   | bash
安装pyenv

vim ~/.bash_profile   添加最后变量
export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


. ~/.bash_profile   加载一下文件
pyenv 检查一下安装完成没有


pyenv  install  -l  查看可以安装什么版本

使用缓存方式安装
cd ~/.pyenv/
mkdir cache
导入python 3.5.3 gz   xz  tgz  3.6.6 xz  tgz 五个版本到目录中
pyenv install 3.6.6 -v  本地库安装

pyenv versions  查看当前全局python是什么版本
pyenv  global  3.6.6  指定全局版本    需要重新登录加载
python  -V  查看python 现在的使用版本确认

pyenv shell 3.6.6  当前会话指定版本

pyenv local  3.6.6  指定当前目录递归继承版本
mkdir  -p  magedu/projects/web
cd  magedu/projects/web/
pyenv  versions
pyenv local  3.6.6    创建目录指定版本
指定目录版本后会生成一个隐藏文件python-version  里面会写入对应指定版本


pyenv  virtualenv 3.6.6 mag366  虚拟环境，比如安装库，生成不同的库，然后可以通过pyenv local  mag366  指定到某个目录，然后pip安装库，不会安装到公共空间里面去，只会安装到这个虚拟的环境中，因为不同的项目需要不同的库支持，但是不能同意安装到公共库，所以可以创建虚拟环境，指定特定的库，然后指定到特定的目录。
pip  list  安装之后可以切换不同的环境看自己的库。  特定为同python版本，然后新建虚拟环境

那虚拟环境安装的东西在哪，
      家目录   .pyenv/versions/版本/虚拟环境mag366/lib/版本/site-packages/
公共环境
     直接进入版本，不进入虚拟环境就是公共环境的

pip,指定下载源
mkdir ~/.pip
touch   pip.conf
配置文件在~/.pip/pip.conf
vi  pip.conf
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
trusted-host=mirrors.aliyun.com
                                 ##或者https://pypi.tuna.tsinghua.edu.cn/simple  清华源

pip  list 查看所有库
pip freeze > requirements  生成一个库文件
pip install  -r  requirements  可以安装文件中所有的库


如果是windows  那就是 win + R  输入.  打开， 新建pip文件夹，新建pip.ini文件，内容一样

pip  install ipython
建议之后的再虚拟环境安装，不要在功能环境安装


pip install jupyter
Jupyter是基于WEB的交互式笔记本，其中可以非常方便的使用Python。
安装lupyter，也会依赖安装ipython的
$ pip install jupyter
$ jupyter notebook help
$ jupyter notebook --ip = 0.0.0.0  --no-browser   ##不弹出浏览器
$ ss -tanl

jupyter notebook --ip=0.0.0.0 --port=8888  --no-browser  启动
http://(localhost.localdomain or 127.0.0.1):8888/?token=5d904bc28b818ea25432034de03b6d38e30449d9a3f1e778
需要带上token自动登录

chkconfig firewalld off   关闭防火墙
cd  magedu/projects/web/  制定的虚拟项目中

'''

'''
linux  使用
1.文件名最长255个字节
2.包括路径在内文件名称最长4095个字节
3.mv/tmp/b{,.dir}     mv /tmp/b   /tmp/b.dir     修改b文件为b.dir
4.ifconfig eth0 | head-2 | tail-1 | cut-d: -f2| cut-d' '-f1 14集 13分钟

/bin   存放二进制可执行文件，存放着最经常使用的命令
/boot  存放引导文件，内核文件等
/dev 设备文件及特殊文件存储位置
/etc   存放系统配置文件
/home  普通用户的主目录
/lib  标准程序设计库，又叫动态链接共享库，作用类似windows里的.dll文件
/mnt  临时文件挂载点
/opt  额外安装的可选应用程序包所放置的位置
/proc  虚拟的目录，系统内存的映射。可直接访问这个目录来获取系统信息
/ root  超级用户主目录
/sbin 存放二进制可执行文件，管理类的基本命令，只有root才能访问
/tmp   sbin用于存放各种临时文件
/var   这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包 括各种日志文件
/usr  用于存放系统应用程序，也是最庞大的目录

cd   pwd  ls    
touch  生成文件    mkdir  生成目录
rm  -rf  递归删除不询问   mv移动  cp  
cat  more  less  head  tail -fn 动态查看
grep  查看
ps -ef 所有进程
uname -a  显示当前内核版本
cat /proc/cpuinfo 显示CPU 的信息
cat /proc/version 显示操作系统版本
cat /etc/redhat-release 查看centos版本
查看防火墙状态：service iptables status
开启防火墙：service iptables start
关闭防火墙：service iptables stop
free  查看内存使用情况
Iostat   监控磁盘I/O使用情况
iftop   监控流量使用情况
vmstat  虚拟内存统计
netstat  网络状态统计
chmod  777   修改权限

'''