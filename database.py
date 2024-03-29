import pandas as pd

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