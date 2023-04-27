<div align="center">
  <h1 align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
    <br>README-AI</h1>

> <h3 align="center">🚀 Generate aesthetic, structured, and informative README.md files </h3>
> <h3 align="center">⚙️ Powered by OpenAI's language model API and the software below</h3>
>  <p align="center">
>   <img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="Markdown" />
>   <img src="https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white" alt="OpenAI" />
>   <img src="https://img.shields.io/badge/Pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
>   <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
>   <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="pytest" />
>   <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="Bash" />
>   <img src="https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white" alt="Anaconda" />
> </p>

</div>

---

## 📍 Table of Contents

- [📍 Table of Contents](#-table-of-contents)
- [🤖 Overview](#-overview)
- [🔮 Features](#-features)
- [🚀 Getting Started](#-getting-started)
  - [✅ Dependencies](#-dependencies)
    - [📂 GitHub Repository](#-github-repository)
    - [🔐 OpenAI API Setup](#-openai-api-setup)
  - [💻 Installation](#-installation)
  - [🪄 Using README-AI](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🤖 Overview

README-AI is a powerful command-line tool that automates the creation of README.md files and generates comprehensive codebase documentation. This tool is designed to create visually appealing, well-structured, and informative README files for your codebase, making it easy for analysts, developers, and teams of **_all levels_** to produce baseline codebase documentation quickly.

> **Note:**
>
> This project is currently under development and has an opinionated configuration and setup. While README-AI provides an excellent starting point for any project that requires documentation, it is important to review all text that is generated by the OpenAI API to ensure that it accurately represents your codebase.

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🔮 Features

<h1 align="center">1.<br>👇<br><br>🔖 Codebase Documentation</h1>
<p align="center">Have you ever met anyone who enjoyed writing documentation for their project? That’s why we're building this project, enjoy!
</p>

|                                                                                                                                                                                                                                                                                        |                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| <br><br/><b>📍 Codebase Documentation</b><br><br>Codebase documentation is generated by the <br>OpenAI API `text-davinci-003` model engine.<br> Each file in your repository is converted to<br> natural language, grouped by directory, and visualized in tables in your README file. | ![docs](docs/imgs/docs.png) |

<h1 align="center">⒉<br>👇<br><br>🪪 Badges</h1>
<p align="center">OpenAI generated introduction sentence and beautiful project badges displayed in the top section of the README.
</p>

|                                                                                                                                                         |                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Introduction and Badges</b><br><br>The introduction sentence is generated by<br> `text-davinci-003` and dependencies are displayed with project badges! | ![header](docs/imgs/header.png) |

<h1 align="center">⒊<br>👇<br><br>🌲 Repository Tree</h1>
<p align="center">Why not a directory tree as well? Visualize your codebase structure in your README. 
</p>

|                             |     |
| --------------------------- | --- |
| ![tree](docs/imgs/tree.png) | 

<h1 align="center">⒋<br>👇<br><br>📚 Table of Contents and Overview</h1>
<p align="center">Adds a table of contents, introduction, and features sections.
</p>

|                                                                                                                                                                                         |                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| <br><br/><b>📍 Table of Contents, Overview, & Features</b><br><br>Builds table of contents, overview, and <br>features sections. The Overview summary is generated by the OpenAI model. | ![toc](docs/imgs/toc.png) |

<h1 align="center">⒌<br>👇<br><br>📦 Project Setup and User Guide</h1>
<p align="center">Creates instructions for setting up and using your codebase. Working on a more dynamic implementation of this section!</p>

|                                                                                                                                                                                               |                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| <br><br/><b>📍 Getting Started </b><br><br>Dynamically creates a setup guide for<br> others can use your project! Sections include dependencies, installation, and usage, and tests.<br><br>Currently works for Python, Rust, JavaScript.<br> | ![setup](docs/imgs/setup.png) |

<h1 align="center">⒍<br>👇<br><br>👩‍💻Contributing Guidelines & more!</h1>
<p align="center">Adds three additional sections to build out a complete README file!</p>

|                             |     |
| --------------------------- | --- |
| ![tree](docs/imgs/misc.png) |                       
                        
<h1 align="center">⒎<br>👇<br><br>💥 Example Files</h1>
<p align="center">Markdown example files produced by the README-AI app!</p>
<div align="center">
  <table align="center">
    <tr>
      <th></th>
      <th>File</th>
      <th>GitHub</th>
      <th>Bytes</th>
    </tr>
    <tr>
      <td>1️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_1.md">README_1_PY.md</a></td>
      <td><a href="https://github.com/eli64s/readme-ai">readme-ai</a></td>
      <td><p>15459624</p>
    </tr>
    <tr>
      <td>2️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_2.md">README_2_PY.md</a></td>
      <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
      <td><p>8698890</p>
    </tr>
    <tr>
      <td>3️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_JS.md">README_3_JS.md</a></td>
      <td><a href="https://github.com/philnash/react-web-audio">react-web-audio</a></td>
      <td><p>533233</p>
    </tr>
    <tr>
      <td>4️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_RUST.md">README_4_RUST.md</a></td>
      <td><a href="https://github.com/MihaiBogdanEugen/contacts-cli">rust-contacts-cli</a></td>
      <td><p>79104</p>
    </tr>
    <tr>
      <td>5️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_EX_3.md">README_5_FastAPI.md</a></td>
      <td><a href="https://github.com/nofoobar/JobBoard-Fastapi">job-board-fastapi</a></td>
      <td><p>75391521</p>
    </tr>
  </table>
</div>

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🚀 Getting Started

### ✅ Dependencies

Before you begin, ensure that you have the following prerequisites installed:

- Python 3.6 or higher
- Conda package manager (recommended)
- Access to the OpenAI API (see OpenAI API Setup below)

#### 📂 GitHub Repository

Copy the url of your project's GitHub repository and update the [configuration file](https://github.com/eli64s/README-AI/conf/conf.toml) as seen in the code snippet below. Additionally, you can provide a local path to your repository if you are not using GitHub.

```toml
[github]
local = "INSERT-LOCAL-REPO-PATH"
remote = "INSERT-GITHUB-REPO-URL"
```

#### 🔐 OpenAI API Setup

To use README-AI, you will need an API key for OpenAI. Follow the steps below to create an API key:

<details closed>
<summary>User Guide - OpenAI API</summary>

1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>

### 💻 Installation

1. Clone the README-AI repository:

```sh
git clone https://github.com/eli64s/README-AI.git && cd README-AI
```

2. Create a Conda environment and install the required dependencies:

```sh
# With Bash
bash setup/setup.sh

# With Conda
conda env create -f setup/environment.yaml
conda activate readmeai
pip install -r requirements.txt
```

3. Set up the OpenAI API key by creating an environment variable:

```sh
export OPENAI_API_KEY=<your-api-key>
```

### 🪄 Using README-AI

Use the command-line to provide the OpenAI API key (if not already set) and specify an output path for your README file.

Options:

- `-k, --api_key`: Provide your OpenAI API key.
- `-l, --local`: Provide a local repository directory path.
- `-o, --output`: Provide an output file path.
- `-r, --remote`: Provide a GitHub remote repository url.

```sh
python src/main.py -k your_api_key -o docs/README_EX.md -r https://github.com/eli64s/readme-ai
```

Alternatively, run the bash script to run README-AI with the default configuration.

```sh
bash scripts/run_main.sh
```

### 🧪 Running Tests

To run the unit-tests for README-AI, use the following command.

```basg
bash scripts/test.sh
```

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🛠 Future Development

- [x] Add compatibility for additional languages (current - Python, Rust, JavaScript).
- [ ] Add user interface to generate README files.
- [ ] Add the ability to choose the language of the generated README file
- [ ] Implement different configuration README template styles.

---

## 🤝 Contributing

Contributions are welcomed and encouraged! Please follow these steps in the [Contributing Guidelines](https://github.com/eli64s/README-AI/CONTRIBUTING.md), thank you!

---

## 🪪 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/eli64s/README-AI/LICENSE.md) file for details.

---

## 🙏 Acknowledgments

- Badge Icons: [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---
