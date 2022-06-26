from setuptools import setup, find_packages


setup(
    name='yv_utils',
    version='0.8',
    license='MIT',
    author="Yerram Varun",
    author_email='yerram.varun@gmail.com',
    packages=find_packages('src', exclude=['.git', '.gitignore']),
    package_dir={'': 'src'},
    url='https://github.com/Varun221/yv_utils',
    keywords='utils package',
    install_requires=[
          'tqdm',
          'pandas'
      ],

)