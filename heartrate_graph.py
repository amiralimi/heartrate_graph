import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv


# number of items returned in each iteration by the generator function.
ITEMS_IN_EACH_ITR = 5

class Scope:
    def __init__(self, ax, maxt=10, dt=0.02):
        self.ax = ax
        self.maxt = maxt
        self.dt = dt

        # max number of points in the graph
        self.MAX = int(maxt/dt)
        # initial data for the lists
        self.tdata = [10 * x/self.MAX for x in range(self.MAX)]
        self.ydata = [0.5 for x in range(self.MAX)]

        # start and end index for making the gap between the new data and old data
        self.start = 0
        self.end = 50

    def update(self, y):
        # add new data in the list.
        for item in y:
            self.ydata[self.start] = item
            self.start += 1
            self.end += 1
            self.start %= self.MAX
            self.end %= self.MAX

        # clear the canvas to draw the new data
        self.ax.clear()
        self.ax.set_ylim(0, 1)
        self.ax.set_xlim(0, self.maxt)

        # create plots
        if self.start < self.end:
            self.ax.plot(self.tdata[:self.start], self.ydata[:self.start], 'b')
            self.ax.plot(self.tdata[self.end:], self.ydata[self.end:], 'b')
        else:
            self.ax.plot(self.tdata[self.end:self.start],
                self.ydata[self.end:self.start], 'b')

    def show(self):
        ani = animation.FuncAnimation(fig, scope.update, emitter,interval=50)
        plt.show()


# a generator function that returns a list of new data.
def emitter():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        l = []
        for row in csv_reader:
            if len(l) != ITEMS_IN_EACH_ITR:
                l.append(int(row[0])/900)
            else:
                yield l
                l.clear()


if __name__ == '__main__':
    fig, ax = plt.subplots()
    scope = Scope(ax)
    scope.show()
