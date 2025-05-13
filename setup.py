from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='iot_simulator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'iot-sim=iot_simulator.main:main',
        ],
    },
    author='Deepthi Deepthi',
    description='An IoT device simulator that publishes MQTT metrics',
    python_requires='>=3.7',
)
