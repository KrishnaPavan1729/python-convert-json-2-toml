from setuptools import setup, find_packages

setup(
    name="json2toml",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ujson==5.4.0",
        "tomlkit==0.11.6",
        "chardet==4.0.0",
        "loguru==0.6.0",
        "pydantic==1.10.2",
    ],
    entry_points={
        "console_scripts": [
            "json2toml=json2toml.main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A personal project demonstrating JSON to TOML conversion skills",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/json2toml",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
