import time
import openpyxl
import pandas as pd
import asyncio
import os

start = time.time()
ex_path = r'excel_Compare\安.xlsx'
# 存放结果的数组
info = []
# 存放列名的字典
column_names = {}

#初始化归0
async def init_data(ex):
    df = pd.read_excel(ex)
    data = pd.DataFrame(df)
    data.fillna(0,inplace=True)
    data.to_excel(ex,index=False)

# 排序(只用执行1遍)
async def sortData(ex):
    df = pd.read_excel(ex)
    df.sort_values(by='苹果涨幅',inplace=True,ascending=False)
    df.to_excel(ex, index=False)

# 删除表格中的指定数据
def remove_data(filename):
    # 打开 Excel 文件
    df = pd.read_excel(filename)
    data = pd.DataFrame(df)
    
    # 向上移动下方单元格的数据
    max_row = len(data)
    for row in range(1, max_row):
        data.iat[row-1,0] = data.iat[row,0]
    data.iat[max_row-1,0] = None
    df.to_excel(filename, index=False)

# 求和、计量
def calc(ex,frequence):
    sign = 0
    fruit_info = []
    df = pd.read_excel(ex)
    data = pd.DataFrame(df)
    index = data.keys()
    count = df[index[0]].count()
    
    for i in range(0,count):
        if(data[index[0]][i]<=0):
            sign = i
            break
    
    for j in range(1,len(index)):
        count_op,count_ne,sum = 0,0,0
        # 大于0的情况
        for k in range(0,sign):
            num = data.iat[k,j]
            sum += num
            if num > 0:
                count_op += 1
            if num <=0:
                count_ne += 1

        if frequence <= 1:
            fruit_info.extend([index[j][:2],sum,count_op,count_ne])
        else:
            fruit_info.extend([sum,count_op,count_ne])

        count_op,count_ne,sum = 0,0,0
        # 小于0的情况
        for k in range(sign,count):
            num = data.iat[k,j]
            sum += num
            if num > 0:
                count_op += 1
            if num <=0:
                count_ne += 1
            if num is None:
                num = 0
        
        fruit_info.extend([sum,count_op,count_ne])
        if frequence <= 1:
            info.append(fruit_info)
        else:
            info[j-1].extend(fruit_info)
        fruit_info = []       

# 导出数据
def Export_result(frequence):
    # 存放结果的表格路径
    file_path = os.path.dirname(os.path.abspath(__file__)) + "/result.xlsx"
    # 存放列名
    column_names['苹果'] = []
        
    for i in range(0,frequence):
        column_names['删'+str(i+1)+'正'] = []
        column_names['删'+str(i+1)+'正的正数量'] = []
        column_names['删'+str(i+1)+'正的负数量'] = []
        column_names['删'+str(i+1)+'负'] = []
        column_names['删'+str(i+1)+'负的正数量'] = []
        column_names['删'+str(i+1)+'负的负数量'] = []

    df = pd.DataFrame(column_names)
    new_rows = pd.DataFrame(info,columns=df.columns)
    data = pd.concat([df,new_rows])
    # # 导出结果   
    data.to_excel(file_path, index=False)

frequence = int(input("请输入想删除的苹果涨幅数据个数: "))
# 创建事件循环
loop = asyncio.get_event_loop()
#定义任务列表
tasks =[init_data(ex_path),sortData(ex_path)]
# 执行任务
loop.run_until_complete(asyncio.gather(*tasks))

for i in range(0,frequence):
    remove_data(ex_path)
    calc(ex_path,i+1)

Export_result(frequence)
    
end = time.time()
print('Running time: %s Seconds'%(end-start))
