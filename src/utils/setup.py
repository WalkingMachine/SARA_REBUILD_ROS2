from setuptools import setup

package_name = 'utils'
roboteq_package = 'utils/PyRoboteq'
controller_package = 'utils/remote_controller'
setup(
    name=package_name,
    version='0.0.0',
    packages=[
        package_name,
        controller_package,
        roboteq_package,
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nimai Jariwala',
    maintainer_email='nimai.jariwala.1@ens.etsmtl.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
