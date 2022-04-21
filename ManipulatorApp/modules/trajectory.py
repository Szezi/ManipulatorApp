import os
import datetime as dt
import numpy as np
from ManipulatorApp.modules import IK


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
    :param table: Array of [command, traj, config, x, y, z, alfa, Servo5, Servo6, time, eff]; table[0] = home position
    :return: generated_path - Array of [command, traj, config, x, y, z , alfa, theta0, theta1, theta2, theta3, Servo5, Servo6, time, eff]
    """

    try:
        print('Generating path - started')

        home_position = table[0]
        # [command, traj, config, x, y, z , alfa, theta0, theta1, theta2, theta3, Servo5, Servo6, time, eff]
        # print(home_position)

        # Calculating inverse kinematics of home position and adding at 0 index of return arg generated_path
        home_values = IK.ik_geo(home_position[3], home_position[4], home_position[5], home_position[6],
                                home_position[10])
        print(home_values)
        if home_position[2] == 'config_1':
            generated_path_home = home_values[0]
        elif home_position[2] == 'config_2':
            generated_path_home = home_values[1]
        else:
            status = 'Unexpected value of config param'
            raise ValueError(status)

        index = 1
        generated_path = [
            [index, 'home', home_position[1], home_position[2],
             home_position[3], home_position[4], home_position[5], home_position[6],
             generated_path_home[0], generated_path_home[1], generated_path_home[2], generated_path_home[3],
             home_position[7], home_position[8], float(home_position[9]), home_position[10]]]

        for row_index in range(1, len(table)):
            # [command, traj, config, x, y, z , alfa, theta0, theta1, theta2, theta3, Servo5, Servo6, time, eff]
            command = table[row_index][0]
            traj = table[row_index][1]
            config = table[row_index][2]
            end_points = [table[row_index][3], table[row_index][4], table[row_index][5], table[row_index][6]]
            servo5 = table[row_index][7]
            servo6 = table[row_index][8]
            time = table[row_index][9]
            eff = table[row_index][10]

            # Initialing start_points - [x, y, z, alfa, config]
            if row_index == 1:
                start_points = [home_position[3], home_position[4], home_position[5], home_position[6],
                                home_position[2]]
            else:
                start_points = [table[row_index - 1][3], table[row_index - 1][4], table[row_index - 1][5],
                                table[row_index - 1][6], table[row_index - 1][2]]

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

                    # Increment index
                    index += 1

                    # Calculating inverse kinematics of each line in path_line and appending to generated_path
                    for n in range(0, sample):
                        alfa = alfa + orient_step

                        path_to_servos = IK.ik_geo(path_line[n][0], path_line[n][1], path_line[n][2], alfa, eff)
                        # Checking if generated points are in working area

                        if path_to_servos[2][2] == 'Calculations ended successfully':
                            # Checking position config and generating path
                            if config == 'config_1':
                                # print(path_to_servos[0])
                                path_to_append = [index, command, traj, config,
                                                  end_points[0], end_points[1], end_points[2], end_points[3],
                                                  path_to_servos[0][0], path_to_servos[0][1],
                                                  path_to_servos[0][2], path_to_servos[0][3],
                                                  servo5, servo6, float(time / sample), eff]

                                generated_path.append(path_to_append)
                            elif config == 'config_2':
                                # print(path_to_servos[1])
                                path_to_append = [index, command, traj, config,
                                                  end_points[0], end_points[1], end_points[2], end_points[3],
                                                  path_to_servos[1][0], path_to_servos[1][1],
                                                  path_to_servos[1][2], path_to_servos[1][3],
                                                  servo5, servo6, float(time / sample), eff]

                                generated_path.append(path_to_append)
                            else:
                                status = 'Unexpected value of config param'
                                raise ValueError(status)
                        else:
                            status = 'Error: Path outside the working Area. Line %d' % row_index
                            raise ValueError(status)

                elif traj == 'p2p':
                    # Calculating inverse kinematics for start and end points of trajectory
                    start_values = list(IK.ik_geo(start_points[0], start_points[1], start_points[2], alfa_start, eff))
                    end_values = list(IK.ik_geo(end_points[0], end_points[1], end_points[2], alfa, eff))
                    # print(start_values)
                    # print(end_values)

                    # Increment index
                    index += 1

                    # Checking if generated points are in working area
                    if end_values[2][2] == 'Calculations ended successfully':
                        # Checking start position config
                        if config_start == 'config_1':
                            start_pos_values = start_values[0].copy()
                        elif config_start == 'config_2':
                            start_pos_values = start_values[1].copy()
                        else:
                            status = 'Unexpected value of config param'
                            raise ValueError(status)
                        # print(start_pos_values)
                        # Checking end position config
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

                        # Generating path
                        for n in range(0, sample):
                            path_to_servos = [round(start_pos_values[0] + values_step[0], 2),
                                              round(start_pos_values[1] + values_step[1], 2),
                                              round(start_pos_values[2] + values_step[2], 2),
                                              round(start_pos_values[3] + values_step[3], 2)]
                            # print(path_to_servos)

                            start_pos_values = path_to_servos

                            path_to_append = [index, command, traj, config,
                                              end_points[0], end_points[1], end_points[2], end_points[3],
                                              path_to_servos[0], path_to_servos[1], path_to_servos[2],
                                              path_to_servos[3], servo5, servo6, float(time / sample), eff]

                            generated_path.append(path_to_append)
                    else:
                        status = 'Error: Path outside the working Area. Line %d' % row_index
                        raise ValueError(status)
                else:
                    status = 'Unexpected value of trajectory param.'
                    raise ValueError(status)

            elif command == 'wait':
                # Increment index
                index += 1

                path_to_append = [index, command, generated_path[-1][2], generated_path[-1][3], generated_path[-1][4],
                                  generated_path[-1][5], generated_path[-1][6], generated_path[-1][7],
                                  generated_path[-1][8], generated_path[-1][9], generated_path[-1][10],
                                  generated_path[-1][11], generated_path[-1][12], generated_path[-1][13], float(time), eff]
                generated_path.append(path_to_append)

            else:
                status = 'Unexpected value of command param.'
                raise ValueError(status)

        status = 'Generating path - Success'
        return generated_path, status

    except ValueError as status:
        return [0, 'errorr', 'error', 'error', 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'error'], str(status)

    except:
        status = 'Something went wrong'
        return [0, 'error', 'error', 'error', 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'error'], status

    finally:
        print('Generating path - Ended')


def write_generated_path_to_file(array: list, file_path: str, file_name: str, file_format: str):
    """
    Function writes robotic path generated using trajectory.path_generator() to file in specified location and name with date and time of creation.
    :param array: Array of xyz points to generate path
    :param file_path: Path of file
    :param file_name: Name of file
    :param file_format: Format of file e.g. (.txt)
    :return: File written in specified location
    """

    path = path_generator(array)
    path_data = path[0].copy()
    path_status = path[1]

    file_date = str(dt.date.today()) + '_' + dt.datetime.now().strftime("%H.%M.%S")

    try:
        # Opening file using contex manager and write each element from generated path to file.
        with open(os.path.join(file_path, file_name + file_date + file_format), 'w', encoding='utf-8') as file:
            file.write("[command, traj, config, x, y, z , alfa, theta0, theta1, theta2, theta3, Servo5, Servo6, time, eff]" + '\n')
            for element in path_data:
                file.write(str(element) + '\n')
            file.write(path_status)
    except FileNotFoundError:
        print('Invalid file path')
    except:
        print('Sth went wrong during writing to file')


def read_generated_path_from_file(file_path: str):
    """
    Function reads robotic path from file in specified location.
    :param file_path: Path of file
    :return: path_from_file - list
    """

    # Initialing empty list
    path_from_file = []
    try:
        # Opening file using contex manager and write read lines from file into list.
        # Line styling of file.txt [command, traj, config, x, y, z , alfa, theta0, theta1, theta2, theta3, Servo5, Servo6, time, eff]
        with open(os.path.join(file_path), 'r', encoding='utf-8') as file:
            path = [line.rstrip() for line in file]
            for elem in path[:-1]:
                element = elem.split(', ')
                element[0] = element[0][1:]
                element[1] = element[1][1:-1]
                element[2] = element[2][1:-1]
                element[3] = element[3][1:-1]
                element[-1] = element[-1][:-1]
                path_from_file.append(element)
    except FileNotFoundError:
        print('Invalid file path / File not found')
    except:
        print('Sth went wrong during reading the file')
    return path_from_file


class RoboticMove(object):
    """ The class contains methods that generate the next and previous lines from a file with robotic path. """

    def __init__(self, generated_path):
        self.list_len = len(generated_path)
        self.generated_path = iter(generated_path)
        self.index = -1
        self.last_index = -1
        self.history = []

    def __del__(self):
        del self.generated_path

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index >= self.list_len:
            raise StopIteration
        elif self.index <= self.last_index:
            return self.history[self.index]
        else:
            line = next(self.generated_path)
            self.history.append(line)
            self.last_index += 1
            return line

    def prev(self):
        self.index -= 1
        if self.index == -1:
            raise StopIteration
        else:
            return self.history[self.index]
