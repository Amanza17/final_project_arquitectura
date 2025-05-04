from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'video_port', default_value='2',
            description='Video port of the camera'
        ),
        DeclareLaunchArgument(
            'fps', default_value='60',
            description='Frames per second'
        ),
        DeclareLaunchArgument(
            'image_width', default_value='1280',
            description='Image width'
        ),
        DeclareLaunchArgument(
            'image_height', default_value='480',
            description='Image height'
        ),
        DeclareLaunchArgument(
            'vis_raw_cam_img', default_value='false',
            description='Visualize raw image of camera'
        ),
        DeclareLaunchArgument(
            'vis_rect_img_overlay', default_value='false',
            description='Visualize overlay of rectified image'
        ),
        DeclareLaunchArgument(
            'publish_raw_images', default_value='false',
            description='Publish raw images'
        ),
        DeclareLaunchArgument(
            'publish_rectified_images', default_value='true',
            description='Publish rect images'
        ),
        DeclareLaunchArgument(
            'left_camera_info_url',
            default_value='package://elp_stereo_camera/cam_params/1280_480/left_camera.yaml',
            description='Left camera info URL'
        ),
        DeclareLaunchArgument(
            'right_camera_info_url',
            default_value='package://elp_stereo_camera/cam_params/1280_480/right_camera.yaml',
            description='Right camera info URL'
        ),
        DeclareLaunchArgument(
            'minimize_motion_blur', default_value='true',
            description='Trick to minimize motion blur for rolling shutter cameras'
        ),

        Node(
            package='elp_stereo_camera',
            executable='stereo_camera_node',
            name='stereo_camera_node',
            output='screen',
            parameters=[{
                'video_port': LaunchConfiguration('video_port'),
                'fps': LaunchConfiguration('fps'),
                'image_width': LaunchConfiguration('image_width'),
                'image_height': LaunchConfiguration('image_height'),
                'vis_raw_cam_img': LaunchConfiguration('vis_raw_cam_img'),
                'vis_rect_img_overlay': LaunchConfiguration('vis_rect_img_overlay'),
                'publish_raw_images': LaunchConfiguration('publish_raw_images'),
                'publish_rectified_images': LaunchConfiguration('publish_rectified_images'),
                'left_camera_info_url': LaunchConfiguration('left_camera_info_url'),
                'right_camera_info_url': LaunchConfiguration('right_camera_info_url'),
                'minimize_motion_blur': LaunchConfiguration('minimize_motion_blur'),
            }]
        ),

        Node(
            package='elp_stereo_camera',
            executable='stereo_point_cloud_generator',
            name='stereo_point_cloud_generator',
        ),

        Node(
            package='elp_stereo_camera',
            executable='tf',
            name='tf',
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='camera_link_to_camera_optical_link',
            arguments=[
                '0', '0', '0',
                '-1.5707963267948966', '0', '-1.5707963267948966',
                'camera_link', 'camera_optical_link'
            ]
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='camera_optical_link_to_left_camera',
            arguments=[
                '0', '0', '0',
                '0', '0', '0',
                'camera_optical_link', 'left_camera'
            ]
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='camera_optical_link_to_right_camera',
            arguments=[
                '0.06', '0', '0',
                '0', '0', '0',
                'camera_optical_link', 'right_camera'
            ]
        )
    ])
