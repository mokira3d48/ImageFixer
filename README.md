# Image Fixer
![](https://img.shields.io/badge/Python-3.8-blue)
![](https://img.shields.io/badge/LICENSE-MIT-%2300557f)
![](https://img.shields.io/badge/lastest-2025--02--27-green)
![](https://img.shields.io/badge/contact-dr.mokira%40gmail.com-blueviolet)

Clonable referential to initialize this project with the best practice.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
  - [For Linux](#for-linux)
  - [For Windows](#for-windows)
- [Usage](#uage)
- [Features](#features)
- [Tests](#tests)
- [To contribute](#to-contribute)
- [Licence](#licence)
- [Contact](#contact)


## Description

Image Fixer is a simple application that allows users to clean a corrupted
image.

## Installation

To install the project, make sure you have Python 3.8 or later version
and `pip` installed on your machine. And then run the following command lines.

### For Linux

```bash
git clone git@github.com:mokira3d48/ImageFixer.git image_fixer
cd image_fixer
sudo rm -r .git
git init
```

And then,

1. `sudo apt install cmake python3-venv` Install *Cmake* and *Virtual env*;
2. `make venv` or `python3 -m venv env` create a virtual env into directory
named `env`;
3. `source env/bin/activate` activate the virtual environment named `env`;
4. `make install` install the requirements of this package;
5. `make dev` install the package in dev mode in virtual environment;
6. `make test` run the unit test scripts located at `tests` directory;
7. `make run` run script located at `src/imfix/__main__.py`.
8. Or Run `imfix` as a command line to run `src/imfix/__main__.py`.

### For Windows

```bash
git clone git@github.com:mokira3d48/ImageFixer.git image_fixer
cd image_fixer
```

And then, delete the hidden directory named `.git` located at the root
of the directory project.

And then,

1. Install python for windows;
2. Open your command prompt;
3. Run `python3 -m venv env` to create a virtual env into directory
named `env`;
4. Run `pip install -r requirements` to install the requirements
of this package or project;
5. Run `pip install -e .` install the package in dev mode in virtual
environment;
6. Run `python3 -m image_fixer` to run main script located
at `src/image_fixer/__main__.py`. Or Run `imfix` as a command line
to run `src/image_fixer/__main__.py` and start the application.


---

## Usage

Here is an example how to clean an image or all image contained on a directory:

```shell
imfix path/to/image path/to/target/directory
# or
imfix path/to/images/directory path/to/target/directory
```

## Features
Allow to clean a corrupted image.

## Tests

To execute the unittest, make sure you have `pytest` package installed,
and then run the following command line:

```bash
make test 
```
or

```shell
pytest
```

---

## To contribute

Contributions are welcome! Please follow these steps:

1. Create a new branch for your feature (`git checkout -b feature/my-feature`);
2. Commit your changes (`git commit -m 'Adding a new feature'`);
3. Push toward the branch (`git push origin feature/my-feature`);
4. Create a new *Pull Request* or *Merge Request*.

## Licence

This project is licensed under the MIT License. See the file [LICENSE](LICENSE)
for more details, contact me please.

## Contact

For your question or suggestion, contact me please :

- **Name** : Arnold Mokira
- **Email** : dr.mokira@gmail.com
- **GitHub** : [mokira3d48](https://github.com/mokira3d48)

