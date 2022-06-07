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
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
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

Robotic arm with five degrees of freedom was designed, which was made with the use of the possibility of printing the necessary elements using 3D printing technology and aluminum profiles. Standard servo motors were used to drive the bearing arms. Control system was based on the Arduino MEGA2560 microcontroller. To control the created manipulator, a desktop application was created that connects to the microcontroller and allows it to be controlled in the manual and automatic control mode with a specific trajectory. Finally, tests were carried out with the use of the created manipulator, the results of which allowed to determine the technical parameter, which is the repeatability of the robot's movements.



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Desktop app -->
### Desktop app
ManipulatorApp is a desktop application that allows to control the robotic arm powered by Arduino in both manual and automatic mode with the possibility of selecting the type of the trajectory being carried out. It also allows to calibrate the system, perform forward and inverse kinematics calculations as well as simulate the programmed sequence of movements.

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Robotic Arm Prototype-->
### Robotic Arm Prototype
Prototype of the robotic arm was designed in AutoCad Inventor. 
A decision was made to design the system in a way that allows its possible inexpensive implementation 
and the chance of making as many elements as possible using 3D printing technology. 
It was also decided to use servo modeling motors and to leave the manipulator 5 degrees of freedom. 
It was decided that the designed robot will have a monolithic structure with an anthropomorphic structure.

The necessary elements have been specially designed for 3D printing and then printed using this technology. 
For robotic links aluminium profiles were used with special holes to decrease weight. 
The printed elements with purchase items are shown below.

<div align="center">
<img src="data\images\elements.png" alt="Elements">
</div>

Assembly of designed robotic arm is shown below:
<div align="center">
<img src="data\images\robotic_arm.png" alt="Robotic_Arm">
</div>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Repeatability tests of the robot's movements-->
### Repeatability test of the robot's movements
Repeatability tests of the robot's movements were carried out. 
After calibration of robotic arm 2 test paths were prepared and saved to:

1. Test_path_01
<div align="center">
<img src="data\images\test_1.png" alt="test_1">
</div>

```
   \data\test_path_01.txt
   ```
2. Test_path_02
<div align="center">
<img src="data\images\test_1.png" alt="test_1">
</div>

```
   \data\test_path_02.txt
   ```

The test results showed a high repeatability of the system. 
However, noticeable system vibrations can be observed due to imperfections of the model prototype. 
The result and videos from the tests are presented below.


<div align="center">
<video src='data\images\VIDEO_test1.mp4' width=180/>
</video>
</div>

<div align="center">
<video src='data\images\VIDEO_test2.mp4' width=180/>
</video>
</div>

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
