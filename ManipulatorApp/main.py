import trajectory


if __name__ == '__main__':
    # [command, traj, config, end_points, time]
    test_array = [['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['move', 'cp_linear', 'config_1', [0, 0, 472, 90], 3.0, [54, 0]],
                  ['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['wait', '', '', [0, 0, 0, 0], 10.0, [54, 0]]]

    file_path_write = r'C:\Users\SZILING\Desktop\ManipulatorApp\data'
    file_name_write = 'generated_path_'
    file_format_write = '.txt'

    # trajectory.write_generated_path_to_file(test_array, file_path_write, file_name_write, file_format_write)

    file_path_read = r'C:\Users\SZILING\Desktop\ManipulatorApp\data\test_path.txt'
    read_path = trajectory.read_generated_path_from_file(file_path_read)
    print(read_path)

    test1 = trajectory.RoboticMove(read_path)
    print('-1--------1-----1-------1-------1')
    print(test1.next())
    print(test1.next())
    print(test1.next())
    print(test1.next())
    print(test1.next())
    print('------------')
    print(test1.prev())
    print(test1.next())
    print(test1.prev())
