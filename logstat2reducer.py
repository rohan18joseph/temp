import re
import sys
from operator import itemgetter
from collections import defaultdict
''''
dict_time = {}
dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    time, ipaddr = ip.split(' ')
    if time not in dict_time:
        dict_time[time] = {}
    if ipaddr not in dict_time[time]:
        dict_time[time][ipaddr]=0
    num = int(num)
    dict_time[time][ipaddr] += num

for time in dict_time:
    temp = dict_time[time]
    temp = sorted(temp.items(), key=lambda x:x[1], reverse = True)
    #print(time)
    for i in range(3):
        #print(temp[i])
        print('{0} {1}'.format(time, ' '.join(str(j) for j in temp[i])))
'''
dict_time = {}
start_time, end_time = sys.argv[1].split('-')
start_time = int(start_time)
end_time = int(end_time)
#start_time = int(sys.argv[1]) #int(input("Enter starting time range: (format 0-24)"))
#end_time = int(sys.argv[2]) #int(input("Enter ending time range: (format: 0-24)"))

time_range_raw = [x for x in range(start_time,end_time+1)]
time_range = ['0' + str(x) + ':00'if len(str(x))<2 else '' + str(x) + ':00' for x in time_range_raw]

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    time, ipaddr = ip.split(' ')
    num = int(num)
    if time not in time_range:
        continue
    if ipaddr not in dict_time:
        dict_time[ipaddr] = num
    else:
        dict_time[ipaddr]+=num


temp = dict_time
temp = sorted(temp.items(), key=lambda x:x[1], reverse = True)

for i in range(3):
    #print(temp[i])
    print('{0}'.format(' '.join(str(j) for j in temp[i])))

'''
dict_time[time] = dict_time.get()
num = int(num)
dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num
except ValueError:
pass
'''
'''
sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
for ip, count in sorted_dict_ip_count:
    print('%s\t%s' % (ip, count))
'''