import matplotlib.pyplot as plt
import numpy as np
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
visitors = [1200,1350,1180,1420,1600,2100,1900]

plt.figure(figsize=(10,6))
plt.plot(days,visitors,marker = 'o',linewidth =2, color= "#041872")
plt.fill_between(range(len(days)),visitors,alpha = 0.3,color = '#667eea')
plt.title('wensite Visitor - Week Overview', fontsize = 16, fontweight = 'bold')
plt.xlabel('Day of week',fontsize = 12 )
plt.ylabel('Numbers of visitor', fontsize = 12)
plt.grid(True,alpha = 0.3)
plt.tight_layout()
plt.show()