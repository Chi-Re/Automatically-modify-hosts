import subprocess
import time
import urllib.request

###########################
# 测试成功,可以正常使用,只不过有一点点的问题
# 请在使用之前备份好你的hosts文件,因为这风险太大
# 使用中时可能会报错,不要害怕,这是正常现象,多试几次就好,或者等待一会
# ipconfig/flushdns
###########################

# 你的hosts文件路径
path = 'C:\\Windows\\System32\\drivers\\etc'


# 获得网页源文件(很直接的方法)
def requesturl_notice(url):
    data = 'https://ip.tool.chinaz.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.190',
    }

    request = urllib.request.Request(url=data + url, headers=headers)

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 这些是需要获得网站的ip
githubs = ['github.com',
           'gist.github.com',
           'docs.github.com',
           'github.global.ssl.fastly.net',
           'assets-cdn.github.com',
           'raw.githubusercontent.com',
           'gist.githubusercontent.com',
           'cloud.githubusercontent.com',
           'camo.githubusercontent.com',
           'avatars.githubusercontent.com',
           'avatars0.githubusercontent.com',
           'avatars1.githubusercontent.com',
           'avatars2.githubusercontent.com',
           'avatars3.githubusercontent.com',
           'avatars4.githubusercontent.com',
           'avatars5.githubusercontent.com',
           'avatars6.githubusercontent.com',
           'avatars7.githubusercontent.com',
           'avatars8.githubusercontent.com']

# 3607行是ip(测试)
# er = 0
# for i in githubs:
#     er += 1

true = False
text = ''
texts = []

for ie in githubs:
    wert = requesturl_notice(ie)
    with open('whitt.html', 'w', encoding='utf-8') as fdg:
        fdg.write(wert)
    print(ie)
    # TODO 奇怪的bug,可能会在你使用时失效,或者你该等一等?
    wert2 = wert.split('<span class="Whwtdhalf w15-0 lh45" style="cursor:pointer;" onclick="AiWenIpData(\'')[1]
    print(wert2)
    for i in wert2:
        if i != "'":
            text += i
        else:
            break
    texts += [text]
    text = ''

print(texts)

generate = ''
for q, w in zip(githubs, texts):
    generate += w + '    ' + q + '\n'
    print(generate)
# 你可以把这个改成你的
host = f'''# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host
# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
# GitHub Start 
{generate}# GitHub End'''

with open(f'{path}\\hosts', 'w', encoding='utf-8') as fs:
    fs.write(host)

# 等待1s后执行刷新ip命令
time.sleep(1)
subprocess.Popen('ipconfig/flushdns', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # with open(f'whitt{er}.html', 'w', encoding='utf-8') as f:
    #     f.write(wert)

# print(host[3:4])


# 20.205.243.166     github.com
# 59.24.3.173        gist.github.com
# 104.244.43.231     github.global.ssl.fastly.net
# 185.199.110.153    assets-cdn.github.com
# 185.199.111.133    raw.githubusercontent.com
# 185.199.108.133    raw.githubusercontent.com
# 151.101.184.133    gist.githubusercontent.com
# 151.101.184.133    cloud.githubusercontent.com
# 151.101.184.133    camo.githubusercontent.com
# 185.199.109.133    avatars.githubusercontent.com
