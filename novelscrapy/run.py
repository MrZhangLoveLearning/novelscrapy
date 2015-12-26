# -*- coding: utf-8 -*-

import subprocess
import db_helper
import logging

def get_text():
    subprocess.call(['scrapy', 'crawl', 'perfect_world'])
    subprocess.call(['scrapy', 'crawl', 'beat_god'])
    subprocess.call(['scrapy', 'crawl', 'night_king'])
    subprocess.call(['scrapy', 'crawl', 'swod_dynasty'])
    content = db_helper.get_send_content(10, True)
    db_helper.clear_email()
    return content

# scrapy crawl perfect_world
# scrapy crawl beat_god
# scrapy crawl night_king
# scrapy crawl swod_dynasty
if __name__ == '__main__':
    subprocess.call(['scrapy', 'crawl', 'perfect_world'])
    subprocess.call(['scrapy', 'crawl', 'beat_god'])
    subprocess.call(['scrapy', 'crawl', 'night_king'])
    subprocess.call(['scrapy', 'crawl', 'swod_dynasty'])
    if db_helper.send_art_email():  
        print "发送成功"  
        db_helper.send_art_email(to_self=True)
    else:  
        print "发送失败" 
        db_helper.send_art_email(to_self=True)  