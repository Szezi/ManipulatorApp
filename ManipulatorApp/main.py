import trajectory
import os
import datetime as dt


def write_generated_path_to_file(array: list, file_path: str, file_name: str, file_format: str):
    """
    Function writes robotic path generated using trajectory.path_generator() to file in specified location and name with date and time of creation.
    :param array: Array of xyz points to generate path
    :param file_path: Path of file
    :param file_name: Name of file
    :param file_format: Format of file e.g. (.txt)
    :return: File written in specified location
    """

    path = trajectory.path_generator(array)
    path_data = path[0].copy()
    path_status = path[1]

    file_date = str(dt.date.today()) + '_' + dt.datetime.now().strftime("%H.%M.%S")

    try:
        # Opening file using contex manager and write each element from generated path to file.
        with open(os.path.join(file_path, file_name + file_date + file_format), 'w', encoding='utf-8') as file:
            file.write("['command', theta0, theta1, theta2, theta3, time]" + '\n')
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
        # Line styling of file.txt ['command', 'theta0', 'theta1', 'theta2', 'theta3', 'time']
        with open(os.path.join(file_path), 'r', encoding='utf-8') as file:
            path = [line.rstrip() for line in file]
            for elem in path[:-1]:
                element = elem.split(', ')
                element[0] = element[0][2:-1]
                element[-1] = element[-1][:-1]
                path_from_file.append(element)
    except FileNotFoundError:
        print('Invalid file path / File not found')
    except:
        print('Sth went wrong during reading the file')
    return path_from_file


if __name__ == '__main__':
    # [command, traj, config, end_points, time]
    test_array = [['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['move', 'cp_linear', 'config_1', [0, 0, 472, 90], 3.0, [54, 0]],
                  ['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['wait', '', '', [0, 0, 0, 0], 10.0, [54, 0]]]

    file_path_write = r'C:\Users\SZILING\Desktop\ManipulatorApp\data'
    file_name_write = 'generated_path_'
    file_format_write = '.txt'

    write_generated_path_to_file(test_array, file_path_write, file_name_write, file_format_write)

    file_path_read = r'C:\Users\SZILING\Desktop\ManipulatorApp\data\test_path.txt'
    read_path = read_generated_path_from_file(file_path_read)
    print(read_path)
