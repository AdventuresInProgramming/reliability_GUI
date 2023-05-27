"""
this file describes the operations of main.py

The purpose is to create a simple Graphical User Interface for non-programmers to use the reliability library

https://reliability.readthedocs.io/en/latest/index.html

It helps MRO engineers perform the following:
1. One population analysis - regression testing of failure/success data for one population
2. Two population comparison - see if they are distinct populations
3. Optimal Replacement calculations to balance Corrective and Preventive Maintenance

General Instructions for using:

Input your reliability data as excel workbooks, xlsx

The data should be in the FR format:

    column 1, row 1 = 'failure data'
    column 1, rows 2 - x = enter your failure data in units of measurement
    column 2, row 2 = 'suspended data'
    column 2, row 2 -x = enter your suspended data in units of measurement

Units of measurement are operating hours or whatever custom unit you use
Do not include the unit, the entry must be in numerical format (float or int)

The columns do not need to be equal in length. the script will handle it

Full details at:
https://reliability.readthedocs.io/en/latest/Converting%20data%20between%20different%20formats.html

Extra Info concerning Operations:

1. One population analysis
    Select the distribution to test from the dropdown menu
    If not sure, test all samples the loglikelihood and returns a popup box.
    You can view the probabilities from there and see which to use first

    Confidence bounds: how wide the range is for x% of the observations to come from there

    Force Parameter is applicable to weibull 2P, normal 2P and lognormal 2P, should you wish to force beta or sigma

    Click on generate graph and the programme will calculate. the graph should show up in the window.
    Cross hairs are enabled and mouse clicking will label the points.
    The parameters are shown in the graph for the shape and scale parameter.
    Saving the graphs can be done from the pop-up graph window

    The output is shown in the files tab under output.xlsx as a default.
    it contains the ranges of parameters as well as the likelihood figure if you are interested.

2. Two Population Comparison
    Select the distributions to use from the dropdown menu
    Click on generate graph and the programme will calculate. the graph should show up in the window.
    Saving the graphs can be done from the pop-up graph window

3. Optimal Replacement
    insert the parameters. no excel file is needed

"""
