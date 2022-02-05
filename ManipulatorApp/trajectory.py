import numpy as np
import IK


def cp_linear(p_start: list, p_finish: list, n=10):
    """
    Produces linear interpolation between two 3D points
    Args:
        p_start (list of 3 floats): Description
        p_finish (list of 3 floats): Description
        n (int, optional): Number of points to sample
    Returns:
        np.array: Interpolated points
    """
    v = np.array([p_finish]) - np.array([p_start])
    t = np.array([np.linspace(0, 1, n)]).T
    return p_start + t.dot(v)


def path_generator(tablica):
    start_points = [0, 0, 472, 90, 'config_1']
    generated_path = []
    print('Generating path - started')
    for line in tablica:
        command = line[0]
        traj = line[1]
        config = line[2]
        end_points = line[3]
        time = line[4]
        eff = line[5]

        alfa_start = start_points[3]
        alfa = end_points[3]
        config_start = start_points[4]

        sample = int(time*10)

        if traj == 'cp_linear':
            # print('cp_linear')
            path_line = cp_linear([start_points[0], start_points[1], start_points[2]],
                                  [end_points[0], end_points[1], end_points[2]], sample)
            # print(path_line)

            if alfa == alfa_start:
                orient_step = 0
            else:
                orient_step = (alfa - alfa_start) / sample

            for n in range(0, sample):
                alfa = alfa + orient_step

                path_to_servos = IK.ik_geo(path_line[n, 0], path_line[n, 1], path_line[n, 2], alfa, eff)

                if config == 'config_1':
                    # print(path_to_servos[0])
                    path_to_append = [command, path_to_servos[0], time]
                    generated_path.append(path_to_append)
                elif config == 'config_2':
                    # print(path_to_servos[1])
                    path_to_append = [command, path_to_servos[1], time]
                    generated_path.append(path_to_append)
                else:
                    print('Something went wrong')
                    raise ValueError

        elif traj == 'p2p':
            # print('p2p')
            start_values = list(IK.ik_geo(start_points[0], start_points[1], start_points[2], alfa_start, eff))
            end_values = list(IK.ik_geo(end_points[0], end_points[1], end_points[2], alfa, eff))

            # print(start_values)
            # print(end_values)
            if config_start == 'config_1':
                start_points = start_values[0].copy()
            elif config_start == 'config_2':
                start_points = start_values[1].copy()

            if config == 'config_1':
                values_difference = [end_values[0][0] - start_points[0],
                                     end_values[0][1] - start_points[1],
                                     end_values[0][2] - start_points[2],
                                     end_values[0][3] - start_points[3]]
            elif config == 'config_2':
                values_difference = [end_values[1][0] - start_points[0],
                                     end_values[1][1] - start_points[1],
                                     end_values[1][2] - start_points[2],
                                     end_values[1][3] - start_points[3]]
            else:
                print('Something went wrong')
                raise ValueError

            values_step = [x / sample for x in values_difference]
            # print(values_step)

            # print('_________________')

            for n in range(0, sample):
                path_to_servos = [start_points[0] + values_step[0], start_points[1] + values_step[1],
                                  start_points[2] + values_step[2], start_points[3] + values_step[3]]
                print(path_to_servos)
                start_points = path_to_servos

                path_to_append = [command, path_to_servos[0], time]
                generated_path.append(path_to_append)

        return generated_path
    print('Generating path - Ended')

# [command, traj, config, end_points, time]
tablica = [['move', 'cp_linear', 'config_1', [0, 0, 450, 90], 3.0, [54, 0]],
           ['move', 'cp_linear', 'config_1', [0, 0, 472, 90], 3.0, [54, 0]],
           ['move', 'cp_linear', 'config_1', [0, 0, 450, 90], 3.0, [54, 0]]]

print(path_generator(tablica))
