import configparser

cf = configparser.ConfigParser()
# list_ns = []
# try:
#     cf.read('config.ini')
#     ns = cf.get('init', 'nodes')
#     list_ns = ns.split(',')
# except Exception as ex:
#     print(ex)
# nodes = set()
# for n in list_ns:
#     nodes.add(n)
# print(nodes)

# '''服务端（UDP协议局域网广播）'''
import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
def getips():
    '''
    获取本机所有ipv4的ip地址
    '''
    ips=[]
    hostname = socket.gethostname()
    addrs = socket.getaddrinfo(hostname,None,family=socket.AF_INET)
    for item in addrs:
        ips.append(item[4][0])
    return ips
    
try:
    cf.read('config.ini')
    ns = cf.get('init', 'route')
except Exception as ex:
    print(ex)
port = 5004
network = '<broadcast>'
# s.sendto('Client broadcast message!'.encode('utf-8'), (network, PORT))
ips = getips()
for ip in ips:
    if ns in ip:
        break
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
    udp.bind((ip,port))
    #下面这行代码允许发送广播数据
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    data='所有电脑注意，测试广播'.encode('UTF-8')
    # data=b'abc'
    udp.sendto(data,(network,port))

#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)
print (myname)
print (myaddr)
#coding=utf-8
# import socket
# #广播地址，表示向本局域网所有电脑发送，下面两个地址都可以
# addr='<broadcast>'
# # addr='255.255.255.255'
# port=5004
# def getips():
#     '''
#     获取本机所有ipv4的ip地址
#     '''
#     ips=[]
#     hostname = socket.gethostname()
#     addrs = socket.getaddrinfo(hostname,None,family=socket.AF_INET)
#     for item in addrs:
#         ips.append(item[4][0])
#     return ips
# def broadcast(ip,port):
#     '''
#     广播
#     '''
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
#         udp.bind((ip,port))
#         #下面这行代码允许发送广播数据
#         udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         data='所有电脑注意，测试广播'.encode('UTF-8')
#         # data=b'abc'
#         udp.sendto(data,(addr,port))
# ips=getips()
# for item in ips:
#     broadcast(item,port)


#     '''
#     广播
#     '''
#     # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#     port=5003
#     network = '<broadcast>'
#     data = json.dumps(block)
#     # s.sendto(data.encode('utf-8'), (network, PORT))
#     ips=getips()
#     for ip in ips:
#         with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp:
#             udp.bind((ip,port))
#             #下面这行代码允许发送广播数据
#             udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#             data='所有电脑注意，测试广播'.encode('UTF-8')
#             # data=b'abc'
#             udp.sendto(data,(network,port))