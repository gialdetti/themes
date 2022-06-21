from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy", "pandas", "pyyaml"]

setup(
    name="themes",
    version="0.0.4",
    author="Eyal Gal",
    author_email="eyalgl@gmail.com",
    description="themes: style once, plot everywhere",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=[],
    url="https://github.com/gialdetti/themes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
    include_package_data=True,
    # package_data={'datasets': ['themes/resources/*']},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
