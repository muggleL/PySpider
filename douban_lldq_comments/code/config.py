HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML'
              ', like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}

# you cookies
# 如果没有 cookie 只能 获取 200 条评论
COOKIES = {
'Cookie': 'bid=0KB0Qc8rcng; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1551489895%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; dbcl2="121781291:U04HZob4JaI"; ck=g97h; __utma=30149280.709130965.1551489970.1551489970.1551489970.1; __utmc=30149280; __utmz=30149280.1551489970.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.1355118323.1551489970.1551489970.1551489970.1; __utmb=223695111.0.10.1551489970; __utmc=223695111; __utmz=223695111.1551489970.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utmt_t1=1; push_doumail_num=0; push_noty_num=1; RT=s=1551489986475&r=https%3A%2F%2Fmovie.douban.com%2Fexplore; _pk_id.100001.4cf6=753a816d724f0658.1551489895.1.1551489987.1551489895.; __utmb=30149280.6.8.1551489987168'
}

RE_CONTENT = '<div class="comment-item".*?<a title="(.*?)" href="(.*?)">.*?"allsta' \
             'r(\d{1})0.*?class="comment-time " title="(.*?)">.*? <span class="sho' \
             'rt">(.*?)</span>'

RE_USER_CONTENT = '<div class="pic">.*?<a tit' \
                  'le="(.*?)" href="https://movie.doub' \
                  'an.com/subject/(.*?)/.*?class="rating(\d)-t"'

# db_host = '192.168.3.74'
db_host = '192.168.1.172'

#db_host = '172.18.72.206'
db_port = 27017
db_name = 'liulang_comments_2'
client_name = 'douban'
