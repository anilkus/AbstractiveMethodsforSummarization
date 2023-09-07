# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 15:11:56 2023

@author: LENOVO
"""

# Dosyanın içeriğini oku
with open("C:/Users/LENOVO/Desktop/TEZ/Veri Ön İşleme/Abstracts/z_Uludağ Üniversitesi Tıp Fakültesi Dergisi/971366-1880431.txt", 'r',encoding="utf-8") as text2:
    abstract=text2.read()
with open("C:/Users/LENOVO/Desktop/TEZ/Veri Ön İşleme/Çalışmanın Özetleri/GPT/z_Uludağ Üniversitesi Tıp Fakültesi Dergisi/971366-1880431.txt", 'r',encoding="utf-8") as text:
    islenecek=text.read()
    summary=islenecek

from rouge import Rouge
ROUGE = Rouge()

print(ROUGE.get_scores(summary, abstract))


        