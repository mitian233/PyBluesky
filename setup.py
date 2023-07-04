from setuptools import setup, find_packages

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name='PyBluesky',
    version='0.0.2',
    author='Mitian233',
    author_email='kasumi@bangdream.moe',
    description='Bluesky.Social AT Protocol API Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mitian233/pybluesky',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'requests',
    ],
)
