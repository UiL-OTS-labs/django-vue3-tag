import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-vue3-tag",
    version="0.0.1",
    author="UiL OTS Labs",
    author_email="labbeheer.gw@uu.nl",
    description="Makes it easier to use Vue3 components in Django templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UiL-OTS-labs/django-vue3-tag",
    packages=setuptools.find_packages(),
    package_data=dict(ageutil=['py.typed']),
    license_files=('LICENSE',),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
