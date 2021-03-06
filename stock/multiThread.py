from django.core.mail import send_mail as core_send_mail
from django.core.mail import EmailMultiAlternatives
import threading
from django.core.mail import EmailMessage
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from .models import User
from datetime import datetime
import time

from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from .forms import RegisterForm, LoginForm
from django.views.generic import View
from .models import User, Stock, Bookmark
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import plotly
from functools import wraps
import plotly.express as px
import plotly.graph_objs as go
import datetime
from .utils import get_plot,get_bar_graph
from django.core.paginator import Paginator
from PIL import Image
import os
import numpy as np
from django.contrib.auth import login as login_a, authenticate
from .prediction import predict, getLabels

class EmailThread(threading.Thread):
    def __init__(self, address, username):
        self.addess = address
        threading.Thread.__init__(self)

    def run (self):

        user = User.objects.filter(email=self.email)
        bookmarks = Bookmark.objects.all().filter(user__email=user.email) 

        a = [1, 2, 3]
        >>> a.append(4)

        company_name=[]
        last_pattern=[]
        increase_or_decease=[] 
        total=[]
        
        for bookmark in bookmarks :
            company_name.append(bookmark.stock.company_name)
            last_pattern.append(bookmark.stock.last_pattern)
            increase_or_decease.append(bookmark.stock.increase_or_decrease)

        
            
        print(bookmark.stock.stock_code)
        # bookmark.stock.last_pettern  이랑 increase_or_decrease 미리 for문돌려서 미리 리스트에 담아두기

        while(1): 
            
            now = datetime.datetime.now()

            if now.hour == user.mail_alarm_time_hour and now.minute == user.mail_alarm_time_hour :

                title = "stocker에서 " + self.username + "님께 보내는 북마크 알림 메일이 도착했어요!"
                contents =  "안녕안녕" # html 형식으로 보내야 깔끔할 것 같긴 함. sendMail.py 참고 . 리스트 뿌려주기 
                # 이미지는 어떻게 보여줄 지 고민 중 ..!
               
                msg = EmailMultiAlternatives(title, contents, to=[self.addess])
                msg.content_subtype = 'html'
                msg.send()

                time.sleep(1)
                print('스레드 한 개 작업 완룟!')

                return 0
            

        else :
            # print(now.hour)
            # print(now.minute)
            # time.sleep(1)
            pass



#이렇게 하면 views.py 에 임포트 될때 딱 한번 실행 됨 
#views.py에서는 이거 실행하기 위해 임포트 하는거고 views.py 안에서 이 클래스를 사용할 일은 없고 사용 하려면 디자인을 바꿔야함 
# def send_email(subject, body, to_email): 


# 알람 성정한 user 객체 수 만큼  for문 돌리기 
alarm_users=User.objects.exclude(mail_alarm_time_hour=None)

for alarm_user in alarm_users :
    EmailThread(alarm_user.email,alarm_user.username).start()  #start()가 run메서드를 호출함


#이거를 shell 에서 한번 테스트 해봤는데 shell 에서 exit()해도 계속 실행 됨 그 cmd를 종료해야지 죽음 이게 웃긴게 ctr+c 도 안먹힘 