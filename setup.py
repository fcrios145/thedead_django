from setuptools import setup

setup(name='TheDead',
      version='1.0',
      description='Noticias acerca del juego The Dead Ate My Friends',
      author='fcrios',
      author_email='fcrios145@hotmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=open('%s/requirements.txt' % os.environ.get('OPENSHIFT_REPO_DIR', PROJECT_ROOT)).readlines(),
     )
