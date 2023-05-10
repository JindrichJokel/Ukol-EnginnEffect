import matplotlib.pyplot as plt
import csv

class CheckResidual:
    def __init__(self, filename):
        self.filename = filename
        self.time = ""
        self.p_rgh = ""
        self.omega = ""
        self.k = ""
        self.ArrayTime = []
        self.ArrayP_rgh = []
        self.ArrayOmega = []
        self.ArrayK = []
        self.data = None

    def process_data(self):
        with open(self.filename, "r") as file:
            for line in file:
                if line.startswith("Time ="):
                    if self.p_rgh != "":
                        self.ArrayP_rgh.append(self.p_rgh)
                    self.time = float(line.split("=")[-1].strip())
                    self.ArrayTime.append(self.time)
                    self.p_rgh = ""
                    self.omega = ""
                    self.k = ""
                elif "Solving for p_rgh" in line:
                    self.p_rgh = float(line.split("Final residual = ")[-1].split(",")[0].strip())
                elif "Solving for omega" in line:
                    self.omega = float(line.split("Final residual = ")[-1].split(",")[0].strip())
                    self.ArrayOmega.append(self.omega)
                elif "Solving for k" in line:
                    self.k = float(line.split("Final residual = ")[-1].split(",")[0].strip())
                    self.ArrayK.append(self.k)
            self.ArrayP_rgh.append(self.p_rgh)
            self.data = zip(self.ArrayTime, self.ArrayP_rgh, self.ArrayOmega,self.ArrayK)

    def plot_data(self):
        if not self.data:
            self.process_data()
        fig, ax = plt.subplots()
        ax.plot(self.ArrayTime, self.ArrayP_rgh, label='p_rgh')
        ax.plot(self.ArrayTime, self.ArrayOmega, label='omega')
        ax.plot(self.ArrayTime, self.ArrayK,label='k')
        ax.set_xlabel('Time(x)')
        ax.set_ylabel('Final residual')
        ax.set_title('Time of final residual')      
        ax.legend()
        plt.show()

    def save_data(self, filename='data.csv'):
        if not self.data:
            self.process_data()
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'p_rgh', 'omega', 'k'])
            for row in self.data:
                writer.writerow(row)

# create an instance of CheckResidual with the filename 'log.txt'
data_analyzer = CheckResidual('log.txt')

# plot the data
data_analyzer.plot_data()

# save the data to a CSV file
data_analyzer.save_data()
