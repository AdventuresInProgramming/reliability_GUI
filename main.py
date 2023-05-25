from tkinter import messagebox
import reliability
import pandas as pd
from tkinter import *
import openpyxl
from reliability.Fitters import Fit_Weibull_2P
from reliability.Fitters import Fit_Weibull_3P
from reliability.Fitters import Fit_Lognormal_2P
from reliability.Fitters import Fit_Everything
import matplotlib.pyplot as plt
from reliability.Convert_data import xlsx_to_FR
from reliability.Repairable_systems import optimal_replacement_time
from reliability.Other_functions import crosshairs

#--------------- create weibull ----------#
def make_weibull_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    #writer = pd.ExcelWriter("C:\\Users\\User\\PycharmProjects\\gui_reliability\\output.xlsx")
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.save()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_weibull_3p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Weibull_3P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    #writer = pd.ExcelWriter("C:\\Users\\User\\PycharmProjects\\gui_reliability\\output.xlsx")
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.save()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_lognormal(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    #writer = pd.ExcelWriter("C:\\Users\\User\\PycharmProjects\\gui_reliability\\output.xlsx")
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.save()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_everything(failure_data, suspended_data):
    fit_wb_2 = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_wb_3 = Fit_Weibull_3P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_lognorm = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    log_likeihood= f"weibull 2P log likehood is {fit_wb_2.goodness_of_fit.iloc[1,1]} \n" \
                   f"weibull 3P log likehood is {fit_wb_3.goodness_of_fit.iloc[1,1]} \n" \
                   f"Log normal log likehood is {fit_lognorm.goodness_of_fit.iloc[1,1]}\n" \
                   f"the smaller the number, the more likely the distribution"

    messagebox.showinfo(title="Output", message=log_likeihood)

def extract_data(filename):
    data = xlsx_to_FR(path=filename)
    data_3 = data.failures
    data_right_3 = data.right_censored
    if variable.get() == "Weibull 2 P":
        make_weibull_2p(data_3, data_right_3)
    elif variable.get() == "Weibull 3 P":
        make_weibull_3p(data_3, data_right_3)
    elif variable.get() == "Log Normal":
        make_lognormal(data_3, data_right_3)
    else:
        make_everything(data_3, data_right_3)

def get_file():
    filename = file_location_entry.get()
    extract_data(filename)

def get_optimal_time():
    cmcost = float(optimal_main_CM.get())
    pmcost = float(optimal_main_PM.get())
    wb_alpha = float(optimal_main_WB_scale.get())
    wb_beta = float(optimal_main_WB_shape.get())
    optimal_replacement_time(cost_PM= pmcost, cost_CM=cmcost, weibull_alpha=wb_alpha, weibull_beta=wb_beta, q=0)
    plt.show()

def get_GOF():
    #to add if necessary. but not needed for maintenance work
    pass

#--------------- create GUI ----------#
window = Tk()
window.title("Reliability Interface")
window.config(padx=50, pady=50)
canvas = Canvas(height=500, width=200)

#Labels
file_loc_label = Label(text="File:")
file_loc_label.grid(row=1, column=0)
conf_bounds_label = Label(text="Confidence Bounds:")
conf_bounds_label.grid(row=2, column=0)

optimal_main_time = Label(text="Optimal PM vs CM")
optimal_main_time.grid(row=4,column=0)
optimal_main_CM = Label(text= "Corrective Mainteance Cost")
optimal_main_CM.grid(row=5, column=0)
optimal_main_PM = Label(text= "Preventive Mainteance Cost")
optimal_main_PM.grid(row=6, column=0)
optimal_main_WB_shape = Label(text= "Weibull Shape")
optimal_main_WB_shape.grid(row=7, column=0)
optimal_main_WB_scale = Label(text= "Weibull Scale")
optimal_main_WB_scale.grid(row=8, column=0)

file_output = Label(text="file output address")
file_output.grid(row=10, column=0 )
#Entries
file_location_entry = Entry(width=35)
file_location_entry.grid(row=1, column=1, columnspan=2)
file_location_entry.insert(0,"C:\\Users\\User\\PycharmProjects\\gui_reliability\\input.xlsx")
file_location_entry.focus()
conf_bounds_entry = Entry(width=35)
conf_bounds_entry.grid(row=2, column=1, columnspan=2)
conf_bounds_entry.insert(0,"0.95")
optimal_main_CM = Entry(width=35)
optimal_main_CM.grid(row=5,column=1,columnspan=2)
optimal_main_PM = Entry(width=35)
optimal_main_PM.grid(row=6,column=1,columnspan=2)
optimal_main_WB_shape = Entry(width=35)
optimal_main_WB_shape.grid(row=7,column=1,columnspan=2)
optimal_main_WB_scale = Entry(width=35)
optimal_main_WB_scale.grid(row=8,column=1,columnspan=2)

file_output_entry = Entry(width=35)
file_output_entry.grid(row=10, column=1, columnspan=2)
file_output_entry.insert(0,"C:\\Users\\User\\PycharmProjects\\gui_reliability\\output.xlsx")

# Buttons
generate_graph = Button(text="Generate Graph", command=get_file)
generate_graph.grid(row=3, column=2)

generate_optimal = Button(text="Generate Optimal Graph", command=get_optimal_time)
generate_optimal.grid(row=9, column=2)

#drop table
graph_options = [
"Weibull 2 P",
"Weibull 3 P",
"Log Normal",
"Test All"
]

variable = StringVar(window)
variable.set(graph_options[0]) # default value

w = OptionMenu(window, variable, *graph_options)
w.grid(row=3, column=1)

window.mainloop()
