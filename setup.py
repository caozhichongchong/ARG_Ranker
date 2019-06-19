from setuptools import setup

setup(
    name="arg_ranker",
    packages=['arg_ranker'],
    version="1.0.5",
    description="Ranking the risk of antibiotic resistance for metagenomes",
    author='Anni Zhang',
    author_email='anniz44@mit.edu',
    url='https://github.com/caozhichongchong/ARG_Ranker',
    keywords=['antibiotic resistance', 'risk', 'one health', 'clinical AMR', 'mobile AMR'],
    license='MIT',
    #install_requires=['python>=3.0'],
    include_package_data=True,
    long_description=open('README.md').read(),
    package_dir={'arg_ranker': 'arg_ranker'},
    package_data={'arg_ranker': ['data/*','bin/*']},
    entry_points={'console_scripts': ['arg_ranker = arg_ranker.__main__:main']},
    #zip_safe=False,
    #setup_requires=['pytest-runner'],
    #tests_require=['pytest'],
    classifiers=[
        #'Development Status :: 1 - Alpha',
        #'Intended Audience :: Bioinformatics and Researchers',
        #'License :: MIT',
        #'Operating System :: MacOS',
        #'Operating System :: Microsoft :: Windows',
        #'Operating System :: LINUX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Topic :: Antibiotic resistance :: risk ranking',
        #'Topic :: Metagenomes :: Antibiotic resistance',
    ]
)
