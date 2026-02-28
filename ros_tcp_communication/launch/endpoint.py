from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ros_tcp_endpoint",
                executable="default_server_endpoint",
                emulate_tty=True,
                parameters=[{"ROS_IP": "192.168.1.23"}, {"ROS_TCP_PORT": 10000}],
            ),
            Node(
                package="topic_tools",
                executable="relay",
                name="right_hand_pose_relay",
                arguments=[
                    "/q2r_right_hand_pose",
                    "/q2r_right_arm_hand_pose",
                ],
                output="screen",
            ),
             Node(
                package="topic_tools",
                executable="relay",
                name="right_hand_inputs_relay",
                arguments=[
                    "/q2r_right_hand_inputs",
                    "/q2r_right_arm_hand_inputs",
                ],
                output="screen",
            ),
            Node(
                package="topic_tools",
                executable="relay",
                name="left_hand_pose_relay",
                arguments=[
                    "/q2r_left_hand_pose",
                    "/q2r_left_arm_hand_pose",
                ],
                output="screen",
            ),
            Node(
                package="topic_tools",
                executable="relay",
                name="left_hand_inputs_relay",
                arguments=[
                    "/q2r_left_hand_inputs",
                    "/q2r_left_arm_hand_inputs",
                ],
                output="screen",
            ),

        ]
    )
