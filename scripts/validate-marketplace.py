#!/usr/bin/env python3
"""Check the catalog against published GitHub tags. Requires Python 3 and gh."""
import base64
import json
from pathlib import Path
import re
import subprocess
import sys


def github(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True))


def check(condition, message):
    if not condition:
        raise ValueError(message)


def validate(catalog):
    check(catalog["name"] == "ahmadabdalla-plugins", "Marketplace identity changed")
    plugins = catalog["plugins"]
    names = [plugin["name"] for plugin in plugins]
    check(len(names) == len(set(names)), "Duplicate plugin entries")
    check(bool(plugins), "Empty catalog")
    for plugin in plugins:
        name, version, source = plugin["name"], plugin["version"], plugin["source"]
        check(re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version), f"{name}: invalid version")
        check(source["source"] == "url" and "sha" not in source, f"{name}: use one release ref, without sha")
        check(source["ref"] == f"v{version}", f"{name}: ref and version differ")
        match = re.fullmatch(r"https://github\.com/([\w.-]+/[\w.-]+)\.git", source["url"])
        check(match, f"{name}: expected an HTTPS GitHub repository URL")
        repo, tag = match[1], source["ref"]
        target = github(f"repos/{repo}/git/ref/tags/{tag}")["object"]
        if target["type"] == "tag":
            target = github(f"repos/{repo}/git/tags/{target['sha']}")["object"]
        check(target["type"] == "commit", f"{name}: tag does not target a commit")
        commit = target["sha"]
        release = github(f"repos/{repo}/releases/tags/{tag}")
        check(release["tag_name"] == tag and not release["draft"], f"{name}: release is not published")
        manifests = [".claude-plugin/plugin.json"]
        if name == "aasystem":
            manifests.append("plugin.json")
        for path in manifests:
            file = github(f"repos/{repo}/contents/{path}?ref={commit}")
            manifest = json.loads(base64.b64decode(file["content"]))
            check(manifest["name"] == name and manifest["version"] == version,
                  f"{name}: {path} identity/version differs from catalog")
        if name == "aasystem":
            github(f"repos/{repo}/contents/skills/aapilot/SKILL.md?ref={commit}")
        print(f"PASS: {name} {version} → {tag} → {commit}")


if __name__ == "__main__":
    path = Path(__file__).resolve().parents[1] / ".claude-plugin/marketplace.json"
    try:
        validate(json.loads(path.read_text()))
    except (ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        sys.exit(f"FAIL: {error}")
