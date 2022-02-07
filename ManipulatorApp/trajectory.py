import numpy as np
import IK


def cp_linear(p_start: list, p_finish: list, n=10):
    """
    Produces linear interpolation between two 3D points
    :param p_start: list of 3 floats (x, y, z)
    :param p_finish: list of 3 floats (x, y, z)
    :param n: Number of points to sample; default n=10
    :return:  np.array: Interpolated points
    """

    v = np.array([p_finish]) - np.array([p_start])
    t = np.array([np.linspace(0, 1, n)]).T
    return p_start + t.dot(v)


def path_generator(table: list):
    """
    Generates robotics arm parameters from path of given 3D points. \n
    Commands - home, move, wait \n
    traj - cp_linear, p2p \n
    config - config_1, config_2 \n
    Parameters can not be empty \n
    :param table: Array of [command, traj, config, end_points[x, y, z, alfa], time, eff]; table[0] = home position
    :return: generated_path - Array of [command, [theta0, theta1, theta2, theta3], time]
    """

    try:
        print('Generating path - started')

        home_position = table[0]
        # print(home_position)

        # Calculating inverse kinematics of home position and adding at 0 index of return arg generated_path
        home_values = IK.ik_geo(home_position[3][0], home_position[3][1], home_position[3][2], home_position[3][3],
                                home_position[5])

        if home_position[2] == 'config_1':
            generated_path_home = home_values[0]
        elif home_position[2] == 'config_2':
            generated_path_home = home_values[0]
        else:
            status = 'Unexpected value of config param'
            raise ValueError(status)

        generated_path = ['home', generated_path_home, float(home_position[4])]

        for row_index in range(1, len(table)):
            # [command, traj, config, end_points, time, eff]
            command = table[row_index][0]
            traj = table[row_index][1]
            config = table[row_index][2]
            end_points = table[row_index][3]
            time = table[row_index][4]
            eff = table[row_index][5]

            # Initialing start_points - [x, y, z, alfa, config]
            if row_index == 1:
                start_points = [home_position[3][0], home_position[3][1], home_position[3][2], home_position[3][3],
                                home_position[2]]
            else:
                start_points = [table[row_index - 1][3][0], table[row_index - 1][3][1], table[row_index - 1][3][2],
                                table[row_index - 1][3][3], table[row_index - 1][2]]

            alfa = end_points[3]
            alfa_start = start_points[3]
            config_start = start_points[4]

            sample = int(time * 10)

            if command == 'move' or command == 'home':
                if traj == 'cp_linear':
                    # Interpolating line between given 3D points and given sample
                    path_line = cp_linear([start_points[0], start_points[1], start_points[2]],
                                          [end_points[0], end_points[1], end_points[2]], sample)
                    # print(path_line)

                    # Calculating step of changing effector orientation
                    if alfa == alfa_start:
                        orient_step = 0
                    else:
                        orient_step = (alfa - alfa_start) / sample

                    # Calculating inverse kinematics of each line in path_line and appending to generated_path
                    for n in range(0, sample):
                        alfa = alfa + orient_step

                        path_to_servos = IK.ik_geo(path_line[n][0], path_line[n][1], path_line[n][2], alfa, eff)

                        if config == 'config_1':
                            # print(path_to_servos[0])
                            path_to_append = [str(command), path_to_servos[0], float(time / sample)]
                            generated_path.append(path_to_append)
                        elif config == 'config_2':
                            # print(path_to_servos[1])
                            path_to_append = [str(command), path_to_servos[1], float(time / sample)]
                            generated_path.append(path_to_append)
                        else:
                            status = 'Unexpected value of config param'
                            raise ValueError(status)

                elif traj == 'p2p':
                    # Calculating inverse kinematics for start and end points of trajectory
                    start_values = list(IK.ik_geo(start_points[0], start_points[1], start_points[2], alfa_start, eff))
                    end_values = list(IK.ik_geo(end_points[0], end_points[1], end_points[2], alfa, eff))
                    # print(start_values)
                    # print(end_values)

                    if config_start == 'config_1':
                        start_pos_values = start_values[0].copy()
                    elif config_start == 'config_2':
                        start_pos_values = start_values[1].copy()
                    else:
                        status = 'Unexpected value of config param'
                        raise ValueError(status)
                    # print(start_pos_values)
                    if config == 'config_1':
                        values_difference = [end_values[0][0] - start_pos_values[0],
                                             end_values[0][1] - start_pos_values[1],
                                             end_values[0][2] - start_pos_values[2],
                                             end_values[0][3] - start_pos_values[3]]
                    elif config == 'config_2':
                        values_difference = [end_values[1][0] - start_pos_values[0],
                                             end_values[1][1] - start_pos_values[1],
                                             end_values[1][2] - start_pos_values[2],
                                             end_values[1][3] - start_pos_values[3]]
                    else:
                        status = 'Unexpected value of config param.'
                        raise ValueError(status)
                    # print(values_difference)
                    values_step = [x / sample for x in values_difference]
                    # print(values_step)

                    for n in range(0, sample):
                        path_to_servos = [round(start_pos_values[0] + values_step[0], 2),
                                          round(start_pos_values[1] + values_step[1], 2),
                                          round(start_pos_values[2] + values_step[2], 2),
                                          round(start_pos_values[3] + values_step[3], 2)]
                        # print(path_to_servos)

                        start_pos_values = path_to_servos

                        path_to_append = [str(command), path_to_servos, float(time / sample)]
                        generated_path.append(path_to_append)

                else:
                    status = 'Unexpected value of trajectory param.'
                    raise ValueError(status)

            elif command == 'wait':
                path_to_append = [str(command), generated_path[-1][1], float(time)]
                generated_path.append(path_to_append)

            else:
                status = 'Unexpected value of command param.'
                raise ValueError(status)

        status = 'Generating path - Success'
        return generated_path, status

    except ValueError as status:
        return ['error', [0.0, 0.0, 0.0, 0.0], 0.0], str(status)

    except:
        status = 'Something went wrong'
        return ['error', [0.0, 0.0, 0.0, 0.0], 0.0], status

    finally:
        print('Generating path - Ended')


# [command, traj, config, end_points, time]
test_array = [['home', 'p2p', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
              ['move', 'p2p', 'config_1', [0, 0, 472, 90], 3.0, [54, 0]],
              ['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
              ['wait', '', '', [0, 0, 0, 0], 10.0, [54, 0]]]

test = path_generator(test_array)
print(*test[0], sep='\n')
print(test[1])
