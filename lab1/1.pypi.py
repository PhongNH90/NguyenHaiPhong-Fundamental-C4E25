#thu vien pypi

# https://pypi.org/project/gmail/

# pip  # chay pypi

#from tenthuvien import *

#email automation

from gmail import *

gmail = GMail('PhongNH <nangthu2405@gmail.com>','buithuha')
#msg = Message('Test Message',to='xyz <xyz@xyz.com>',text='Hello')   #plain text


n = '''<p><em>Xin ch&agrave;o anh chị em,</em></p>
<p>H&ocirc;m nay Anh em <span style="text-decoration: underline;"><strong>nghỉ học nh&eacute;</strong></span>.</p>
<p>Hết email rồi.</p>'''

# https://html5-editor.net/

#note: nếu muốn xuống dòng thì gõ ''' ở đầu và cuối dòng

msg = Message('Hello anh',to='PhongNH2 <phong.nh@ubgroup.vn>',html=n)     #gui text dang html
gmail.send(msg)