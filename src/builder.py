"""src/format.py
"""
import pandas as pd

import utils


def get_icons(path):
    contents = utils.read_json(path)
    icon_map = {}
    idx = 0
    while True:
        try:
            row = contents["icons"][idx]
            icon_map[row["name"].lower()] = row
        except:
            break
        idx += 1
    return icon_map


def create_header(path, pkgs):
    pkgs.append("git")
    header = ""
    icons = get_icons(path)
    for pkg in pkgs:
        if pkg in icons:
            badge = icons[pkg.strip().lower()]["src"]
            header += f'<img src="{badge}">\n\t\t\t\t'
    return header


def create_html(cfg, badges, name, path):
    """This function creates an html file from a csv file.
    Args:
        icon (str): The icon to be used in the html file.
    Returns:
        str: The html file.
    """
    header = f"""{cfg.html.header}
        <h1>{name}</h1>
        <hr>
        <h3>Software and Packages</h3>
        <p>[description]</p>
        <p>{badges}</p>
        </div>
        """
    body = cfg.html.body
    closing = cfg.html.closing

    data = pd.read_csv(path)

    prev_dir = None
    for i, j in data.iterrows():
        file = j[0].split("/")
        curr_dir = file[0]
        script = file[1]

        if prev_dir != curr_dir:
            tag = f"""<h3><i>{curr_dir.upper()}</i></h3>
                <dl>
                <dt><b><i>{script}</i></b></dt>
                <dd>{j[1].replace('"', '')}</dd>
                </dl>
                """
        else:
            tag = f"""<dl>
                <dt><b><i>{script}</i></b></dt>
                <dd>{j[1].replace('"', '')}</dd>
                </dl>
                """
        body = f"{body}{tag}"
        prev_dir = curr_dir

    return f"{header}{body}{closing}"
