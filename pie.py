from matplotlib import pyplot as plt
from matplotlib.transforms import Bbox
from datetime import datetime
import json
data = json.load(open("config.json"))
pie_color = data['pie_color']
def plot_pie(x):
    t = [1000-(x%1000),x%1000]
    fig = plt.figure(x,figsize = (9.19,9.19),dpi = 100)
    ax = fig.add_subplot(111)
    ax.pie(t, colors = pie_color, startangle=90, radius=1.5,center = (0.41,0.41))
    fig.tight_layout()
    fig.savefig(str(x)+'.jpg', format='jpg', facecolor = 'w',bbox_inches = Bbox([[-0.41,-0.41],[9.59,9.59]]))
    plt.close()
def get_time(x):
	yr = x//1000+2000
	permille = x%1000
	return (int(datetime(yr+1,1,1,0,0).timestamp())-int(datetime(yr,1,1,0,0).timestamp()))*permille//1000+int(datetime(yr,1,1,0,0).timestamp())
if __name__ == '__main__':
    i = int(input())
    plot_pie(i)
