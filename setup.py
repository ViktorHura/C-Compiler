from setuptools import find_packages, setup

setup(
    name='compiler-project',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'antlr4-python3-runtime',
        'pytest'
    ]
)