from setuptools import setup
import os
from glob import glob

package_name = 'py_obstacle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/**')),
        (os.path.join('share', package_name, 'models/box'), glob('models/box/**')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
    maintainer_email='ros2@test.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'follower = py_obstacle.line_follower:main',
            'box_spawn = py_obstacle.box_spawn:main',
            'box_delete = py_obstacle.box_delete:main',

        ],
    },
)
