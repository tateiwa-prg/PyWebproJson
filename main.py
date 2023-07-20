#json filenameを指定
filename='WEBPRO_inputSheet_11_result_AC.json'
#filename='test.json'
##################################################







import pandas as pd
import numpy as np
import json

daynum=360
#daynum=5
OutJson={}

def getJsonFile():
    with open('./files/'+filename,encoding="utf-8") as f:
        inputjson = json.load(f)
    return inputjson

def main():
    ij=getJsonFile()
    #print(ij)
    IfJson(ij,"")
    #print(OutJson)

    header=[]
    data=[]
    for key in OutJson:
        header.append(key)
        data.append(OutJson[key])

    data_t = np.array(data).T

    #print(header)
    #print(data_t)

    df = pd.DataFrame(data=data_t, columns=header)
    #print(df)
    ofn='./files/'+filename+'_out.csv'
    df.to_csv(ofn)
  



def IfJson(json,moji):

    key_arr=json.keys()
    #print(key_arr)

    if len(key_arr)>0:
        for key in key_arr:
            val=json[key]
            #print(val)
            head=moji+"_"+key

            if isinstance(val, list): # 値がリスト（配列）かどうかを判定する
                #print('リストです。')
                if len(val)>daynum:
                    #print(head,val)
                    OutJson[head]=val

            elif isinstance(val, dict):
                #print("dict",val)
                IfJson(val,head)
            
            '''
            else:
                print("FIN")
            '''


if __name__ == '__main__':
    main()
