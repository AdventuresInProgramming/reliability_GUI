# reliability_GUI
this creates a simple GUI for relaibility work

the underlying calculations are based on the work of the excellent reliability module

import your failure data in an exel format

column 1, row 1 = 'failure data'
column 1, rows 2 - x = enter your failure data in units of measurement
eg operating hours, FH, EOT, or other unit
do not include units!

column 2, row 2 = 'suspended data'
column 2, row 2 -x = enter your suspended data in units of measurement

the columns do not need to be equal in lenght. the script will handle it

name your file as 'input.xlsx'

drag and drop into the file location

click run on the top of the screen

after loading for some time, you should see a GUI window pop up

file location: default is input.xlsx
confidence bounds: how wide the range is for x% of the observations to come from there

drop down menu - select weibull 2P, weibull 3P, log normal or test all.

test all - samples the log likeihood to tell you which distribution is more likely to generate it

click on generate graph and the programme will calculate. the graph should show up in the window. cross hairs are enabled and mouse clicking will label the points. the parameters are shown in the graph for the shape and scale parameter.

the output is shown in the files tab under output.xlsx as a default. it contains the ranges of parameters as well as the likelihood figure if you are interested.

"""
