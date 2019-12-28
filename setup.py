from setuptools import setup, find_packages
setup(
      name="xdict",
      version = "1.1.10",
      description="tools for transform between html,dict and cmdline",
      author="dapeli",
      url="https://github.com/ihgazni2/dlixhict-didactic",
      author_email='terryinzaghi@163.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/dlixhict-didactic",
      entry_points = {
         'console_scripts': [
                                'ide_apis_from_verb=xdict.bin.creat_apis_from_verb:main',
                                'ide_apis_from_strblk=xdict.bin.creat_apis_from_strblk:main',
                                'ide_indent=xdict.bin.ide_indent:main',
                                'pobj=xdict.bin.pobj:main',
                                'hentry=xdict.bin.hentry:main',
                                'jsonq=xdict.bin.jsonq:main'
                            ]
      },
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

