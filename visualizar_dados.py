import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(low=1, high=1500, size=10)
print(y)

# grafico = plt.plot(y)
# plt.show()

#Insere a primeira linha no plot 
plt.plot(y, color='#749187', marker='o', ms=5, mec='black', markerfacecolor='white', ls='-.') 

#Insere a segunda linha no plot 
plt.plot(y*2, marker='+', color='black', ms=5)

#Rótulos
plt.xlabel('Eixo X', color = 'red', size = 12)
plt.ylabel('Eixo Y')
plt.title('Título', loc = 'left')

#gridlines 
plt.grid(axis='y' , color = 'gray',
         linestyle = '--', linewidth = 1,
         alpha = 0.8)
plt.show()
