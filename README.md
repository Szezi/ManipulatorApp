<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Szezi/ManipulatorApp">
    <img src="data\images\icons8-robot-50.png" alt="Logo" width="50" height="50">
  </a>
<h3 align="center">ManipulatorApp</h3>
  <p align="center">
ManipulatorApp is a desktop application that allows to control the robotic arm powered by Arduino in both manual and automatic mode with the possibility of selecting the type of the trajectory being carried out. It also allows to calibrate the system, perform forward and inverse kinematics calculations as well as simulate the programmed sequence of movements.
    <br />
    <a href="https://github.com/Szezi/ManipulatorApp"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
      <ul>
        <li><a href="#arduino">Arduino</a></li>
      </ul>
      <ul>
        <li><a href="#technologies">Technologies</a></li>
      </ul>
    </li>
    <li><a href="#about-yhe-project">About the project</a></li>
      <ul>
        <li><a href="#desktop-app">Desktop App</a></li>
      </ul>
      <ul>
        <li><a href="#robotic-arm-prototype">Robotic arm prototype</a></li>
      </ul>
      <ul>
        <li><a href="#repeatability-test-of-the-robot's-movements">Repeatability test of the robot's movements</a></li>
      </ul>
    <li><a href="#todo">Todo</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To run this project, create virtual environment and install it locally.

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/Szezi/ManipulatorApp
   ```
2. Install packages
   ```sh
   $ pip install -r requirements.txt
   ```
3. Run main.py

### Arduino
To control robotic arm install a standard Firmata sketch on Arduino board.

   ```sh
   File -> Examples -> Firmata -> Standard Firmata
   ```
   
### Technologies

* [Python](https://www.python.org/downloads/release/python-370/)
* [PySide2](https://pypi.org/project/PySide2/)
* [pyFirmata2](https://pypi.org/project/pyFirmata2/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="data\images\vis_arduino.jpg" alt="Project_arduino">
</div>

Robotic arm with five degrees of freedom was designed, which was made with the use of the possibility of printing the necessary elements using 3D printing technology and aluminum profiles. Standard servo motors were used to drive the bearing arms. Control system was based on the Arduino MEGA2560 microcontroller. To control the created manipulator, a desktop application was created that connects to the microcontroller and allows it to be controlled in the manual and automatic control mode with a specific trajectory. Finally, tests were carried out with the use of the created manipulator, the results allowed to determine the technical parameter, which is the repeatability of the robot's movements.



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Desktop app -->
### Desktop app
ManipulatorApp is a desktop application that allows to control the robotic arm powered by Arduino in both manual and automatic mode with the possibility of selecting the type of the trajectory being carried out. It also allows to calibrate the system, perform forward and inverse kinematics calculations as well as simulate the programmed sequence of movements.

The desktop application consists of several screens with different functionality. Switching between the selected screens is done with the use of the pull-down side menu. In the upper bar there is information about the currently selected screen, while in the lower part of the screen there is a bar with application operation messages. These logs are also saved in the appropriate file.

<div align="center">
<img src="data\images\page_home.PNG" alt="page_Home">
</div>

The Home screen contains links to the remaining screens and information about the presence of the effector mounting, communication status with the microcontroller and the current position of the robotic arm.

<div align="center">
<img src="data\images\page_fk.PNG" alt="page_fk">
</div>

The FK screen is used to calculate the forward kinematics of the manipulator. Using the sliders, the user enters the input data and the result is presented on the visualization. The sliders change their color as they approach their maximum. There is also a button below the sliders to reset their values.

<div align="center">
<img src="data\images\page_ik.PNG" alt="page_ik">
</div>

The IK screen is used to calculate the inverse kinematics of the manipulator. Using the sliders, the user enters the input data, and then the result in two configurations is presented in two tabs and on the visualization. There is also a button below the sliders to reset their values.

<div align="center">
<img src="data\images\page_manual.PNG" alt="page_manual">
</div>

The manual mode screen is used to control the robot arm using sliders. Below them are 3 buttons. The first places the robot arm in the pistol position. The second one puts manipulator in the home position and the third resets the entered values. In addition, the robot is also simulated in the program.

<div align="center">
<img src="data\images\page_auto.PNG" alt="page_auto">
</div>

The automatic mode screen consists of 3 tabs. The first tab contains sliders for entering values ​​into the created sequence of robot movements. It also allows to create a home position and add the entered values ​​in the appropriate configuration and trajectories to the table on the second tab.
The second tab contains a table containing the sequences of the robots movements. After completing it,  it is possible with the appropriate button to generate the robots path and save it to disk.

<div align="center">
<img src="data\images\page_auto_save.png" alt="page_auto_save">
</div>

Robotic program is being saved with name "generated_path_ + actual date and time" to selected folder in format .txt.
First row contains information of saved data.

<div align="center">
<img src="data\images\page_auto_txt.png" alt="page_auto_txt">
</div>

In order to call up the created program, load the previously saved program with the READ button and then initiate the program with the INIT button. After selecting the appropriate SIM / SERVO mode, it is possible to run the program in selected mode by one line of code or in full.

<div align="center">
<img src="data\images\page_set.PNG" alt="page_set">
</div>

The settings screen consists of 4 tabs. The first one contains information about the project, the dimensions of the robot and the components used. The second is to establish communication with the robot. The third is for system calibration. The last one allows you to enter information about the effector used. The choice of the effector affects the calculations made in other places of the application.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Robotic Arm Prototype-->
### Robotic arm prototype
Prototype of the robotic arm was designed in AutoCad Inventor. 
A decision was made to design the system in a way that allows its possible inexpensive implementation 
and the chance of making as many elements as possible using 3D printing technology. 
It was also decided to use servo modeling motors and to leave the manipulator 5 degrees of freedom. 
It was decided that the designed robot will have a monolithic structure with an anthropomorphic structure.

<div align="center">
<img src="data\images\prototype_project.JPG" alt="prototype_project">
</div>

The necessary elements have been specially designed for 3D printing and then printed using this technology. 
For robotic links aluminium profiles were used with special holes to decrease weight. 
The printed elements with purchase items are shown below.

<div align="center">
<img src="data\images\elements.png" alt="Elements">
</div>

Assembly of designed robotic arm is shown below:
<div align="center">
<img src="data\images\robotic_arm.PNG" alt="Robotic_Arm">
</div>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Repeatability tests of the robot's movements-->
### Repeatability test of the robot's movements
Repeatability tests of the robot's movements were carried out. 
After calibration of robotic arm 2 test paths were prepared and saved to:

1. Test_path_01
<div align="center">
<img src="data\images\test_1.PNG" alt="test_1">
</div>

```
   \data\test_path_01.txt
   ```
2. Test_path_02
<div align="center">
<img src="data\images\test_1.PNG" alt="test_1">
</div>

```
   \data\test_path_02.txt
   ```

The test results showed a high repeatability of the system. 
However, noticeable system vibrations can be observed due to imperfections of the model prototype. 
The result and videos from the tests are presented below.
* [test_path_01_video](https://github.com/Szezi/ManipulatorApp/blob/master/data/images/VIDEO_test1.mp4)
* [test_path_02_video](https://github.com/Szezi/ManipulatorApp/blob/master/data/images/VIDEO_test2.mp4)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Todo -->
## Todo

- [ ] Circular movement
- [ ] Unit tests
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GPL-3.0 license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Szezi/ManipulatorApp](https://github.com/Szezi/ManipulatorApp)

<p align="right">(<a href="#top">back to top</a>)</p>
