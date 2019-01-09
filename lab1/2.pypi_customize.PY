#CUSTOMIZE NỘI DUNG GỬI EMAIL

from random import *

#import random
# n_content = n.replace("timeline", random.choice(timeline_list))

timeline_list = ["đi học bình thường", "học muộn 30p", "học sớm 30p"]

n = '''<p><em>Xin ch&agrave;o anh chị em,</em></p>
<p>H&ocirc;m nay Anh em <span style="text-decoration: underline;"><strong>{{timeline}} nh&eacute;</strong></span>.</p>
<p>Hết email rồi.</p>'''

# n_content = n.replace("timeline", "đi học bình thường")         #replace: thay thế nội dung này bằng cái mới

n_content = n.replace("{{timeline}}", choice(timeline_list))        #choice nằm trong thư viện random

print(n_content)

#GỬI NHIỀU EMAIL DÙNG VÒNG LẶP FOR





