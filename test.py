from compare import generate_user_data, generate_uniform_points_in_circle, simulate
from inputs import system_parameters
from check_noma import check_noma_possible

ue_locations = generate_uniform_points_in_circle(8, system_parameters['cell_redius'])
H_db, th_data_Rate = generate_user_data(8, 10, ue_locations)
(power ,association) = simulate(H_db, th_data_Rate, 10)
print(f"{association=}")
print(f"{power=}")
