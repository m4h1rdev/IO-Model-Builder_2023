from setuptools import setup

setup(
    name="IO Model Builder",
    version="1.2.2",
    author="Michael Srocka (Greendelta), Wesley Ingwersen (US Environmental Protection Agency)",
    author_email="ingwersen.wesley@epa.gov",
    description="iomb is a package for creating environmentally extended "
                "input-output models",
    license="CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    keywords=['economic input-output models','supply and use framework','EEIO','life cycle assessment','LCA','USEEIO'],
    url="https://github.com/USEPA/IO-Model-Builder",
    packages=['iomb'],
    package_data={'iomb': ["data/*.*"]},
    python_requires='>=3',
    install_requires=['numpy>=1.15', 'pandas>=1.3.4', 'matplotlib==3.1', 'flask==1.0.3'],
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.5",
        "Topic :: Utilities",
    ]
)
