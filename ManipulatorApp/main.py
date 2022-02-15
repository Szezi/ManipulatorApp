import trajectory
import os

if __name__ == '__main__':
    # [command, traj, config, end_points, time]
    test_array = [['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['move', 'cp_linear', 'config_1', [0, 0, 472, 90], 3.0, [54, 0]],
                  ['home', 'cp_linear', 'config_1', [0, 0, 460, 90], 3.0, [54, 0]],
                  ['wait', '', '', [0, 0, 0, 0], 10.0, [54, 0]]]

    test_path = trajectory.path_generator(test_array)

    test_path_data = test_path[0].copy()
    test_path_status = test_path[1]

    file_path = r'C:\Users\SZILING\Desktop\ManipulatorApp\data'

    try:
        with open(os.path.join(file_path, 'test_path.txt'), 'w', encoding='utf-8') as f:
            f.write('[command, [theta0, theta1, theta2, theta3], time]' + '\n')
            for element in test_path_data:
                f.write(str(element) + '\n')
            f.write(test_path_status)
    except:
        print('Sth went wrong')
