from pandas import DataFrame
from IPython import display

dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths' : [87, 91, 97, 95],
        'Science' : [83, 99, 84, 76]}
df = DataFrame(dict)

display.display(df)
print(df)
