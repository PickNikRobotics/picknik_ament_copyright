from setuptools import find_packages
from setuptools import setup

package_name = 'picknik_ament_copyright'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    package_data={'': [
        'template/*',
    ]},
    zip_safe=False,
    author='Joe Schornak',
    author_email='joseph.schornak@picknik.ai',
    maintainer='Joe Schornak',
    maintainer_email='joseph.schornak@picknik.ai',
    url='https://github.com/PickNikRobotics/picknik_ament_copyright',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD 3-Clause License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Check source files for PickNik-specific copyright reference.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'ament_copyright.copyright_name': [
            'picknik = picknik_ament_copyright.copyright_names:picknik',
        ],
        'ament_copyright.license': [
            'picknik_proprietary = picknik_ament_copyright.licenses:picknik_proprietary',
        ],
    },
)
