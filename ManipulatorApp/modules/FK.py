import numpy as np
import math


def fk_dh(theta1: int, theta2: int, theta3: int, theta4: int, eff: list):
    """
    Function calculate forward kinematics of the robotic arm with given parameters and specified length of robotic arm links.
    Forward kinematics is being calculated using Denavit–Hartenberg notation.
    :param theta1: Base rotation angle
    :param theta2: 1st link rotation angle
    :param theta3: 2nd link rotation angle
    :param theta4: 3rd link rotation angle
    :param eff: End effector dimensions

    :return: alpha; xyz_pos_link3; xyz_pos_link2; xyz_pos_link1; status: Orientation and list of xyz positions of each link end

    """
    try:
        # Input parameters

        # Convert angels in degrees to radians
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)
        theta3 = math.radians(theta3)
        theta4 = math.radians(theta4)

        # Robotic arm links length
        l1 = 118  # base height
        l2 = 150  # 1st links length
        l3 = 150  # 2nd links length
        l4 = eff[0]  # "L" effector dimension
        l5 = eff[1]  # "H" effector dimension

        # DH table with input parameters
        table_dh = np.array([[theta1, l1, 0, math.radians(90)],
                             [theta2, 0, l2, 0],
                             [theta3, 0, l3, 0],
                             [theta4, 0, l4, 0],
                             [math.radians(-90), 0, l5, 0]])

        # Generation of homogenous transformation matrices Ti
        def dh(i):
            t_dh = np.array([[math.cos(table_dh[i, 0]), (-1 * math.sin(table_dh[i, 0]) * math.cos(table_dh[i, 3])),
                              (math.sin(table_dh[i, 0]) * math.sin(table_dh[i, 3])),
                              table_dh[i, 2] * math.cos(table_dh[i, 0])],
                             [math.sin(table_dh[i, 0]), (math.cos(table_dh[i, 0]) * math.cos(table_dh[i, 3])),
                              (-1 * math.cos(table_dh[i, 0]) * math.sin(table_dh[i, 3])),
                              table_dh[i, 2] * math.sin(table_dh[i, 0])],
                             [0, math.sin(table_dh[i, 3]), math.cos(table_dh[i, 3]), table_dh[i, 1]],
                             [0, 0, 0, 1]])
            return t_dh

        matrix_t1 = dh(0)
        matrix_t2 = dh(1)
        matrix_t3 = dh(2)
        matrix_t4 = dh(3)
        matrix_t5 = dh(4)

        # Determination of the homogenous transformation matrices
        matrix_t12 = matrix_t1 @ matrix_t2
        matrix_t123 = matrix_t12 @ matrix_t3
        matrix_t1234 = matrix_t123 @ matrix_t4
        matrix_t12345 = matrix_t1234 @ matrix_t5

        # 1st link XYZ position
        x1 = matrix_t12[0, 3]
        y1 = matrix_t12[1, 3]
        z1 = matrix_t12[2, 3]
        xyz_pos_link1 = [float(round(x1, 2)), float(round(y1, 2)), float(round(z1, 2))]

        # 2nd link XYZ position
        x2 = matrix_t123[0, 3]
        y2 = matrix_t123[1, 3]
        z2 = matrix_t123[2, 3]
        xyz_pos_link2 = [float(round(x2, 2)), float(round(y2, 2)), float(round(z2, 2))]

        # 3rd link XYZ position
        if eff[1] == 0:
            # Position without end effector
            x3 = matrix_t1234[0, 3]
            y3 = matrix_t1234[1, 3]
            z3 = matrix_t1234[2, 3]
            xyz_pos_link3 = [float(round(x3, 2)), float(round(y3, 2)), float(round(z3, 2))]
        elif eff[1] != 0:
            # Position with end effector
            x4 = matrix_t12345[0, 3]
            y4 = matrix_t12345[1, 3]
            z4 = matrix_t12345[2, 3]
            xyz_pos_link3 = [float(round(x4, 2)), float(round(y4, 2)), float(round(z4, 2))]
        else:
            raise ValueError('Unexpected value xyz_pos_link3')

        # End effector orientation
        z_ef = round(matrix_t1234[2, 3]) - round(z2)
        alpha = math.degrees(math.asin(z_ef / l4))
        status = "Forward kinematics calculations ended successfully"
        return round(alpha), xyz_pos_link3, xyz_pos_link2, xyz_pos_link1, status

    except ZeroDivisionError:
        status = 'L4 dimension needs to be greater then 0'
        return 0, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], status

    except:
        status = 'Something went wrong.'
        return 0, [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], status

    finally:
        print('Forward kinematics calculations ended')


# test
# print(fk_dh(0, 90, 0, 0, [54, 0]))
