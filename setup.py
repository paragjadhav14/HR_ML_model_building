from setuptools import find_packages, setup

with open("./reponame/__init__.py", "r") as fp:
    file_lines = fp.readlines()

for line in file_lines:
    if '__version__' in line:
        split = line.split('"') if '"' in line else line.split("'")
        version = split[1]


setup(
    name='reponame',
    version=version,
    description='Describe what reponame does',
    author="healthrhythms",
    url='https://github.com/healthrhythms/reponame',
    install_requires=open("req.txt").read().strip().split("\n"),  # noqa: SIM115
    license='LICENSE.txt',
    packages=find_packages(),
    include_package_data=True,
)
