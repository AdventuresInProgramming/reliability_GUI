from tkinter import messagebox
import reliability
import pandas as pd
from tkinter import *
import openpyxl
from reliability.Fitters import Fit_Weibull_2P
from reliability.Fitters import Fit_Weibull_3P
from reliability.Fitters import Fit_Lognormal_2P
from reliability.Fitters import Fit_Lognormal_3P
from reliability.Fitters import Fit_Exponential_1P
from reliability.Fitters import Fit_Gamma_2P
from reliability.Fitters import Fit_Gamma_3P
from reliability.Fitters import Fit_Normal_2P
from reliability.Fitters import Fit_Gumbel_2P
from reliability.Fitters import Fit_Exponential_2P
from reliability.Fitters import Fit_Loglogistic_2P
from reliability.Fitters import Fit_Loglogistic_3P
from reliability.Fitters import Fit_Everything
import matplotlib.pyplot as plt
from reliability.Convert_data import xlsx_to_FR
from reliability.Repairable_systems import optimal_replacement_time
from reliability.Other_functions import crosshairs
from reliability.Reliability_testing import likelihood_plot

#--------------- create weibull ----------#
def make_weibull_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    if variable_f_1.get() == "FORCE":
        force_parameter = float(force_para_entry.get())
        fit = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, force_beta = force_parameter,print_results=False)
    else:
        fit = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, CI=conf_bounds, print_results=False)
    #fit = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, CI=conf_bounds, print_results=False)
    #writer = pd.ExcelWriter("C:\\Users\\User\\PycharmProjects\\gui_reliability\\output.xlsx")
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    #writer.save()
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_weibull_3p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Weibull_3P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    #writer.save()
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_lognormal(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    if variable_f_1.get() == "FORCE":
        force_parameter = float(force_para_entry.get())
        fit = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, force_sigma = force_parameter,print_results=False)
    else:
        fit = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, CI=conf_bounds, print_results=False)
    #fit = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    #writer.save()
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_exponential_1p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Exponential_1P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_gamma_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Gamma_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_normal_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    #fit = Fit_Normal_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    if variable_f_1.get() == "FORCE":
        force_parameter = float(force_para_entry.get())
        fit = Fit_Normal_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, force_sigma = force_parameter,print_results=False)
    else:
        fit = Fit_Normal_2P(failures=failure_data, right_censored=suspended_data, CI=conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_gumbel_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Gumbel_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_exponential_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Exponential_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_gamma_3p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Gamma_3P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_lognormal_3p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Lognormal_3P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_loglogistic_2p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Loglogistic_2P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_loglogistic_3p(failure_data, suspended_data):
    plt.subplot(111)
    conf_bounds = float(conf_bounds_entry.get())
    fit = Fit_Loglogistic_3P(failures=failure_data, right_censored=suspended_data, CI = conf_bounds, print_results=False)
    writer = pd.ExcelWriter(file_output_entry.get())
    fit.results.to_excel(writer,"Distribution Parameters")
    fit.goodness_of_fit.to_excel(writer,"goodness of fit")
    writer.close()
    crosshairs(xlabel='t', ylabel='%tage')
    plt.legend()
    plt.show()

def make_everything(failure_data, suspended_data):
    fit_wb_2 = Fit_Weibull_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_wb_3 = Fit_Weibull_3P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_lognorm_2 = Fit_Lognormal_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_lognorm_3 = Fit_Lognormal_3P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_exp_1 = Fit_Exponential_1P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_exp_2 = Fit_Exponential_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_gamma_2 = Fit_Gamma_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_gamma_3 = Fit_Gamma_3P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_loglog_2 = Fit_Loglogistic_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_loglog_3 = Fit_Loglogistic_3P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_norm = Fit_Normal_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    fit_gumbel = Fit_Gumbel_2P(failures=failure_data, right_censored=suspended_data, print_results=False)
    log_likeihood= f"weibull 2P log likelihood is {fit_wb_2.goodness_of_fit.iloc[1,1]} \n" \
                   f"weibull 3P log likelihood is {fit_wb_3.goodness_of_fit.iloc[1,1]} \n" \
                   f"Log normal 2P log likelihood is {fit_lognorm_2.goodness_of_fit.iloc[1,1]}\n" \
                   f"Log normal 3P log likelihood is {fit_lognorm_3.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Exp 1P log likelihood is {fit_exp_1.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Exp 2P log likelihood is {fit_exp_2.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Gamma 2P log likelihood is {fit_gamma_2.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Gamma 3P log likelihood is {fit_gamma_3.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Log logistics 2P log likelihood is {fit_loglog_2.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Log logistics 3P log likelihood is {fit_loglog_3.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Normal 2P log likelihood is {fit_norm.goodness_of_fit.iloc[1, 1]}\n" \
                   f"Gumbel 2P log likelihood is {fit_gumbel.goodness_of_fit.iloc[1, 1]}\n" \
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
    elif variable.get() == "Log Normal 2 P":
        make_lognormal(data_3, data_right_3)
    elif variable.get() == "Exponential 1 P":
        make_exponential_1p(data_3, data_right_3)
    elif variable.get() == "Gamma 2 P":
        make_gamma_2p(data_3, data_right_3)
    elif variable.get() == "Normal 2 P":
        make_normal_2p(data_3, data_right_3)
    elif variable.get() == "Gumbel 2 P":
        make_gumbel_2p(data_3, data_right_3)
    elif variable.get() == "Exponential 2 P":
        make_exponential_2p(data_3, data_right_3)
    elif variable.get() == "Gamma 3 P":
        make_gamma_3p(data_3, data_right_3)
    elif variable.get() == "Log Normal 3 P":
        make_lognormal_3p(data_3, data_right_3)
    elif variable.get() == "Log Logistic 2 P":
        make_loglogistic_2p(data_3, data_right_3)
    elif variable.get() == "Log Logistic 3 P":
        make_loglogistic_3p(data_3, data_right_3)
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

def get_2_pop_likeli():
    filename_1 = file_2p1_location_entry.get()
    filename_2 = file_2p2_location_entry.get()
    data_1 = xlsx_to_FR(path=filename_1)
    data_2 = xlsx_to_FR(path=filename_2)
    data_1a = data_1.failures
    data_1b = data_1.right_censored
    data_2a = data_2.failures
    data_2b = data_2.right_censored
    dist_to_use = variable_2.get()
    likelihood_plot(distribution=dist_to_use , failures=data_1a, right_censored=data_1b, CI=[0.9, 0.95])
    likelihood_plot(distribution=dist_to_use , failures=data_2a, right_censored=data_2b, CI=[0.9, 0.95])
    plt.show()





#----------- pop up boxes ----#

def popup_help():
   top= Toplevel(window)
   top.geometry("750x250")
   top.title("Help for Input")
   Label(top,font=24,justify='left', text=" Import your failure data in an exel workbook(xlsx), FR format:"
                   "\n column 1, row 1 = 'failure data'"
                   "\n column 1, rows 2 - x = enter your failure data in units of measurement"
                   "\n column 2, row 2 = 'suspended data'"
                   "\n column 2, row 2 -x = enter your suspended data in units of measurement"
                   "\n name your file as 'input.xlsx'"
                   "\n copy the filepath and paste it in the entry box").place(x=0, y=0)

def popup_help_2pop():
    top = Toplevel(window)
    top.geometry("750x250")
    top.title("Help for Input")
    Label(top, font=24,justify='left',text=" This test requires the two populations in different excel files(xlsx)."
                    "\n For each population, Import your failure data in the following format (FR):"
                    "\n column 1, row 1 = 'failure data'"
                    "\n column 1, rows 2 - x = enter your failure data in units of measurement"
                    "\n column 2, row 2 = 'suspended data'"
                    "\n column 2, row 2 -x = enter your suspended data in units of measurement"
                    "\n name your files as 'input_1.xlsx' and 'input_2.xlsx'"
                    "\n copy the filepath and paste it in the respective entry boxes").place(x=0, y=0)

def popup_help_optimal():
    top = Toplevel(window)
    top.geometry("750x250")
    top.title("Help for Input")
    Label(top, font=24,justify='left',text=" This test solves for the optimal replacement regime"
                    "\n Insert Corrective Maintenance Cost and Preventive Maintenance Costs"
                    "\n The Weibull Shape parameter is beta"
                    "\n The Weibull Scale parameter is eta"
                    "\n Press Generate Button to execute").place(x=0, y=0)

def popup_help_info():
    top = Toplevel(window)
    top.geometry("750x250")
    top.title("Help for Input")
    Label(top, font=24,justify='left',text=" This GUI serves to simplify the reliability library for the non pythoners"
                    "\n In general, copy your input file location (xlsx) into the file input path"
                    "\n After generation, the output data is available at the output path specified"
                    "\n the respective graphs will generate and can be saved from their windows"
                    "\n Find out more on this wonderful piece of work at:"
                    "\n https://reliability.readthedocs.io/en/latest/Quickstart%20for%20reliability.html"
                    "\n Required Libraries: Tkinter, Reliability, Pandas, Matplotlib"
                    "\n Accurate as of 2023-05").place(x=0, y=0)

#--------------- create GUI ----------#
window = Tk()
window.title("Reliability Interface")
window.config(padx=50, pady=50)
canvas = Canvas(height=1500, width=1000)

section_1_row = 1
section_2_row = 9
section_3_row = 14

col_1_width = 25
col_2_width = 40
#Labels
header_1_label = Label(text='One Population Analysis',font=24)
header_1_label.grid(row=section_1_row, column=1)
file_loc_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="File Input Path:")
file_loc_label.grid(row=section_1_row+1, column=0)
conf_bounds_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="Confidence Bounds:")
conf_bounds_label.grid(row=section_1_row+2, column=0)
force_para_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="Force Parameter:")
force_para_label.grid(row=section_1_row+3, column=0)
file_output = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="File Output Path:")
file_output.grid(row=section_1_row+4, column=0 )
dropdown_1_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="Choose Distribution:")
dropdown_1_label.grid(row=section_1_row+5, column=0 )
spacer_1_label = Label(text="")
spacer_1_label.grid(row=section_1_row+6, column=0 )

