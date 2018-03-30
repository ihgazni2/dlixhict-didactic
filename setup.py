from setuptools import setup, find_packages
setup(
      name="xdict",
      version = "0.94.44",
      description="tools for transform between html,dict and cmdline",
      author="dapeli",
      url="https://github.com/ihgazni2/dlixhict-didactic",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/dlixhict-didactic",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['xdict'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

