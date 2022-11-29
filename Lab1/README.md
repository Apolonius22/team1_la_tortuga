# team1_la_tortuga

# Folder Structure


# Real simulation

- done in Sparkassen lecture room

# Steps for map creation
1.	establish connection with robot
2.	launch SLAM
3.	drive around in room
4.	save map
# Code for executing steps in real 
1.	Setup PC
1.1.	make sure robot & PC are in the same Network
1.2.	go into docker folder
1.3.	bash run_docker.sh
1.4.	gedit ~/.bashrc
1.5.	a textfile will pop up
1.6.	add at the end:

export ROS_MASTER_URI=http://{IP_ADDRESS_OF_REMOTE_PC}:11311
export ROS_HOSTNAME={IP_ADDRESS_OF_RASPBERRY_PI_3}

1.7.	change both IP-Addresses to the IP of your PC (check IP with <ifconfig>)
1.8.	save File
1.9.	source ~/.bashrc
1.10.	roscore 
2.	open new terminal
2.1.	ssh ubunt 192.168.73.61 (IP of Raspberry)
2.2.	enter password (turtlebot)
2.3.	nano ~/.bashrc
2.4.	change IP-Adress of Master to PC-IP and Host-IP to Raspberry IP
2.5.	cntr + o to save and cntr + x to exit
2.6.	source ~/.bashrc
2.7.	roslaunch turtlebot3_bringup turtlebot3_robot.launch
2.8.	wait till calibration end
3.	open new terminal 
3.1.	navigate to docker
3.2.	bash_into_docker.sh
3.3.	roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
3.4.	use keys to move robot
4.	open new terminal
4.1.	roslaunch turtlebot3_slam turtlebot3_slam.launch
5.	drive around the room with keypad
6.	open new terminal 
6.1.	rosrun map_server map_saver -f ~/map
6.2.	~/map -> change to path were you want to save the map


# Code for simulation 

1.	Launch turtlehouse or turtleworld
2.	Launch Keypad -> look in description of real
3.	Run SLAM -> look in description of real
4.	Save map -> look in description of real