header_3_label = Label(text='Two Population Comparison',font=24)
header_3_label.grid(row=section_2_row, column=1)
file_2p1_loc_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="File Pop 1 Input Path:")
file_2p1_loc_label.grid(row=section_2_row+1, column=0)
file_2p2_loc_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="File Pop 2 Input Path:")
file_2p2_loc_label.grid(row=section_2_row+2, column=0)
dropdown_2_label = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text="Choose Distribution:")
dropdown_2_label.grid(row=section_2_row+3, column=0 )
spacer_3_label = Label(text="")
spacer_3_label.grid(row=section_2_row+4, column=0 )


header_2_label = Label(text='Optimal Replacement Regime',font=24)
header_2_label.grid(row=section_3_row, column=1)
optimal_main_CM = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text= "Corrective Mainteance Cost:")
optimal_main_CM.grid(row=section_3_row+1, column=0)
optimal_main_PM = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text= "Preventive Mainteance Cost:")
optimal_main_PM.grid(row=section_3_row+2, column=0)
optimal_main_WB_shape = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text= "Weibull Shape:")
optimal_main_WB_shape.grid(row=section_3_row+3, column=0)
optimal_main_WB_scale = Label(borderwidth=1, relief="solid",width=col_1_width,anchor='w',text= "Weibull Scale:")
optimal_main_WB_scale.grid(row=section_3_row+4, column=0)

