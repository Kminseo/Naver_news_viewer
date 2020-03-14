# -*- coding: utf-8 -*-
import os, sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import threading
import datetime,time
import requests
from bs4 import BeautifulSoup

def load_politics(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find(class_='ranking_section').find('ol').find_all('dl'):
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

def load_eoconomy(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find_all(class_='ranking_section othbor')[0].find('ol').find_all('dl'): # 위치 바뀌면 여기 부분 교체
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

def load_society(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find_all(class_='ranking_section othbor')[1].find('ol').find_all('dl'): # 위치 바뀌면 여기 부분 교체
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

def load_life(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find_all(class_='ranking_section othbor')[2].find('ol').find_all('dl'): # 위치 바뀌면 여기 부분 교체
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

def load_global(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find_all(class_='ranking_section othbor')[3].find('ol').find_all('dl'): # 위치 바뀌면 여기 부분 교체
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

def load_it(soup):
    politisc_list=[[],[]]
    for tr_tag in soup.find_all(class_='ranking_section othbor')[4].find('ol').find_all('dl'): # 위치 바뀌면 여기 부분 교체
            dt_list = tr_tag.find_all('dt')
            for dt in dt_list:
                info = dt.find('a')
                politisc_list[0].append(info.get('href'))
                politisc_list[1].append(info.get('title'))
    return politisc_list

class Market_Widget(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        threading.Thread.__init__(self)
        UI_add = './ui/news_viewer.ui'
        uic.loadUi(UI_add, self)
        self.thread_kill = False
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')
        self.Date_label.setText(self.today)
        self.label_setting()
        self.t1 = threading.Thread(target=self.reload)
        self.t1.start()
        self.reload_btn.clicked.connect(self.thread_starter)

    def thread_starter(self):
        self.t1.join()
        self.t1 = threading.Thread(target=self.reload)
        self.t1.start()

    def reload(self):
        while(1):
            self.load_data()
            self.update_news()
            if(self.auto_chk.isChecked() == False or self.thread_kill == True):
                break
            elif self.auto_chk.isChecked() == True:
                time.sleep(120)

    def label_setting(self):
        self.pol_1.setOpenExternalLinks(True)
        self.pol_2.setOpenExternalLinks(True)
        self.pol_3.setOpenExternalLinks(True)
        self.pol_4.setOpenExternalLinks(True)
        self.pol_5.setOpenExternalLinks(True)

        self.eco_1.setOpenExternalLinks(True)
        self.eco_2.setOpenExternalLinks(True)
        self.eco_3.setOpenExternalLinks(True)
        self.eco_4.setOpenExternalLinks(True)
        self.eco_5.setOpenExternalLinks(True)

        self.it_1.setOpenExternalLinks(True)
        self.it_2.setOpenExternalLinks(True)
        self.it_3.setOpenExternalLinks(True)
        self.it_4.setOpenExternalLinks(True)
        self.it_5.setOpenExternalLinks(True)

        self.glo_1.setOpenExternalLinks(True)
        self.glo_2.setOpenExternalLinks(True)
        self.glo_3.setOpenExternalLinks(True)
        self.glo_4.setOpenExternalLinks(True)
        self.glo_5.setOpenExternalLinks(True)

        self.soc_1.setOpenExternalLinks(True)
        self.soc_2.setOpenExternalLinks(True)
        self.soc_3.setOpenExternalLinks(True)
        self.soc_4.setOpenExternalLinks(True)
        self.soc_5.setOpenExternalLinks(True)

        self.lif_1.setOpenExternalLinks(True)
        self.lif_2.setOpenExternalLinks(True)
        self.lif_3.setOpenExternalLinks(True)
        self.lif_4.setOpenExternalLinks(True)
        self.lif_5.setOpenExternalLinks(True)
    

    def load_data(self):
        html = requests.get('https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111').text
        soup = BeautifulSoup(html,'html.parser')
        self.society_data = load_society(soup)
        self.it_data = load_it(soup)
        self.life_data = load_life(soup)
        self.economy_data = load_eoconomy(soup)
        self.global_data = load_global(soup)
        self.politics_data = load_politics(soup)

    def update_news(self):
        self.pol_1.setText("<a href=\"https://news.naver.com/"+self.politics_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.politics_data[1][0]+"<\a>")
        self.pol_2.setText("<a href=\"https://news.naver.com/"+self.politics_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.politics_data[1][1]+"<\a>")
        self.pol_3.setText("<a href=\"https://news.naver.com/"+self.politics_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.politics_data[1][2]+"<\a>")
        self.pol_4.setText("<a href=\"https://news.naver.com/"+self.politics_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.politics_data[1][3]+"<\a>")
        self.pol_5.setText("<a href=\"https://news.naver.com/"+self.politics_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.politics_data[1][4]+"<\a>")
        
        self.eco_1.setText("<a href=\"https://news.naver.com/"+self.economy_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.economy_data[1][0]+"<\a>")
        self.eco_2.setText("<a href=\"https://news.naver.com/"+self.economy_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.economy_data[1][1]+"<\a>")
        self.eco_3.setText("<a href=\"https://news.naver.com/"+self.economy_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.economy_data[1][2]+"<\a>")
        self.eco_4.setText("<a href=\"https://news.naver.com/"+self.economy_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.economy_data[1][3]+"<\a>")
        self.eco_5.setText("<a href=\"https://news.naver.com/"+self.economy_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.economy_data[1][4]+"<\a>")

        self.it_1.setText("<a href=\"https://news.naver.com/"+self.it_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.it_data[1][0]+"<\a>")
        self.it_2.setText("<a href=\"https://news.naver.com/"+self.it_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.it_data[1][1]+"<\a>")
        self.it_3.setText("<a href=\"https://news.naver.com/"+self.it_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.it_data[1][2]+"<\a>")
        self.it_4.setText("<a href=\"https://news.naver.com/"+self.it_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.it_data[1][3]+"<\a>")
        self.it_5.setText("<a href=\"https://news.naver.com/"+self.it_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.it_data[1][4]+"<\a>")

        self.soc_1.setText("<a href=\"https://news.naver.com/"+self.society_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.society_data[1][0]+"<\a>")
        self.soc_2.setText("<a href=\"https://news.naver.com/"+self.society_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.society_data[1][1]+"<\a>")
        self.soc_3.setText("<a href=\"https://news.naver.com/"+self.society_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.society_data[1][2]+"<\a>")
        self.soc_4.setText("<a href=\"https://news.naver.com/"+self.society_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.society_data[1][3]+"<\a>")
        self.soc_5.setText("<a href=\"https://news.naver.com/"+self.society_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.society_data[1][4]+"<\a>")

        self.glo_1.setText("<a href=\"https://news.naver.com/"+self.global_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.global_data[1][0]+"<\a>")
        self.glo_2.setText("<a href=\"https://news.naver.com/"+self.global_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.global_data[1][1]+"<\a>")
        self.glo_3.setText("<a href=\"https://news.naver.com/"+self.global_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.global_data[1][2]+"<\a>")
        self.glo_4.setText("<a href=\"https://news.naver.com/"+self.global_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.global_data[1][3]+"<\a>")
        self.glo_5.setText("<a href=\"https://news.naver.com/"+self.global_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.global_data[1][4]+"<\a>")

        self.lif_1.setText("<a href=\"https://news.naver.com/"+self.life_data[0][0]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.life_data[1][0]+"<\a>")
        self.lif_2.setText("<a href=\"https://news.naver.com/"+self.life_data[0][1]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.life_data[1][1]+"<\a>")
        self.lif_3.setText("<a href=\"https://news.naver.com/"+self.life_data[0][2]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.life_data[1][2]+"<\a>")
        self.lif_4.setText("<a href=\"https://news.naver.com/"+self.life_data[0][3]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.life_data[1][3]+"<\a>")
        self.lif_5.setText("<a href=\"https://news.naver.com/"+self.life_data[0][4]+\
            "\"style=\"color: black;text-decoration:none;\">"+self.life_data[1][4]+"<\a>")

    def closeEvent(self, event):
        self.thread_kill = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = Market_Widget()
    main_dialog.show()
    app.exec_()	
    
                

    
    
