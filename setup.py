import setuptools

setuptools.setup(
    name="coiiot_sdk",
    version="0.0.1",
    author="VK",
    author_email="",
    description="SDK для разработки правил IoT",
    url="https://github.com/vk-cs/iot-python-rules-engine-sdk",
    packages=setuptools.find_packages(include="coiiot_sdk.*"),
    install_requires=[
        "click==8.0.4",
        "requests==2.27.1",
        "pyyaml==6.0",
    ],
    entry_points ={
        "console_scripts": [
            "coiiot-cli = coiiot_sdk.cli:cli"
        ]
    },
    python_requires=">=3.7",
)
