from setuptools import setup

setup(name='Restcomm_Python_SDk',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    #  https://packaging.python.org/en/latest/single_source_version.html

      version='1.3.1',
      description='Restcomm SDk for Python user',
      long_description='Restcomm_Python_SDk is a module for using the *Restcomm Rest API*. This Documentation provides the basic information on the usage of this SDk in performing various operations offered by the Restcomm-Rest APIs. The Restcomm REST API allows you to query meta-data about your account, phone numbers, calls, text messages, and recordings. You can also do some communications control like initiate outbound calls and send text messages.',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
    # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
    #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
    # Pick your license as you wish (should match "license" below)
        'License :: OSI Approved :: MIT License',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
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