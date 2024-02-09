import sys 
import csv 

#csv 文件格式
#无头列
#表名,表注释,列名,列注释,列数据类型,列长度,列精度,是否为主键
#table name , table comment ,column name ,column comment , column data type , column length ,column precision , is Primary key 
#最后一行不能有空行.
#没有用"/"代替,不能空着.


createTable=''   #创建表语句
tableComment=''  #表注释语句
columnComment='' #列注释语句
primaryKey=''    #主键语句
columnFirst=' '  #首行都号语句

#读取csv语句
with open(sys.argv[1],'r') as f:
    filePath=csv.reader(f)
    
    #逐行读取csv内容
    for i in filePath:
        #csv第一行文件特殊输出内容.
        if filePath.line_num==1:
            createTable='create table {} ( '.format(i[0])    #构造创建表的create  内容.
            tableComment='comment on table {} is \'{}\';'.format(i[0],i[1])  #表注释在第一行写
            columnFirst=' '   #首行那么逗号会被去掉.
            primaryKey='alter table {} add primary key ('.format(i[0])   #创建表主键内容.
        else :
            columnFirst=','   #非首行该变量会被重置成逗号.

        #拼接列内容.
        createTable=createTable+'\n'+'{} {} {}({},{})'.format(columnFirst,i[2],i[4],i[5],i[6])
        #列注释
        columnComment=columnComment+'\n'+'comment on column {}.{} is \'{}\';'.format(i[0],i[2],i[3])

        #第8列是否是主键的判断.
        if i[7].upper()=='Y':
            primaryKey=primaryKey+'{} {}'.format(columnFirst,i[2])


#创建表语句和主键语句,封口.
createTable=createTable+'\n'+');'
primaryKey=primaryKey+');'

#显示内容.
#创建表语句有一个简单的整容.
print(createTable.replace('(/,/)','').replace(',/)',')'))
print(' ')
print(primaryKey)
print(' ')
print(tableComment)
print(' ')
print(columnComment)
