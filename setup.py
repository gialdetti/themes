from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

base_packages = ["numpy", "pandas", "pyyaml"]
altair_packages = ["altair"]
test_packages = ["pytest", "ipython", "tox"]
docs_packages = ["black>=24.3.0"]
dev_packages = (
    ["matplotlib", "seaborn", "notebook", "ipywidgets"]
    + altair_packages
    + docs_packages
    + test_packages
)

setup(
    name="themes",
    version="0.0.5",
    author="Eyal Gal",
    author_email="eyalgl@gmail.com",
    description="themes: style once, plot everywhere",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords=[],
    url="https://github.com/gialdetti/themes",
    packages=find_packages(),
    install_requires=base_packages,
    extras_require={
        "test": test_packages,
        "docs": docs_packages,
        "dev": dev_packages,
    },
    python_requires=">=3.7",
    include_package_data=True,
    # package_data={'datasets': ['themes/resources/*']},
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
