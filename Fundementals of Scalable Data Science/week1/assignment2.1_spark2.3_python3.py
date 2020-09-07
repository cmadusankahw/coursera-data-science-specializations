#!/usr/bin/env python
# coding: utf-8

# ### Assignment 2
# Welcome to Assignment 2. This will be fun. It is the first time you actually access external data from ApacheSpark. 
# 
# #### You can also submit partial solutions
# 
# Just make sure you hit the play button on each cell from top to down. There are three functions you have to implement. Please also make sure than on each change on a function you hit the play button again on the corresponding cell to make it available to the rest of this notebook.
# 

# This notebook is designed to run in a IBM Watson Studio default runtime (NOT the Watson Studio Apache Spark Runtime as the default runtime with 1 vCPU is free of charge). Therefore, we install Apache Spark in local mode for test purposes only. Please don't use it in production.
# 
# In case you are facing issues, please read the following two documents first:
# 
# https://github.com/IBM/skillsnetwork/wiki/Environment-Setup
# 
# https://github.com/IBM/skillsnetwork/wiki/FAQ
# 
# Then, please feel free to ask:
# 
# https://coursera.org/learn/machine-learning-big-data-apache-spark/discussions/all
# 
# Please make sure to follow the guidelines before asking a question:
# 
# https://github.com/IBM/skillsnetwork/wiki/FAQ#im-feeling-lost-and-confused-please-help-me
# 
# 
# If running outside Watson Studio, this should work as well. In case you are running in an Apache Spark context outside Watson Studio, please remove the Apache Spark setup in the first notebook cells.

# In[ ]:


from IPython.display import Markdown, display
def printmd(string):
    display(Markdown('# <span style="color:red">'+string+'</span>'))


if ('sc' in locals() or 'sc' in globals()):
    printmd('<<<<<!!!!! It seems that you are running in a IBM Watson Studio Apache Spark Notebook. Please run it in an IBM Watson Studio Default Runtime (without Apache Spark) !!!!!>>>>>')


# In[ ]:


get_ipython().system('pip install pyspark==2.4.5')


# In[ ]:


try:
    from pyspark import SparkContext, SparkConf
    from pyspark.sql import SparkSession
except ImportError as e:
    printmd('<<<<<!!!!! Please restart your kernel after installing Apache Spark !!!!!>>>>>')


# In[ ]:


sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))

spark = SparkSession     .builder     .getOrCreate()


# This is the first function you have to implement. You are passed a dataframe object. We've also registered the dataframe in the ApacheSparkSQL catalog - so you can also issue queries against the "washing" table using "spark.sql()". Hint: To get an idea about the contents of the catalog you can use: spark.catalog.listTables().
# So now it's time to implement your first function. You are free to use the dataframe API, SQL or RDD API. In case you want to use the RDD API just obtain the encapsulated RDD using "df.rdd". You can test the function by running one of the three last cells of this notebook, but please make sure you run the cells from top to down since some are dependant of each other...

# In[ ]:


#Please implement a function returning the number of rows in the dataframe
def count():
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    #some more help: https://www.w3schools.com/sql/sql_count_avg_sum.asp
    return spark.sql('select ### as cnt from washing').first().cnt


# Now it's time to implement the second function. Please return an integer containing the number of fields (columns). The most easy way to get this is using the dataframe API. Hint: You might find the dataframe API documentation useful: http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame

# In[ ]:


def getNumberOfFields():
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    return len(df.###)


# Finally, please implement a function which returns a (python) list of string values of the field names in this data frame. Hint: Just copy&past doesn't work because the auto-grader will create a random data frame for testing, so please use the data frame API as well. Again, this is the link to the documentation: http://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame

# In[ ]:


def getFieldNames():
    #TODO Please enter your code here, you are not required to use the template code below
    #some reference: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#pyspark.sql.DataFrame
    return df.###


# Now it is time to grab a PARQUET file and create a dataframe out of it. Using SparkSQL you can handle it like a database. 

# In[ ]:


get_ipython().system('wget https://github.com/IBM/coursera/blob/master/coursera_ds/washing.parquet?raw=true')
get_ipython().system('mv washing.parquet?raw=true washing.parquet')


# In[ ]:


df = spark.read.parquet('washing.parquet')
df.createOrReplaceTempView('washing')
df.show()


# The following cell can be used to test your count function

# In[ ]:


cnt = None
nof = None
fn = None

cnt = count()
print(cnt)


# The following cell can be used to test your getNumberOfFields function

# In[ ]:


nof = getNumberOfFields()
print(nof)


# The following cell can be used to test your getFieldNames function

# In[ ]:


fn = getFieldNames()
print(fn)


# Congratulations, you are done. So please submit your solutions to the grader now.
# 
# # Start of Assignment-Submission
# 
# The first thing we need to do is to install a little helper library for submitting the solutions to the coursera grader:
# 

# In[ ]:


get_ipython().system('rm -f rklib.py')
get_ipython().system('wget https://raw.githubusercontent.com/IBM/coursera/master/rklib.py')


# Now it’s time to submit first solution. Please make sure that the token variable contains a valid submission token. You can obtain it from the coursera web page of the course using the grader section of this assignment.
# 
# Please specify you email address you are using with cousera as well.
# 

# In[ ]:


from rklib import submit, submitAll
import json

key = "SVDiVSHNEeiDqw70MIp2vA"

if type(23) != type(cnt):
    raise ValueError('Please make sure that "cnt" is a number')
    
if type(23) != type(nof):
    raise ValueError('Please make sure that "nof" is a number')

if type([]) != type(fn):
    raise ValueError('Please make sure that "fn" is a list')

email = #### your code here ###
token = #### your code here ### (have a look here if you need more information on how to obtain the token https://youtu.be/GcDo0Rwe06U?t=276)

parts_data = {}
parts_data["2FjQw"] = json.dumps(cnt)
parts_data["j8gMs"] = json.dumps(nof)
parts_data["xaauC"] = json.dumps(fn)


submitAll(email, token, key, parts_data)

