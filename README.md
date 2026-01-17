<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="https://github.com/user-attachments/assets/e218a6b9-fb46-4ce1-a27f-3218953e1e94" width="100%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# <code>❯ Password Generator</code>

<em></em>

<!-- BADGES -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
---

## Overview

This project is a command-line password generator written in Python:

- Users run the script to output a randomly generated password.


---

## Features

- Command-Line Password Generation
    - Generates passwords directly from the terminal using a specified length.

- Custom Password Length
    - Users define the password length via a command-line argument.

- Mixed Character Sets
    - Passwords are generated using:
    - Lowercase letters
    - Uppercase letters
    - Numbers
    - Special symbols

- Randomized Character Selection
    - Each character in the password is randomly selected from one of the available character categories.

- Colored Terminal Output
    - Uses colorama to display:
        - ASCII banner in color
        - Password output highlighted for readability
        - Clear visual separators

- ASCII Art Banner
    - Displays a stylized ASCII header when the tool starts.

- Input Validation
    - Displays a syntax message if the password length is not provided.

- Graceful Exit Handling
    - Safely handles Ctrl + C interruptions and unexpected errors.

- Lightweight & Fast
    - Minimal dependencies and quick execution.

---

## Project Structure

```sh
└── /
    ├── README.md
    ├── pass_generator.py
    └── requirements.txt
```

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### Installation

Build  from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/JZBOSS3/password_generator.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd password_generator
    ```

3. **Install the dependencies:**

	```sh
	❯ pip install -r requirements.txt
	```

### Usage

Run the project with:

```sh
python pass_generator.py
```

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
