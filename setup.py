from setuptools import setup

setup(
    name='compliance_calC',
    version='0.1.0',    
    description='This code analyzes the crack closure during fatigue crack growth. '
                'Specifically it gives the Mean Opening Force at 2%'
                ' compliance offset according to E647 standard.',
    url='https://github.com/',
    author='Varun Nair',
    author_email='varunvnair1111@gmail.com',
    license='MIT',
    packages=['compliance_calculator'],
    install_requires=['matplotlib==3.7.4',
                      'numpy==1.24.4',
                      'pandas==2.0.3',
                      'scipy==1.10.1'                     
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research', 
        # 'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
    ],
)
