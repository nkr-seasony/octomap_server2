#!/usr/bin/env python

import os.path as osp

from launch import LaunchDescription, logging
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import \
    PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import ThisLaunchFileDir

#'frame_id': 'odom',
def generate_launch_description():

    params = {'resolution': 0.02,
               'use_sim_time':True,
              'frame_id': 'base_link',
              #'base_frame_id': 'base_link',
              'height_map': True,
              'colored_map': True,
              'latch': False,
              'color_factor': 0.8,
              'filter_ground': False,
              'filter_speckles': False,
              'ground_filter/distance': 0.04,
              'ground_filter/angle': 0.15,
              'ground_filter/plane_distance': 0.07,
              'compress_map': True,
              'incremental_2D_projection': False,
              'sensor_model/max_range':20.0,
              'sensor_model/hit': 0.7,
              'sensor_model/miss': 0.3,
              'sensor_model/min': 0.1,
              'sensor_model/max': 0.99,
              #'sensor_model/max': 0.99,
              'color/r': 0.0,
              'color/g': 0.0,
              'color/b': 1.0,
              'color/a': 1.0,
              'color_free/r': 0.0,
              'color_free/g': 0.0,
              'color_free/b': 1.0,
              'color_free/a': 1.0,
              'publish_free_space': True,
             #'OccupancyThres':0.5,
            
    }
    
    remap = [('cloud_in', '/lewis/local_cloud'),
             ('projected_map', '/lewis/projected_map')]
    node = Node(package='octomap_server2',
                 executable='octomap_server',
                 output='screen',
                 remappings=remap,
                 parameters=[params])
    return LaunchDescription([node])
