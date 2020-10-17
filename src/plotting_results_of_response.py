import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pickle
    
    
infile=open("response_study_output/respone_analysis",'rb') 
log =pickle.load(infile)   
print(log[0])

fig , ax =plt.subplots()
ax.plot(log[:,1],log[:,0])
#ax.set(xlable='time ms',,title='step function response')
ax.set_title('step function response')
ax.set_xlabel('time (ms)')
ax.set_ylabel('RPS')
ax.grid()
fig.savefig("response_study_output/step_response.png")
plt.show()