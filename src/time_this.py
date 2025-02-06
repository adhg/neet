from datetime import datetime

def foo_b():
    my_list = []
    for i in range(0,1_000_000_000):
        my_list.append('A')         
    
    #str = ''.join(my_list)
    #print(str)
    
    
if __name__=='__main__':
    print ("Start...")
    start = datetime.now()
    foo_b()
    exec_time = (datetime.now()-start).total_seconds()
    print (f"Ended in {exec_time}") #Ended in 51.554514
