'''
Vamos a utilizar la libreria matplotlib para realizar nuestras graficas, y debemos instalarla de la siguiente manera

$ pip install matplotlib

Ahora la vamos a importar
'''

import matplotlib.pyplot as plot

def generate_bar_chart(labels, values):
    figure, ax = plot.subplots()
    ax.bar(labels, values)
    plot.show()

def generate_pie_chart(labels, values):
    figure, ax = plot.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plot.show()


if __name__ == '__main__':
    labels = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
    values = [10800, 8750, 11200, 15300, 9800, 12400]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)