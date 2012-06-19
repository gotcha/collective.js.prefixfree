from setuptools import setup, find_packages
version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.js.prefixfree',
      version=version,
      description="Lea Verou -prefix-free for Plone",
      long_description=long_description,
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Godefroid Chapelle',
      author_email='gotcha@bubblenet.be',
      url='https://github.com/gotcha/collective.js.prefixfree',
      license='mit',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.GenericSetup',
          'plone.theme',
      ],
      extras_require=dict(
          test=[
          'plone.app.testing',
          ],
          robot=[
          'plone.act',
          ]),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
