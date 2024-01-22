import pandas as pd
from datetime import datetime

def cre(data):
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                    orient='records',
                    dtype={'mid':str,'info':str,'char':str})
    new = {
        "mid":data['mid'],
        "info":data['info'],
        "char":data['char']
        }
    new_df = pd.DataFrame(new,index=[0])
    resurts = pd.concat([DF,new_df],ignore_index=True)
    return resurts.to_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',orient='records',force_ascii=False,indent=4)

def put(data):
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                    orient='records',
                    dtype={'mid':str,'info':str,'char':str})
    chn = {
        "mid":data['mid'],
        "info":data['info'],
        "char":data['char']
        }
    DF.loc[DF['mid']==chn['mid'],'info'] = chn['info']
    DF.loc[DF['mid']==chn['mid'],'char'] = chn['char']
    return DF.to_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',orient='records',force_ascii=False,indent=4)

def delete(data):
    DF = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',
                    orient='records',
                    dtype={'mid':str,'info':str,'char':str})
    d = {
        "mid":data['mid']
        }
    ind = DF[DF['mid']==d['mid']].index
    DF.drop(ind, inplace=True)
    return DF.to_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\info_.json',orient='records',force_ascii=False,indent=4)

def RM(data):
    wk = pd.read_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\RM_.json',
                        orient='records',
                        dtype={'mid':str,'name':str,'month':str})
    now = datetime.now().strftime('%Y년 %m월')
    new = {
        "mid":data['mid'],
        "name":data['name'],
        "month":data['month']
    }
    new_df = pd.DataFrame(new,index=[0])
    resurts = pd.concat([wk,new_df],ignore_index=True)
    ind = resurts[resurts['month'] != now].index
    resurts.drop(ind,inplace=True)
    return resurts.to_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\RM_.json',orient='records',force_ascii=False,indent=4)