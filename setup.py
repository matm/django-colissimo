from setuptools import setup, find_packages

VERSION = (0, 5)

# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

version= str_version

setup(
    name = 'django-colissimo',
    version = version,
    description = "colissimo",
    long_description = """django-colissimo provides the ability to get prices from the La Poste Colissimo postal service.""",
    author = 'Mathias Monnerville',
    author_email = 'mathias@monnerville.com',
	url = 'https://bitbucket.org/matm/django-colissimo',
    license = 'GPL 3',
    platforms = ['any'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
				   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
    packages = find_packages(),
    setup_requires=["setuptools_hg"],
    include_package_data = True,
)

