import setuptools

setuptools.setup(
    name="coiiot_sdk",
    version="0.0.1",
    author="VK",
    author_email="",
    description="SDK for developing IoT rules",
    url="https://github.com/vk-cs/iot-python-rules-engine-sdk",
    packages=setuptools.find_packages(include="coiiot_sdk.*"),
    install_requires=[],
    entry_points ={},
    python_requires=">=3.7",
)