#Entries
file_location_entry = Entry(width=col_2_width)
file_location_entry.grid(row=section_1_row+1, column=1, columnspan=2,sticky = "w")
file_location_entry.insert(0,"Insert Path Here")
file_location_entry.focus()
conf_bounds_entry = Entry(width=col_2_width)
conf_bounds_entry.grid(row=section_1_row+2, column=1, columnspan=2,sticky = "w")
conf_bounds_entry.insert(0,"0.95")
force_para_entry = Entry(width=col_2_width)
force_para_entry.grid(row=section_1_row+3, column=1, columnspan=2,sticky = "w")
force_para_entry.insert(0,"1")
file_output_entry = Entry(width=col_2_width)
file_output_entry.grid(row=section_1_row+4, column=1, columnspan=2,sticky = "w")
file_output_entry.insert(0,"Insert Path Here")

optimal_main_CM = Entry(width=col_2_width)
optimal_main_CM.grid(row=section_3_row+1,column=1,columnspan=2,sticky = "w")
optimal_main_PM = Entry(width=col_2_width)
optimal_main_PM.grid(row=section_3_row+2,column=1,columnspan=2,sticky = "w")
optimal_main_WB_shape = Entry(width=col_2_width)
optimal_main_WB_shape.grid(row=section_3_row+3,column=1,columnspan=2,sticky = "w")
optimal_main_WB_scale = Entry(width=col_2_width)
optimal_main_WB_scale.grid(row=section_3_row+4,column=1,columnspan=2,sticky = "w")

