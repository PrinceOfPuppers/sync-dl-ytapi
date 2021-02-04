import setuptools

with open('README.md', 'r') as f:
    longDescription = f.read()

setuptools.setup(
    name="sync-dl-ytapi",
    version="0.1.1",
    author="Joshua McPherson",
    author_email="joshuamcpherson5@gmail.com",
    description="An addon for sync-dl, providing commands which utilize the youtube api",
    long_description = longDescription,
    long_description_content_type = 'text/markdown',
    url="https://github.com/PrinceOfPuppers/sync-dl-ytapi",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['sync-dl','requests','google-auth','google-auth-oauthlib','google-api-python-client','cryptography'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
    ],
    python_requires='>=3.6',
)