import math


def ik_geo(px: int, py: int, pz: int, alfa: int, eff: list):
    """
    Function calculate inverse kinematics of the robotic arm with given parameters and specified length of robotic arm links.
    Inverse kinematics is being calculated using geometrical method.
    :param px: X value of target position
    :param py: Y value of target position
    :param pz: Z value of target position
    :param alfa: End effector orientation
    :param eff: End effector dimensions
    :return: config_1[theta0, theta1, theta2, theta3], config_2[theta0, theta11, theta22, theta33], Kom(kom_config_1, kom_config_2, Success/Sth. wrong)
    """

    # Robotic arm links length
    l0 = 118  # base height
    l1 = 150  # 1st links length
    l2 = 150  # 2nd links length
    l3 = eff[0]  # "L" effector dimension
    l4 = eff[1]  # "H" effector dimension
    try:
        # End effector orientation angel converted to radians
        alfa = math.radians(alfa)

        # XY plane - determination of theta0 and R
        if px != 0 and py != 0:
            theta0 = math.atan(py / px)
        elif px != 0 and py == 0:
            theta0 = math.radians(0)
        elif px == 0 and py > 0:
            theta0 = math.radians(90)
        elif px == 0 and py < 0:
            theta0 = math.radians(-90)
        elif px == 0 and py == 0:
            theta0 = math.radians(0)
        else:
            raise ValueError('Unexpected angel theta0')

        # Position Z,Y raised to power of 2
        px2 = px ** 2
        py2 = py ** 2
        # Calculate vector_r
        vector_r = math.sqrt(px2 + py2)
        # _____________________________________________________________________________________________________________
        # Effector ZR plane
        c = math.sqrt(l3 ** 2 + l4 ** 2)
        beta = math.atan(l4 / l3)
        z_effector = c * math.sin(alfa - beta)
        r_effector = c * math.cos(alfa - beta)

        # Designation of the Z, R end of the second link
        # Subtract the effector Z, R from the ZR of the system and reduce by the base height
        z_2nd_link = pz - l0 - z_effector
        r_2nd_link = vector_r - r_effector

        # ____________________________________________________________________________________________________________

        # ZR plane - determination of theta1 and theta2
        delta = r_2nd_link ** 2 + z_2nd_link ** 2
        temp_l = (delta - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
        theta2 = math.acos(temp_l)
        theta22 = (-1 * (math.acos(temp_l)))
        gamma1 = math.acos((delta + l1 ** 2 - l2 ** 2) / (2 * math.sqrt(delta) * l1))
        gamma2 = -1 * (math.acos((delta + l1 ** 2 - l2 ** 2) / (2 * math.sqrt(delta) * l1)))

        if r_2nd_link == 0:  # The point is on the Z axis of the system
            theta1 = math.radians(90) - gamma1
            theta11 = math.radians(90) - gamma2
        else:
            z_divide_r = z_2nd_link / r_2nd_link
            if z_divide_r >= 0:  # The point is located in the 1st quarter of the ZR coordinate system
                theta1 = math.atan(z_2nd_link / r_2nd_link) - gamma1
                theta11 = math.atan(z_2nd_link / r_2nd_link) - gamma2
            elif z_divide_r < 0:  # # the point is located in the 2nd quarter of the ZR coordinate system
                theta1 = (math.radians(180) + math.atan(z_2nd_link / r_2nd_link)) - gamma1
                theta11 = (math.radians(180) + math.atan(z_2nd_link / r_2nd_link)) - gamma2
            else:
                raise ValueError('Unexpected angel theta1/theta11')

        # Determination of the angle of inclination of the 2nd link in relation to the ground plane
        z1 = l1 * math.sin(theta1)  # height in Z axis of joint R1, R2
        z11 = l1 * math.sin(theta11)

        beta = math.asin((z_2nd_link - z1) / l2)  # Angle of inclination of the 2nd link in relation to the ground plane
        beta2 = math.asin((z_2nd_link - z11) / l2)

        # Calculation of theta3
        theta3 = alfa - beta
        theta33 = alfa - beta2

        # Convert from radians to degrees
        theta0 = math.degrees(theta0)
        theta1 = math.degrees(theta1)
        theta2 = math.degrees(theta2)
        theta3 = math.degrees(theta3)
        theta11 = math.degrees(theta11)
        theta22 = math.degrees(theta22)
        theta33 = math.degrees(theta33)

        if -90 <= theta0 <= 90 and 0 <= theta1 <= 180 and -120 <= theta2 <= 60 and -90 <= theta3 <= 90:
            status_config_1 = "Config_1: Success"
            config_1 = [round(theta0, 2), round(theta1, 2), round(theta2, 2), round(theta3, 2)]

        else:
            config_1 = [0.0, 0.0, 0.0, 0.0]
            status_config_1 = "Config_1: No results"

        if -90 <= theta0 <= 90 and 0 <= theta11 <= 180 and -120 <= theta22 <= 60 and -90 <= theta33 <= 90:
            status_config_2 = "Config_2: Success"
            config_2 = [round(theta0, 2), round(theta11, 2), round(theta22, 2), round(theta33, 2)]

        else:
            status_config_2 = "Config_2: No results"
            config_2 = [0.0, 0.0, 0.0, 0.0]

        status = [status_config_1, status_config_2, 'Calculations ended successfully']
        return list(config_1), list(config_2), status

    except ValueError:
        status = ['', '', 'Something went wrong']
        return [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], status

    except:
        status = ['', '', 'The entered data is incorrect ']
        return [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], status

    finally:
        print('Inverse kinematics calculations ended')

#test
# test = ik_geo(0, 0, 472, 90, [54, 0])
# print(test[0])
# print(test[1])
# print(test[2][2])