file_2p1_location_entry = Entry(width=col_2_width)
file_2p1_location_entry.grid(row=section_2_row+1, column=1, columnspan=2,sticky = "w")
file_2p1_location_entry.insert(0,"Insert Path Here")

file_2p2_location_entry = Entry(width=col_2_width)
file_2p2_location_entry.grid(row=section_2_row+2, column=1, columnspan=2,sticky = "w")
file_2p2_location_entry.insert(0,"Insert Path Here")


# Buttons
generate_graph = Button(text="Generate Graph", command=get_file)
generate_graph.grid(row=section_1_row+5, column=3,sticky = "w")
help_1_button = Button(window, text= "Help Me!", command= popup_help)
help_1_button.grid(row=section_1_row+1, column =3,sticky = "w")


generate_2p = Button(window, text= "Generate 2 Pop Graph", command=get_2_pop_likeli)
generate_2p.grid(row=section_2_row+3, column =3,sticky = "w")
help_2_button = Button(window, text= "Help Me!", command= popup_help_2pop)
help_2_button.grid(row=section_2_row+1, column =3,sticky = "w")

generate_optimal = Button(text="Generate Optimal Graph", command=get_optimal_time)
generate_optimal.grid(row=section_3_row+6, column=3,sticky = "w")
help_3_button = Button(window, text= "Help Me!", command= popup_help_optimal)
help_3_button.grid(row=section_3_row+1, column =3,sticky = "w")

help_0_button = Button(window, text= "Whats All This?!", command=popup_help_info)
help_0_button.grid(row=1, column =4,sticky = "w")


#drop table
graph_options = [
"Weibull 2 P",
"Weibull 3 P",
"Log Normal 2 P",
"Log Normal 3 P",
"Gamma 2 P",
"Gamma 3 P",
"Normal 2 P",
"Gumbel 2 P",
"Exponential 1 P",
"Exponential 2 P",
"Log Logistic 2 P",
"Log Logistic 3 P",
"Test All"
]

variable = StringVar(window)
variable.set(graph_options[0]) # default value

w = OptionMenu(window, variable, *graph_options)
w.grid(row=section_1_row+5, column=1,sticky = "w")

graph_options_2p = [
"Weibull",
"Lognormal",
"Loglogistic",
"Gamma",
"Normal",
"Gumbel"
]

variable_2 = StringVar(window)
variable_2.set(graph_options_2p[0]) # default value

w_2 = OptionMenu(window, variable_2, *graph_options_2p)
w_2.grid(row=section_2_row+3, column=1,sticky = "w")

force_1_options = [
"NO FORCE",
"FORCE"
]

variable_f_1 = StringVar(window)
variable_f_1.set(force_1_options[0]) # default value

w_f_1 = OptionMenu(window, variable_f_1, *force_1_options)
w_f_1.grid(row=section_1_row+3, column=3,sticky = "w")



window.mainloop()