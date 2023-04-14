import json
import squarify 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Datahandler:
  def __init__(self, input_json):
    self.input_json = input_json
    self.data = ""

  def loader(self):
    with open(self.input_json, "r") as read_file:
      self.data = json.load(read_file)
    return self.data

def currency_volume_graph(data):
  labels = [el['name'] for el in data]
  sizes = [el['volume'] for el in data]
  colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

  plt.figure(figsize=(12,8), dpi= 80)
  squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8, pad = 2)
  plt.title('Treemap of cryptocurrency volume')
  plt.axis('off')
  plt.show()

def currency_price_graph(data):

  fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
  ax.vlines(x=[el['name'] for el in data], ymin=0, ymax=[el['price'] for el in data], color='firebrick', alpha=0.7, linewidth=20)

  ax.set_title('Bar Chart for Cryptocurrency price', fontdict={'size':22})
  ax.set(ylabel='Mean price per day', ylim=(0, 30))
  plt.xticks([el['name'] for el in data], rotation=60, horizontalalignment='right', fontsize=12)

  p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
  p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
  fig.add_artist(p1)
  fig.add_artist(p2)
  plt.show()
