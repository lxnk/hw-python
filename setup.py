from setuptools import setup, find_packages


setup(
    name='hw-python',
    version='0.1.1',
    package_dir = {"": "src"},
    # packages=['pylloworld'],
    url='https://github.com/lxnk/hw-python',
    license='MIT',
    author='OK',
    author_email='o.kashuba@gmail.com',
    description='Hello world with entry point',
    python_requires = ">=3.9",
    entry_points={  # Optional
        "console_scripts": [
            "pyllo-world=pylloworld:print_hi",
        ],
    }
)
