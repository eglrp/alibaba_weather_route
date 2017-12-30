import argparse
import time
from datetime import datetime
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from config.configuration import Configuration
from tools.utils import HMS, configurationPATH
from tools.visualisation import plot_real_wind, plt_forecast_wind_train, plt_forecast_wind_test, plot_all_wind, plt_forecast_wind_test_multiprocessing,plt_forecast_wind_train_multiprocessing
from tools.A_star_alibaba import A_star_2d_hourly_update_route, A_star_search_3D, A_star_search_3D_multiprocessing
from tools.simpleSub import submit_phase
from tools.evaluation import evaluation, evaluation_plot
from tools.RL_alibaba import reinforcement_learning_solution
from FCN.FCN import fully_convolutional_wind_pred


def process(cf):
    if cf.plot_real_wind:
        print('plot_real_wind')
        plot_real_wind(cf)
    if cf.plt_forecast_wind_train:
        print('plot_forecast_wind_train')
        plt_forecast_wind_train(cf)
    if cf.plt_forecast_wind_train_multiprocessing:
        print('plt_forecast_wind_train_multiprocessing')
        plt_forecast_wind_train_multiprocessing(cf)
    if cf.plt_forecast_wind_test:
        print('plt_forecast_wind_test')
        plt_forecast_wind_test(cf)
    if cf.plt_forecast_wind_test_multiprocessing:
        print('plt_forecast_wind_test_multiprocessing')
        plt_forecast_wind_test_multiprocessing(cf)
    if cf.plot_all_wind:
        print('Draw weather')
        plot_all_wind(cf)

    if cf.A_star_search_2D:
        print('A_star_search_2D')
        A_star_2d_hourly_update_route(cf)

    # This is one of the core algorithm
    if cf.A_star_search_3D:
        print('A_star_search_3D')
        A_star_search_3D(cf)

    if cf.A_star_search_3D_multiprocessing:
        print('A_star_search_3D_multiprocessing')
        A_star_search_3D_multiprocessing(cf)

    if cf.reinforcement_learning_solution:
        print('reinforcement_learning_solution')
        reinforcement_learning_solution(cf)

    if cf.fully_convolutional_wind_pred:
        print('fully_convolutional_wind_pred')
        fully_convolutional_wind_pred(cf)

    if cf.submission_dummy:
        print("submission")
        submit_phase(cf)

    if cf.evaluation:
        print('evaluation')
        total_penalty = evaluation(cf, cf.csv_for_evaluation)
        print(int(np.sum(np.sum(total_penalty))))
        print(total_penalty.astype('int'))
        print(np.sum(total_penalty.astype('int') == 1440))

    if cf.evaluation_plot:
        print('evaluation_plot')
        evaluation_plot(cf)



def main():
    # Get parameters from arguments
    parser = argparse.ArgumentParser(description='Model training')
    parser.add_argument('-c', '--config_path', type=str, default='/home/stevenwudi/PycharmProjects/alibaba_weather_route/config/diwu.py', help='Configuration file')

    arguments = parser.parse_args()
    assert arguments.config_path is not None, 'Please provide a path using -c config/pathname in the command line'
    print('\n > Start Time:')
    print('   ' + datetime.now().strftime('%a, %d %b %Y-%m-%d %H:%M:%S'))
    start_time = time.time()
    # Define the user paths

    # Load configuration files
    configuration = Configuration(arguments.config_path)
    cf = configuration.load()
    configurationPATH(cf)

    # Train /test/predict with the network, depending on the configuration
    process(cf)

    # End Time
    end_time = time.time()
    print('\n > End Time:')
    print('   ' + datetime.now().strftime('%a, %d %b %Y-%m-%d %H:%M:%S'))
    print('\n   ET: ' + HMS(end_time - start_time))


if __name__ == "__main__":
    main()
