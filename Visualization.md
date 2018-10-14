

```python
import pandas as pd
import numpy as np
import plotly

```


```python
df = pd.read_csv('./Million_Song_Subset.csv')
```


```python
#artist_hotness vs familiarity
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

plotly.tools.set_credentials_file(username='shashankprabhakar', api_key='wdZOOKmWMCiXQJZYo5Wm')


# Create a trace
trace = go.Scatter(
    x = df['artist.hotttnesss'],
    y = df['familiarity'],
    mode = 'markers',
)
layout = go.Layout(
    xaxis = dict(title = 'Artist Hotttnesss'),
    yaxis = dict(title = 'Artist Familiarity')
)

data = [trace]

# Plot and embed in ipython notebook!
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Artist_hotttnesss vs familiarity')

```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~shashankprabhakar/7.embed" height="525px" width="100%"></iframe>




```python
print("The Pearson's Coefficient ")
print(df['artist.hotttnesss'].corr(df['familiarity']))
```

    The Pearson's Coefficient 
    0.8111015325321547



```python
#Song Locations across the globe
from IPython.core.display import display, HTML
display(HTML('<iframe width="1050" height="600" scrolling="no" frameborder="no" src="https://fusiontables.google.com/embedviz?q=select+col14+from+1u481cSQDjs7WzcEDkqSEDTqw4hmgWRNgwFMWRDVb&amp;viz=MAP&amp;h=false&amp;lat=14.648669236670923&amp;lng=14.315151566960822&amp;t=3&amp;z=2&amp;l=col14&amp;y=4&amp;tmplt=6&amp;hml=TWO_COL_LAT_LNG"></iframe>'))
```


<iframe width="1050" height="600" scrolling="no" frameborder="no" src="https://fusiontables.google.com/embedviz?q=select+col14+from+1u481cSQDjs7WzcEDkqSEDTqw4hmgWRNgwFMWRDVb&amp;viz=MAP&amp;h=false&amp;lat=14.648669236670923&amp;lng=14.315151566960822&amp;t=3&amp;z=2&amp;l=col14&amp;y=4&amp;tmplt=6&amp;hml=TWO_COL_LAT_LNG"></iframe>



```python
#Plot of Number of songs vs years
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x = df['year']
yrs = []
for i in x:
    if i!=0:
        yrs.append(i)

data2 = [go.Histogram(x=yrs)]

layout2 = go.Layout(
    xaxis = dict(title = 'Year'),
    yaxis = dict(title = 'Number of Songs')
)
fig2 = go.Figure(data=data2, layout=layout2)
py.iplot(fig2, filename='Number of songs vs years')

```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~shashankprabhakar/9.embed" height="525px" width="100%"></iframe>




