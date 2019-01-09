# import datetime

from datetime import *
now = datetime.now()

from gmail import *

once = 0

while once == 0:
    if now.day == 7:
        gmail = GMail('Bankers <bankers.store69@gmail.com>','ub123456')
#msg = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')   #plain text
        n = '''<p>Sếp th&acirc;n mến,</p>
<p>Em viết thư n&agrave;y trong t&acirc;m trạng v&ocirc; c&ugrave;ng b&igrave;nh tĩnh, tự tin.</p>
<p>H&ocirc;m nay em bị ốm, v&igrave; vậy, em muốn ở nh&agrave; nghỉ.</p>
<p>Sếp duyệt gi&uacute;p em nha.</p>
<p>Th&acirc;n Sếp.</p>'''
        msg = Message('Đơn xin nghỉ phép',to='PhongNH2 <phong.nh@ubgroup.vn>',html=n) 
        gmail.send(msg)