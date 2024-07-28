from setuptools import setup, find_packages

setup(
    name="my_project_tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            # 'your_script_name = your_module:main_function',
        ],
    },
)

