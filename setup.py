from setuptools import setup, find_packages

with open('README.md') as f:
	long_description = f.read()

setup(
	name='climmands',
	version='0.0.2',
	author='Eryk Andrzejewski',
	author_email='erykandrzejewski@gmail.com',
	description='A small cli command helper package',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/qwercik/climmands',
	packages=find_packages(),
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires='>=3.6',
)

