import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart._title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
              {'value': 39593, 'label': 'Discription of httpie.'},
              {'value': 39212, 'label': 'Discription of django.'},
              {'value': 41630, 'label': 'Discription of flask.'},
             ]

chart.add('', plot_dicts)
chart.render_in_browser()
