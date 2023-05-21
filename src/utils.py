"""Utility methods for the project."""

import re

import spacy


def reformat_sentence(text: str) -> str:
    """Clean up a sentence generated by OpenAI's GPT API."""
    # Remove non-letter characters from beginning of string
    text = re.sub(r"^[^a-zA-Z]*", "", text)

    # Remove extra white space around punctuation
    reformatted_text = re.sub(r"\s*([()'.,!?;:])(?!\.\s*\w)", r"\1", text)
    reformatted_text = re.sub(" +", " ", reformatted_text)

    # Remove extra white space around hyphens
    reformatted_text = re.sub(r"\s*-\s*", "-", reformatted_text)

    return reformatted_text


def spacy_text_processor(text: str) -> str:
    """Process text using spaCy."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    processed_text = " ".join([token.text for token in doc])
    return processed_text


def valid_url(s: str) -> bool:
    """
    Check if a given string is a valid URL.

    Parameters
    ----------
    s : str
        The string to check.

    Returns
    -------
    bool
        Returns True if the string is a valid URL, False otherwise.

    Raises
    ------
    None

    Examples
    --------
    is_url("https://www.google.com/") --> True
    is_url("ftp://ftp.example.com/") --> True
    is_url("www.example.com") --> False
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,63}|[A-Z]{2,63}\.[A-Z]{2,63}))"
        r"(?::\d+)?"  # optional port number
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(regex.match(s))
