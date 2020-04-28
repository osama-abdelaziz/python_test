import datetime as dt   
start = dt.datetime.now()
print(start)
for i in range(20):
     print("hello")
end = dt.datetime.now()
print("execution:"+str(end-start))
print(start.strftime('%H %M %S'))   