from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Restcomm_Python_SDk',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    #  https://packaging.python.org/en/latest/single_source_version.html

      version='1.2.1a2',
      description='Restcomm SDk for Python user',
      long_description=readme(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
    # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
    #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
    # Pick your license as you wish (should match "license" below)
        'License :: OSI Approved :: MIT License',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
      ],

    # What does your project relate to?

      keywords='Restcomm SDk for python',
    # The project's main homepage.
      url='https://github.com/mdsharique/restcomm-sdk-python',
    # Author details
      author='MD Sharique',
      author_email='nukles1.07@gmail.com',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.

      packages=['Restcomm_Python_SDk'],
      install_requires=[
          'requests', 'vcr',
      ],
      include_package_data=True,
      zip_safe=False)