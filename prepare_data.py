# -*- coding: utf-8 -*-
"""



"""

import pandas as pd


def read_transform_df(file_name, sheet_name=0):
    try:
        df=pd.read_excel('Data.xlsx', header=[0,1,2], sheet_name=sheet_name)
        columns=df.columns
        
        measure=columns[0][0]
        unit_of_measurement=columns[0][1]
        
        df1=df[(measure, unit_of_measurement, columns[0][2])]
        df1=pd.DataFrame({'text':df1})
        df1['measure']=[measure]*len(df1)
        df1['unit_of_measurement']=[unit_of_measurement]*len(df1)
        df2=df[(measure, unit_of_measurement, columns[1][2])]
        df2=pd.DataFrame({'text':df2})
        df2['measure']=['no_measure']*len(df2)
        df2['unit_of_measurement']=['no_unit_of_measurement']*len(df2)
        
        df_rez=pd.concat([df1,df2], axis=0, ignore_index=True)
    except:
        raise RuntimeError('error of file reading')
        return True
    
    return df_rez

if __name__=='__main__':
    file_name='Data.xlsx'
    # sheet_names=['sheet_0', 'sheet_1', 'sheet_2', 'sheet_3' ]    
    sheet_names=['sheet_'+str(i) for i in range(25)]
    flag=False
    for sheet_name in sheet_names:
        
        df=read_transform_df(file_name, sheet_name=sheet_name)
        if type(df)==bool:
            raise RuntimeError('error of file reading')
            break
        
        if flag==False:
            df_rez=df.copy()
            flag=True
        else:
            df_rez=pd.concat([df_rez, df], axis=0, ignore_index=True)
    df_rez.dropna(inplace=True)
    df_rez.to_excel('Data_rez.xlsx')
        
        