savepath                    = '/home/wzn/PycharmProjects/alibaba_weather_route/Experiments'
dataroot_dir                = '/media/samsumg_1tb/Alibaba_tianchi_RL/downloaded_data/'
fig_save_path               = '/home/wzn/PycharmProjects/alibaba_weather_route/Figures/Figure_post_12_05'
fig_save_train_path         = '/home/wzn/PycharmProjects/alibaba_weather_route/Figures/train_models_post_12_05'
fig_save_test_path          = '/home/wzn/PycharmProjects/alibaba_weather_route/Figures/test_models_post_12_05'
wind_save_path              = '/media/samsumg_1tb/Alibaba_tianchi_RL/wind_numpy_12_05_multiprocessing'

TrainRealFile               = 'In_situMeasurementforTraining_201712.csv'
TrainForecastFile           = 'ForecastDataforTraining_201712.csv'
TestForecastFile            = 'ForecastDataforTesting_201712.csv'

########################################################################################################################
plot_real_wind              = False
plt_forecast_wind_train     = False
plt_forecast_wind_test      = False
plt_forecast_wind_train_multiprocessing = False
plt_forecast_wind_test_multiprocessing = False
plot_all_wind               = False
plot_train_model            = False
plot_test_model             = False
model_unique                = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hour_unique                 = (3, 20)
# submission
submission_dummy            = False
add_day                     = 1 #[1| 6]
submission_path             = '/home/wzn/PycharmProjects/alibaba_weather_route/Submissions'
num_threads                 = 12

########################################################################################################################
# A star search
A_star_search_2D            = False
A_star_search_3D            = False
A_star_search_3D_multiprocessing = False
A_star_search_3D_multiprocessing_multicost = True
search_method               = 'a_star_search_3D'  #search methods ['a_star_search_3D','dijkstra']
model_number                = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grid_world_shape            = (548, 421)
time_length                 = 30 * 18  # total number of unit time (2 min is a unit time). We can fly maximum 18 hours which is 18 *30 unit time
model_description           = search_method  #['A_star_search_3D_risky', 'A_star_search_3D_conservative']
hourly_travel_distance      = 30

# important parameters
day_list                    = [3]  # train [1, 2, 3, 4, 5]  # test [6, 7, 8, 9, 10]
goal_city_list              = [1, 2, 3, 4, 5, 7, 9, 10]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
risky                       = True   # this flag will set the path weight to 1 to let A star choose the most efficient(risky) path
wall_wind                   = 15    # Set this lower will also reduce the risk!
risky_coeff                 = 15.  # This will only take effect is risky is set to False
wind_exp                    = False
wind_exp_mean               = 5
wind_exp_std                = 5
use_real_weather            = False
real_hour                   = 3


colormap                    = 'jet'  #['hot', 'jet']
#colors                     = ['red', 'magenta', 'cyan', 'yellow', 'green', 'blue']
colors                      = ['red', 'white']
wind_penalty_coeff          = 1
strong_wind_penalty_coeff   = 24*60  # this ensure that the wind hard threshold, we will not trespass the wind wall unless not viable route was found.

# evaluation
debug_draw                  = False
evaluation_days             = [3]  # [1, 2, 3, 4, 5]
evaluation_goal_cities      = [1, 2, 3, 4, 5, 7, 9, 10]  #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evaluation                  = False
collect_csv_for_submission_fraction = False
csv_for_evaluation          = '/home/wzn/PycharmProjects/alibaba_weather_route/Submissions/Train_a_star_search_3D_risky_wall_wind_15_model_number_[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].csv'

# evalutation plot
evaluation_plot             = False  # a flag for visualising predicted route
eval_day                    = [3]
eval_city                   = [9]

########################################################################################################################
# reinforcement_learning solution
reinforcement_learning_solution = False
reinforcement_learning_solution_multiprocessing = False
num_threads                     = 12
return_to_start                 = True
strong_wind_return              = True    # will go back to the previous state
include_all                     = False     # A flag indicating include all other A star heuristics
reward_goal                     = 1e5
reward_move                     = 0.0
reward_obstacle                 = -1e5

# Dyna model hyper
maxSteps                        = time_length  # Maze maximum steps
random_state                    = 0
planningSteps                   = time_length     # planning steps for Dyna model
alpha                           = 1      # Learning step size
gamma                           = 0.99
theta                           = 10
epsilon                         = 1.0 / time_length
qLearning                       = False  # flag for qLearning
expected                        = True  # flag for expected Sarsa
priority                        = True   # flag for prioritized sweeping
plus                            = True   # Dyna Plus algorithm
temp_model                      = 1  # a flag saying the temporary model
optimal_length_relax            = 1.5
heuristic                       = False
increase_epsilon                = 1.5  # for every maxSteps fail to reach the goal, we increase the epilson

########################################################################################################################
## FCN
fully_convolutional_wind_pred   = False
go_to_all_dir                   = None
#go_to_all_dir                   = '/home/stevenwudi/PycharmProjects/alibaba_weather_route/Experiments/go_to_all.npy'
a_star_loop                     = time_length
train_model                     = True
valid_model                     = True
collect_train_valid_mse_iou     = False
model_name                      = 'segnet_basic'  # Model to use ['fcn8' | 'lenet' | 'alexNet' | 'vgg16' |  'vgg19' | 'resnet50' | 'InceptionV3']
train_model_path                = '/home/wzn/PycharmProjects/alibaba_weather_route/Experiments/FCN_segnet_basic_____2018-01-01-14-25-58/epoch_470_mMSE:.12.057328mIOU:.0.499915_net.pth'
learning_rate                   = 1e-5
n_epochs                        = 1000
valid_epoch                     = 10
optimizer                       = 'sgd'  #' 'adam', 'sgd'
momentum                        = 0.9
weight_decay                    = 1e-4
train_days                      = [1, 2, 3, 4]
valid_days                      = [5]
random_crop                     = 416   # We choose 64 here because 30*2+1=61 is the expansion and 64 is the closest to resnet input requirement to integer
random_crop_valid               = 416
batch_size                      = 18

