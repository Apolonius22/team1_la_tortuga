######################## imports ########################################
import rospy
from sensor_msgs.msg import LaserScan
from numpy import cos, sin
import matplotlib.pyplot as plt



######################## class definition ########################################
class Scan:

    def __init__(self):

        # saves variables from LIDAR
        self.ranges = [] 

        # saves points from LIDAR converted to X/Y Coordinates
        self.x_l = []
        self.y_l = []

        # initialie ROS Stuff
        rospy.init_node('object_detection')
        scan_sub = rospy.Subscriber('/scan',LaserScan,self.scan_callback)


    def scan_callback(self,msg):

        # get Values from LaserScan Topic
        self.ranges = msg.ranges

        # get angle_increment from LaserScan Topic
        angle_increment = msg.angle_increment 
        
        # initialize counter
        angle_counter = 0 
        
        # empty X/Y Lists 
        self.x_l = []
        self.y_l = []

        # Loop through LIDAR Values, convert to X/Y Coordinates and save in List
        for value in self.ranges:
            angle_counter += angle_increment  
            if type(value) == float:
                self.x_l.append(-1 * (value * sin(angle_counter)))
                self.y_l.append(value * cos(angle_counter))
            else:
                pass

        

    def main(self):

        while not rospy.is_shutdown():

            # set marker were the robot is
            plt.quiver(0, 0, 0, 1)
            # scatter - plot points (those get updated in scan_callback method)
            plt.scatter(self.x_l,self.y_l)
            # show and pause
            plt.draw()
            plt.pause(0.1)
            # clear all points 
            plt.clf()

    
if __name__ == "__main__":

    # Init Objects and start main Methode 
    task1 = Scan()
    task1.main()

