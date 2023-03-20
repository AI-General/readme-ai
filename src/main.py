"""
src/main.py
"""
import argparse
from pathlib import Path

import dacite
import openai

import builder
import model
import processor
from conf import AppConfig
from logger import Logger
from utils import FileFactory

CONF = "conf/conf.toml"
LOGGER = Logger("readmeai_logger")


def main() -> None:
    LOGGER.info("README-AI is now executing.")

    # Load config file
    conf_file = Path(CONF).resolve()
    toml_file = FileFactory(conf_file).get_handler()
    conf_dict = toml_file.read_file()
    conf = dacite.from_dict(AppConfig, conf_dict)
    output_file = conf.paths.md
    
    # Command line arguments
    parser = argparse.ArgumentParser(
        description="Generate a README.md file via OpenAI."
    )
    parser.add_argument(
        "-k", "--api_key", type=str, help="Provide your OpenAI API key.", default=None
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Provide an output file path.", default=output_file,
    )
    args = parser.parse_args()
    openai.api_key = args.api_key
    if args.output:
        output_file = args.output

    # Get project dependencies
    repo_url = conf.github.url
    repo_full_name, repo_name = processor.get_repo_name(repo_url)
    files = processor.fetch_github_folder_contents(repo_full_name)
    reqs = processor.dependencies_helper(repo_url)

    LOGGER.info(f"Creating README.md for the {repo_name} repo.")
    LOGGER.info(f"Total files to summarize via OpenAI: {len(files)}")
    LOGGER.info(f"Project dependencies and tools list: {reqs}")

    # OpenAI API
    prompt_feats = conf.api.prompt_features
    features_text = model.generate_readme_features(repo_url, prompt_feats)
    code_docs = model.code_to_text(files)

    LOGGER.info(f"OpenAI generated text for README features section: {features_text}")
    LOGGER.info(f"OpenAI generated text for README modules section: {code_docs}")

    # Build README.md
    raw_docs = conf.paths.docs
    csv_file = FileFactory(raw_docs).get_handler()
    csv_file.write_file(code_docs)
    builder.build(conf, features_text, output_file, reqs, repo_name, repo_url)

    LOGGER.info("README-AI execution complete.")
    LOGGER.info(f"Find your documentation ➡️ {output_file}")


if __name__ == "__main__":
    main()
