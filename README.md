<div align="center">
  <h1 align="center">
    <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="80"/>
    <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="80"/>
    <br>
    README-AI
  </h1>

> <h3 align="center">🚀 Generate beautiful and informative README Markdown files!</h3>
> <h3 align="center">⚙️ Powered by OpenAI's language model APIs and the tools below:</h3>
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
    - [📂 Repository](#-repository)
    - [🔐 OpenAI API Setup](#-openai-api-setup)
  - [💻 Installation](#-installation)
  - [🎮 Using README-AI](#-using-readme-ai)
  - [🧪 Running Tests](#-running-tests)
- [🛠 Future Development](#-future-development)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---

## 🤖 Overview

README-AI is a powerful, user-friendly tool that generates extensive README markdown documents for your software and data projects. By simply providing a remote repository URL or directory path to your codebase, this tool will generate documention for your entire project, harnessing the capabilities of large language models via OpenAI's GPT APIs.

README-AI simplifies the process of writing and maintaining high-quality project documentation. My aim for this project is to provide a tool that supports developers, making software development more efficient and user-friendly. Ultimately, the goal of README-AI is to improve the adoption rate and usability of open-source projects, helping all skill levels better understand and use codebases, and allowing everyone to focus on tasks that matter most to you!

> ⚠️ **Note:**
>
> This project is currently under development and has an opinionated configuration and setup. While README-AI provides an excellent starting point for any project that requires documentation, it is important to review all text that is generated by the OpenAI API to ensure that it accurately represents your codebase.

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🔮 Features

<h1 align="center">1.<br>👇<br><br>🔖 Codebase Documentation</h1>
<table>
  <tr>
    <td>
      <h3>📍 Repository File Summaries</h3>
      <ul>
        <li>Code summaries of each script in your repository are generated via OpenAI's large language model APIs, such as gpt-3.5-turbo.</li>
        <li>Your codebase is parsed and file contents are converted to natural language, and displayed in Markdown table format.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="./docs/imgs/open_docs.png" alt="docs">
      <h1 align="center">↕️</h1>
      <img src="./docs/imgs/closed_docs.png" alt="docs">
    </td>
  </tr>
</table>
</p>

<h1 align="center">⒉<br>👇<br><br>🎖 Badges</h1>
<table>
  <tr>
    <td>
      <h3>📍 Introduction, Badges, Table of Contents</h3>
      <ul>
        <li>The OpenAI API generates a 1-sentence phrase describing your project.</li>
        <li>Project dependencies and software visualized using beautiful SVG icon badges.</li>
        <li>Badges are sorted by hex code, displayed from light to dark hues.</li>
        <li>A table of contents is also provided for your README.md file.</li>
        </li>
      </ul>
      <br>
    </td>
  </tr>
  <tr>
    <td>
      <img src="./docs/imgs/header.png" alt="header">
    </td>
  </tr>
</table>
</p>

<h1 align="center">⒊<br>👇<br><br>🧚 Text Generation</h1>
<table>
  <tr>
    <td>
      <h3>📍 Project Feature Table</h3>
      <ul>
        <li>These sections are generated using detailed prompts, embedded with your repository metadata.</li>
        <li>The <i>Overview</i> section describes your project's use case and application.</li>
        <li>The <i>Features</i> section highlights attributes of your codebase, formatted in a Markdown table.</li>
        <li>Working on fine-tuning the prompts to improve the accuracy and relevance to your project.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="./docs/imgs/overview.png" alt="overview">
      <img src="./docs/imgs/features.png" alt="features">
    </td>
  </tr>
</table>
</p>

<h1 align="center">⒋<br>👇<br><br>🌲 Repository Tree</h1>
<p align="center">Why not a directory tree as well? Visualize your codebase structure in your README.
</p>

|                               |
|-------------------------------|
| ![tree](./docs/imgs/tree.png) |


<h1 align="center">⒌<br>👇<br><br>📦 Dynamic User Setup Guides</h1>
<table>
  <tr>
    <td>
      <h3><b>📍 Installation, Usage, and Running Tests</b></h3>
        <ul>
          <li>Dynamically generates instructions for installing, using, and testing your codebase.</li>
          <li>This section of your README.md will help others easily setup and use your project!</li>
          <li>README-AI currently supports this feature for codebases written in:</li>
          <ul>
            <li>
              <i>Python, Rust, Go, C, Kotlin, Java, JavaScript, TypeScript.</i>
            </li>
          </ul>
        </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="./docs/imgs/setup.png" alt="setup">
    </td>
  </tr>
</table>

<h1 align="center">⒍<br>👇<br><br>👩‍💻Contributing Guidelines & more!</h1>
<p align="center">Adds additional standard sections to build out a robust README file!</p>

|                               |
|-------------------------------|
| ![contribute](./docs/imgs/contribute.png) |
| ![license](./docs/imgs/license.png) |

<h1 align="center">⒎<br>👇<br><br>💥 Example Files</h1>
<p align="center">Markdown example files generated by the README-AI app!</p>
<div align="center">
  <table align="center">
    <tr>
      <th></th>
      <th>Example File</th>
      <th>Repository</th>
      <th>Language</th>
      <th>Bytes</th>
    </tr>
    <tr>
      <td>1️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_Python.md">README-Python.md</a></td>
      <td><a href="https://github.com/eli64s/README-AI">readme-ai</a></td>
      <td>Python</td>
      <td><p>19,839</p>
    </tr>
      <td>2️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_TypeScript.md">README-TypeScript.md</a></td>
      <td><a href="https://github.com/Yuberley/ChatGPT-App-React-Native-TypeScript">chatgpt-app-react-typescript</a></td>
      <td>TypeScript, React</td>
      <td><p>988</p>
    </tr>
    <tr>
      <td>3️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_JavaScript_GPT.md">README-JavaScript.md</a></td>
      <td><a href="https://github.com/idosal/assistant-chat-gpt">assistant-chat-gpt-javascript</a></td>
      <td>JavaScript, React</td>
      <td><p>212</p>
    </tr>
    <tr>
      <td>4️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_Kotlin.md">README-Kotlin.md</a></td>
      <td><a href="https://github.com/rumaan/file.io-Android-Client">file.io-android-client</a></td>
      <td>Kotlin, Java, Android</td>
      <td><p>113,649</p>
    </tr>
    <tr>
      <td>5️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_RUST_C.md">README-Rust-C.md</a></td>
      <td><a href="https://github.com/DownWithUp/CallMon">rust-c-app</a></td>
      <td>C, Rust</td>
      <td><p>72</p>
    </tr>
    <tr>
      <td>6️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_Go.md">README-Go.md</a></td>
      <td><a href="https://github.com/olliefr/docker-gs-ping">go-docker-app</a></td>
      <td>Go</td>
      <td><p>41</p>
    </tr>
    <tr>
      <td>7️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_Java.md">README-Java.md</a></td>
      <td><a href="https://github.com/avjinder/Minimal-Todo">java-minimal-todo</a></td>
      <td>Java</td>
      <td><p>17,725</p>
    </tr>
    <tr>
      <td>8️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_FastAPI_Redis.md">README-FastAPI-Redis.md</a></td>
      <td><a href="https://github.com/FerrariDG/async-ml-inference">async-ml-inference</a></td>
      <td>Python, FastAPI, Redis</td>
      <td><p>355</p>
    </tr>
    <tr>
      <td>9️⃣</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_MLOps.md">README-Python-MLOps.md</a></td>
      <td><a href="https://github.com/GokuMohandas/mlops-course">mlops-course</a></td>
      <td>Python, Jupyter</td>
      <td><p>8,524</p>
    </tr>
    <tr>
      <td>🔟</td>
      <td><a href="https://github.com/eli64s/README-AI/blob/main/docs/README_PyFlink.md">README-Apache-Flink.md</a></td>
      <td>local directory</td>
      <td>PyFlink</td>
      <td><p>32</p>
    </tr>
  </table>
</div>


<h1 align="center">⒏<br>👇<br><br>📜 Custom templates and styles coming soon!</h1>
<p align="center">Developing a feature that allows the user to select from a variety of README formats and styles.</p>
<p align="center">Example template options include data and ML focused, research, hackathons, minimal, and more!</p>

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---

## 🚀 Getting Started

### ✅ Dependencies

Before you begin, ensure that you have the following prerequisites installed:

- Python 3.8 or higher
- Conda package manager (recommended)
- Access to the OpenAI API (see OpenAI setup guide below)

#### 📂 Repository

Most user's will run README-AI using the command-line interface, specifying their repository on run-time. However, if you would like to use the default configuration, you will need to update the [configuration file](./conf/conf.toml) with your repository's remote URL (GitHub, GitLab) or local directory pat on your machine.

```toml
# Repository Configuration
[git]
repository = "INSERT YOUR REPOSITORY URL / LOCAL DIRECTORY"
```

#### 🔐 OpenAI API Setup

To use the README-AI application, you will need to create an [OpenAI account](https://platform.openai.com/) and generate an API key. The steps below outline how to create an account and generate an API key:

<details closed><summary>OpenAI API User Guide</summary>

1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click the "Sign up for free" button.
3. Fill out the registration form with your information and agree to the terms of service.
4. Once logged in, click on the "API" tab.
5. Follow the instructions to create a new API key.
6. Copy the API key and keep it in a secure place.

</details>

For the best README-AI experience, consider setting up a payment method on OpenAI's website. This allows you to use more performant language models such as `gpt-3.5-turbo`. With no payment method, you will be limited to the base `gpt-3` models, which may result in less accurate README files or errors during the generation process.

> ⚠️ **Note:**
>
> If using a payment method, ensure that you have enough credits to run the README-AI application and be sure to continously monitor your API usage and costs with this link - [OpenAI API Usage Dashboard](https://platform.openai.com/account/usage). This API is not free to use, and **YOU WILL BE CHARGED FOR EACH REQUEST MADE TO THE API, WHICH CAN ADD UP VERY QUICKLY.** The README.md file generation should take less than 1 minute to execute, so please kill the process if it is taking longer than a few minutes.

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
conda activate readme_ai
pip install -r requirements.txt
```

3. Set up the OpenAI API key by creating an environment variable:

```sh
export OPENAI_API_KEY=<your-api-key>
```

### 🎮 Using README-AI

Use the command-line to provide the OpenAI API key (if not already set) and specify an output path for your README file, along with the path to your local repository or remote code repository.

Command-Line Arguments:

- `--api_key` : Provide your OpenAI API key.
- `--output` : Provide a path where to write the output file.
- `--repository` : Provide a remote Git URL or a local directory.

```sh
python src/main.py --api_key skabc123 --output README_AI.md --repository https://github.com/eli64s/README-AI
```

Alternatively, run the bash script to run README-AI with the default configuration.

```sh
bash scripts/run.sh
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

- [X] Add additional language support for populating the *installation*, *usage*, and *test* README sections.
- [ ] Design and implement a variety of README template formats and styles.
- [ ] Add feature to select the output language for the README file (e.g. CN, DE, ES, FR, JA, KO, PT, RU).
- [ ] Create UI with [Textual](https://github.com/Textualize/textual) or another framework to improve user experience.

---

## 🤝 Contributing

Contributions are welcomed and encouraged! Please follow these steps in the [Contributing Guidelines](./CONTRIBUTING.md), thank you!

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## 👏 Acknowledgments

*SVG Icons*
  - [Aveek-Saha/GitHub-Profile-Badges](https://github.com/Aveek-Saha/GitHub-Profile-Badges)
  - [Ileriayo/Markdown-Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right">
  <a href="#top"><b>🔝 Return </b></a>
</p>

---
