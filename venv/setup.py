import setuptools
# read in required packages from requirements.txt
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="The_Mastermind",
    version="0.0.0",
    author='Katharina Melchart',
    author_email='katharina.melchart@gmx.at',
    description='A vault for secret lists',
    long_description='''This package is currently under development. Stay tuned for updates.''',
    url="https://github.com/Neo2460/The_Mastermind",
    license='BSD',
    keywords='encoding,secret,lists,...',
    packages=setuptools.find_packages(),
    package_data={'The_Mastermind': ['']},
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: -',
        'Topic :: Encrypting :: Decrypting',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',],
    install_requires=requirements,
    include_package_data=True
)
