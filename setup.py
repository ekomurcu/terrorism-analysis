import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cs210-project2-ekomurcu',
    version='0.0.1',
    author=[
        "Ali Yasin Akalın",
        "Bilge Bahadır Berber",
        "Berkay Ersever",
        "Egemen Yiğit Kömürcü"
    ],
    author_email=[
        "ayasinakalin@sabanciuniv.edu",
        "bbahadir@sabanciuniv.edu",
        "berkayersever@sabanciuniv.edu",
        "ekomurcu@sabanciuniv.edu"
    ],
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ekomurcu/Data-Analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        # List of every classifier: https://pypi.org/classifiers/
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ]
)
