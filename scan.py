import rospy
from nav_msgs.msg import Odometry
import tf.transformations as tftr
from sensor_msgs.msg import LaserScan
from numpy import pi, cos, sin
import matplotlib.pyplot as plt

cur_rot_z = 0
def scan_callback(msg):
    global ranges,dis_foward
    ranges = msg.ranges
    angle_increment = msg.angle_increment #*(180/pi)
    # print(angle_increment)
    dis_foward = ranges[359]
    # print(len(ranges))
    number_of_values = len(ranges) 
    step_size  = 360
    shown = False
    angle_counter = 0 
    print(angle_counter)
    x_l = []
    y_l = []

    for value in ranges:
        angle_counter+= angle_increment

     
        if type(value) == float:

            x_l.append(-1 * (value * sin(angle_counter)))
            y_l.append(value * cos(angle_counter))




            # if angle_counter <= 90:
            #     print(cur_rot_z)
            #     # print(f"value ={value}")
            #     # print(f"angle_counter ={angle_counter}")
            #     x_l.append(-1 * (value * sin(angle_counter*pi/180)))
            #     y_l.append(value * cos(angle_counter*pi/180))
            
            # elif angle_counter <= 180:
            #     x_l.append(-1 * (value * cos((angle_counter -90)*(pi/180))))
            #     y_l.append(-1*(value * sin((angle_counter- 90)*(pi/180))))
            
            # elif angle_counter <= 270:
            #     x_l.append( (value * sin((angle_counter -180) *pi/180)))
            #     y_l.append(-1*(value * cos((angle_counter-180)*pi/180 )))
            
            # elif angle_counter <= 360:
            #     x_l.append(value * cos((angle_counter-270) *pi/180))
            #     y_l.append(value * sin((angle_counter-270)*pi/180))
    if not shown:
        print(cur_rot_z)
        
        y_pos = 0
        x_pos = 0
        x_direct = 0
        y_direct = 1
        # if cur_rot_z > 0:
        #     x_direct = - sin(cur_rot_z)
        #     y_direct = cos(cur_rot_z)
 
        # elif cur_rot_z < 0:
        #     print(cur_rot_z)
        #     print(2 * pi + cur_rot_z)
        #     print(cos(2 * pi + cur_rot_z))
        #     print(- sin(2 * pi + cur_rot_z))
        #     x_direct = - sin(2 * pi + cur_rot_z)
        #     y_direct = - cos(2 * pi + cur_rot_z)



        # Creating plot
        fig, ax = plt.subplots(figsize = (12, 12))
        ax.quiver(x_pos, y_pos, x_direct, y_direct)
        ax.set_title('Map')
        plt.scatter(x_l,y_l)
        if not shown:
            plt.show()
            shown = True

def odometry_callback(msg):
    global cur_rot_z
    cur_position = msg.pose.pose.position
    cur_q = msg.pose.pose.orientation
    cur_rpy = tftr.euler_from_quaternion((cur_q.x, cur_q.y, cur_q.z, cur_q.w))  # roll pitch yaw
    cur_rot_z = cur_rpy[2]
    

            
        
        
        # print(value_x)
ranges = []
dis_foward = 0.0
#set sub,pub
rospy.init_node('object_detection')

scan_sub = rospy.Subscriber('/scan',LaserScan,scan_callback)
sub_odom = rospy.Subscriber("/odom", Odometry,odometry_callback)
#RATE = rospy.get_param('/rate', 50)
while not rospy.is_shutdown():
    pass