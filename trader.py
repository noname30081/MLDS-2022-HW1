import sys
import pandas as pd
import numpy as np
import math
import csv,os

if __name__ == '__main__':
     # You should not modify this part.
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
    default='training_data.csv',
    help='input training data file name')
    parser.add_argument('--testing',
    default='testing_data.csv',
    help='input testing data file name')
    parser.add_argument('--output',
    default='output.csv',
    help='output file name')
    args = parser.parse_args()
 #讀取訓練、測試數據集

    header_list = ['Open', 'High', 'Low','Close']
    #dataset_train  = pd.read_csv('./training_data.csv', encoding = 'utf-8', names=header_list)
    dataset_train  = pd.read_csv(args.training, encoding = 'utf-8', names=header_list)


    test_data_path = args.testing
    dataset_test = pd.read_csv(test_data_path, encoding = 'utf-8', names=header_list)
    row_count = len(dataset_test)
    file=open(test_data_path,'r', encoding = 'utf-8-sig')
    reader=csv.reader(file)
    High_n=0.0#最近最高價
    Low_n=0.0#最近最低價
    hold=0#股票持有
    #wrfile=open('./output.csv','w',newline='')
    wrfile=open(args.output,'w',newline='')
    write=csv.writer(wrfile)
    #print('row_count:'+str(row_count))
    for row in reader:
        try:
            close=float(row[3])
            High=float(row[1])
            Low=float(row[2])
            #判斷最近日期最高價
            if High_n<High:
                High_n=High
            #判斷最近日期最價
            if Low_n>Low or Low_n==0:
                Low_n=Low
            #威廉指標
            wr=-(High_n-close)/(High_n-Low_n)
            #print(wr)
            #不做放空
            '''if( wr>=-1 and wr<-0.8 and hold==0 and row_count>1):
                #市場超賣時買入
                hold=hold+1
                write.writerow([1])
            elif( wr<=-0.2 and wr>=-0.8 and hold==0 and row_count>1):
                #威廉交易訊號
                hold=hold+1
                write.writerow([1])
            elif(wr>-0.2 and wr<=-0 and hold==1 and row_count>1):
                #市場超買時賣出
                hold=hold-1
                write.writerow([-1])
            elif(row_count>1):
                write.writerow([0])'''
            #放空
            if( wr>=-1 and wr<-0.8 and hold==0 and row_count>1):
                #市場超賣時買入
                hold=hold+1
                write.writerow([1])
            elif( wr<=-0.2 and wr>=-0.8 and hold==0 and row_count>1):
                #威廉交易訊號
                hold=hold+1
                write.writerow([1])
            elif(wr>-0.2 and wr<=-0 and hold>=0 and row_count>1):
                #市場超買時賣出允許放空一張
                hold=hold-1
                write.writerow([-1])
            elif(row_count>1):
                write.writerow([0])
            row_count=row_count-1
        except:
            print("Error when csv read")
    file.close()
    wrfile.close()








