# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:12:26 2019

@author: Brodie
"""


# Define functions
def FirstDerApp(t, dx, an_sol):
    """
    This function uses the first derivative approximation methods on
    the center point:
        First Derivative Forward: f'(x_i) = (f(x_i+1) - f(x_i)) / dx
        First Derivative Backward: f'(x_i) = (f(x_i) - f(x_i-1)) / dx
        First Derivative Centered: f'(x_i) = (f(x_i+1) - f(x_i-1)) / 2dx
        Higher Order Forward: f'(x_i) = (-3 * f'(x_i) + 4 * f(x_i+1) -
                                        f(x_i+2)) / 2 * dx
        Higher Order Backward: f'(x_i) = (3 * f'(x_i) - 4 * f(x_i-1) +
                                         f(x_i-2)) / 2 * dx
        Higher Order Centered: f'(x_i) = (f(x_i+1) - 2 * f(x_i) +
                                         f(x_i-1)) / 2 * dx
    Takes:
        t: List of temperature measurements at different grid points
        dx: delta x beteween them
        an_sol: the analytic solution of this function
    Returns:
        fdf: the first derivative of the center point using the forward
             approximation method defined above
        fdb: the first derivative of the center point using the backward
             approximation method defined above
        fdc: the first derivative of the center point using the center
             approximation method defined above
        t_err: the truncation error
    Note: If there is an even number of observations, it will use the one to
          the right of center (i + 1)
    """
    if len(t) % 2 != 0:  # checking if there is an odd number of observations
        center = round(len(t)/2)
    else:
        print("I don't know how to do an even number of observations yet so,\
              I am just using the next observation")
        center = int(len(t)/2)
    fdf = (t[center + 1] - t[center]) / dx
    fdb = (t[center] - t[center - 1]) / dx
    fdc = (t[center + 1] - t[center - 1]) / (2 * dx)
    hof = ((-3 * t[center]) + (4 * t[center + 1]) - t[center + 2]) / (2 * dx)
    hob = ((3 * t[center]) - (4 * t[center - 1]) + t[center - 2]) / (2 * dx)
    hoc = (1/3) * ((4 * ((t[center + 1] - t[center - 1]) /
                    ((50 + dx) - (50 - dx)))) -
                   ((t[center + 2] - t[center - 2]) /
                   ((50 + 2 * dx) - (50 - 2 * dx))))
    t_err_fdf = fdf - an_sol
    t_err_fdb = fdb - an_sol
    t_err_fdc = fdc - an_sol
    t_err_hof = hof - an_sol
    t_err_hob = hob - an_sol
    t_err_hoc = hoc - an_sol
    return fdf, fdb, fdc, \
        hof, hob, hoc, \
        t_err_fdf, t_err_fdb, t_err_fdc, \
        t_err_hof, t_err_hob, t_err_hoc


def SecondDerApp(t, dx):
    """
    # TODO: Needs doc string
    """
    if len(t) % 2 != 0:  # checking if there is an odd number of observations
        center = round(len(t)/2)
    else:
        print("I don't know how to do an even number of observations yet so,\
              I am just using the next observation")
        center = int(len(t)/2)
    sec_der = (t[center + 1] - (2 * t[center]) + t[center - 1]) / (dx**2)
    return sec_der


def FirstThreePrinter(dict_of_obs, dict_of_errors_and_dx):
    # Call the function three times with different variables
    row_format = "{:>17}" * 4
    for cs in dict_of_obs:
        print('\n')
        fst_f, fst_b, fst_c, fst_hof, fst_hob, fst_hoc,\
            fst_f_err, fst_b_err, fst_c_err, fst_hof_err, fst_hob_err, \
            fst_hoc_err = FirstDerApp(dict_of_obs[cs],
                                      dict_of_errors_and_dx[cs][0],
                                      dict_of_errors_and_dx[cs][1])
        row = ['Technique | ', cs + ' (∆x = ' +
               str(dict_of_errors_and_dx[cs][0]) + ')|',
               ' TruncationError']
        print(row_format.format("", *row))
        row = ['f\' fwrd | ', str(round(fst_f, 4)) + ' |',
               str(round(fst_f_err, 4)) + '|']
        print(row_format.format("", *row))
        row = ['f\' bwrd | ', str(round(fst_b, 4)) + ' |',
               str(round(fst_b_err, 4)) + '|']
        print(row_format.format("", *row))
        row = ['f\' cntr | ', str(round(fst_c, 4)) + ' |',
               str(round(fst_c_err, 4)) + '|']
        print(row_format.format("", *row))
        row = ['f\' hof | ', str(round(fst_hof, 4)) + ' |',
               str(round(fst_hof_err, 4)) + '|']
        print(row_format.format("", *row))
        row = ['f\' hob | ', str(round(fst_hob, 4)) + ' |',
               str(round(fst_hob_err, 4)) + '|']
        print(row_format.format("", *row))
        row = ['f\' hoc | ', str(round(fst_hoc, 4)) + ' |',
               str(round(fst_hoc_err, 4)) + '|']
        print(row_format.format("", *row))


def LastPrinter(dict_of_obs, dict_of_errors_and_dx):
    print('\n')
    row_format = "{:>17}" * 4
    row = ['f\'\' @: | ', 'Case 1 |',
               ' TruncationError']
    print(row_format.format("", *row))
    for cs in dict_of_obs:
        sec_deriv = SecondDerApp(dict_of_obs[cs],
                                 dict_of_errors_and_dx[cs][0])
        row = ['∆x = ' + str(dict_of_errors_and_dx[cs][0]) + ' | ',
               str(round(sec_deriv, 4)) + ' |',
               str(round(sec_deriv + 0.0118029, 4)) + '|']
        print(row_format.format("", *row))


# These are the numbers from Lab 2
obs = {'Case 1': [16.5224, 27.3463, 42.6537, 53.4776, 53.4776],
       'Case 2': [27.3463, 35.0, 42.6537, 49.1421, 53.4776],
       'Case 3': [35.0, 38.9018, 42.6537, 46.1114, 49.1421]}
er_dx = {'Case 1': [20, 0.7256132],
         'Case 2': [10, 0.7256132],  # Here was my mistake
         'Case 3': [5, 0.7256132]}
FirstThreePrinter(obs, er_dx)
LastPrinter(obs, er_dx)
