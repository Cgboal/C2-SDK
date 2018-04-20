from setuptools import setup, find_packages

setup(name="c2sdk",
      version="0.0.1",
      description="Command and Control Framework Software Development Kit",
      url="https://git.veldt.me/cgboal/C2-Framework",
      author="Calum Boal",
      author_email="cgboal@protonmail.com",
      license="MIT",
      packages=find_packages(),
      install_requires=[
          'urllib3',
      ],
      )