import matplotlib.pyplot as plt

class DynamicTermination:
    def __init__(self, filename):
        self.column1 = []
        self.column2 = []
        self.filename = filename

    def read_columns(self):
        with open(self.filename, 'r') as f:
            for _ in range(3):
                next(f)

            for line in f:
                values = line.strip().split()
                self.column1.append(float(values[0]))
                self.column2.append(float(values[1]))

                if self.stopping_condition_met():
                    print("Stopping condition met at line", len(self.column2))
                    break

    def stopping_condition_met(self):
        if len(self.column2) > 20000 and all(val < 0.5 for val in self.column2[-20000:]) and max(self.column2[-20000:]) - min(self.column2[-20000:]) < 0.1:
            return True
        else:
            return False

    def plot_columns(self):
        plt.plot(self.column1, self.column2)
        plt.xlabel('Column 1')
        plt.ylabel('Column 2')
        plt.show()

# create an instance of DynamicTermination with the filename 'alpha.txt'
column_plotter = DynamicTermination('alpha.txt')
# process the data
column_plotter.read_columns()
# plot the data
column_plotter.plot_columns()