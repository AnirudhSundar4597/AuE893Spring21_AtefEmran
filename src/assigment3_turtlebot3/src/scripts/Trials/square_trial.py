#!/usr/bin/env python3
import rospy
from geometry_msgs.msg  import Twist
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt
pi=22/7
corner=pi/2

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.callback)
        self.pose = Odometry()
        self.rate = rospy.Rate(10)

    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.pose.pose.position.x = round(self.pose.pose.pose.position.x, 4)
        self.pose.pose.pose.position.y = round(self.pose.pose.pose.position.y, 4)

    def move2goal(self):

#Variables definition ################################################################################################
        goal_pose = Odometry()
        vel_msg = Twist()

#YOUR INPUT ###########################################################################################################

        speed_linear=0.3
        speed_angular=0.3
        member_length=2

        first_x=2
        first_y=0
        first_angle=0

        second_x=2
        second_y=2

        third_x=0
        third_y=2

        angle_tolerance = 0.0001

        angle_diff=0.05  #intial value

        print("Let's draw a square")

#Going to the  first targets ################################################################################################
        goal_pose.pose.pose.position.x = first_x
        goal_pose.pose.pose.position.y = first_y
        goal_angle = first_angle

        #we should start with 0 angle
        angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)

        while(abs(angle_diff) > angle_tolerance):
            vel_msg.angular.z = (angle_diff/abs(angle_diff))*speed_angular   #Normalizing the differnce and getting the opposit angle
            #publish the velocity
            self.velocity_publisher.publish(vel_msg)
            #calculating the angle
            angle_diff = (goal_angle - self.pose.pose.pose.orientation.z)
            self.rate.sleep()


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        print("Finished first orientation")

        #Setting the current time for distance calculations
        t0 = float(rospy.Time.now().to_sec())
        current_distance=0

        while (current_distance<member_length):
            #linear velocity
            vel_msg.linear.x = speed_linear
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= speed_linear*(t1-t0)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

        print("ARRIVED the 1st Goooooal!")

#Going to the  Second targets ################################################################################################
        goal_pose.pose.pose.position.x = second_x
        goal_pose.pose.pose.position.y = second_y

        #we should start with 0 angle
        t0 = float(rospy.Time.now().to_sec())
        current_angle=0

        while(current_angle <= corner):
            vel_msg.angular.z = speed_angular   #Normalizing the differnce and getting the opposit angle
            #publish the velocity
            self.velocity_publisher.publish(vel_msg)
            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_angle= speed_angular*(t1-t0)
            #calculating the angle


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        print("Finished second orientation")

        #Setting the current time for distance calculations
        t0 = float(rospy.Time.now().to_sec())
        current_distance=0

        while (current_distance<member_length):
            #linear velocity
            vel_msg.linear.x = speed_linear
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= speed_linear*(t1-t0)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        print("ARRIVED the 2nd Goooooal!")

#Going to the  Second targets ################################################################################################
        goal_pose.pose.pose.position.x = second_x
        goal_pose.pose.pose.position.y = second_y

        #we should start with 0 angle
        t0 = float(rospy.Time.now().to_sec())
        current_angle=0

        while(current_angle <= corner):
            vel_msg.angular.z = speed_angular   #Normalizing the differnce and getting the opposit angle
            #publish the velocity
            self.velocity_publisher.publish(vel_msg)
            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_angle= speed_angular*(t1-t0)
            #calculating the angle
            self.rate.sleep()


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        print("Finished second orientation")

        #Setting the current time for distance calculations
        t0 = float(rospy.Time.now().to_sec())
        current_distance=0

        while (current_distance<member_length):
            #linear velocity
            vel_msg.linear.x = speed_linear
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            t1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= speed_linear*(t1-t0)

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        #Stoping
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        self.rate.sleep()

        print("ARRIVED the 2nd Goooooal!")



if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass