# ahmadabdalla/plugins

Centralized plugin marketplace for all **ahmadabdalla** plugins. Works with [Codex CLI](https://developers.openai.com/plugins/build/plugins), [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces), and [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

Plugins are hosted in their own dedicated repositories and referenced here via the `url` source type (with explicit HTTPS URLs) so that this marketplace acts as a single discovery point.

## Quick start

### Codex CLI

```bash
codex plugin marketplace add ahmadabdalla/plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

Start a task with `$aasystem:aapilot`, or select a specialist such as `$aasystem:product`.

### Claude Code

```bash
claude plugin marketplace add ahmadabdalla/plugins
claude plugin install aasystem@ahmadabdalla-plugins
```

Start a task with `/aasystem:aapilot`, or select a specialist such as `/aasystem:product`.

### GitHub Copilot CLI

```bash
copilot plugin marketplace add ahmadabdalla/plugins
copilot plugin install aasystem@ahmadabdalla-plugins
```

Run `/skills` in Copilot to inspect the installed skills.

The repository registers as **`ahmadabdalla-plugins`**. Add it once per host. Replace `aasystem` with `azure-cost-calculator` to install that plugin instead. If the marketplace is already registered, refresh it before installing a newly listed plugin.

## Marketplace commands

<details>
<summary><strong>Codex CLI</strong></summary>

| Action | Command |
| --- | --- |
| Add | `codex plugin marketplace add ahmadabdalla/plugins` |
| List | `codex plugin marketplace list` |
| Refresh | `codex plugin marketplace upgrade` |
| Remove | `codex plugin marketplace remove ahmadabdalla-plugins` |

</details>

<details>
<summary><strong>GitHub Copilot CLI</strong></summary>

| Action | Command                                          |
| ------ | ------------------------------------------------ |
| Add    | `/plugin marketplace add ahmadabdalla/plugins`   |
| List   | `/plugin marketplace list`                       |
| Update | `/plugin marketplace update ahmadabdalla-plugins` |
| Remove | `/plugin marketplace remove ahmadabdalla-plugins` |

> When **adding** a marketplace you use `OWNER/REPO`. When **removing** you use the marketplace **name** (as shown in the list).

</details>

<details>
<summary><strong>Claude Code</strong></summary>

> Claude Code uses the `name@marketplace` format for plugin commands. Direct install from GitHub (without a marketplace) is **not supported**.

**Shortcuts:** `/plugin market` works in place of `/plugin marketplace`. `rm` works in place of `remove`.

| Action | Command                                            |
| ------ | -------------------------------------------------- |
| Add    | `/plugin marketplace add ahmadabdalla/plugins`     |
| List   | `/plugin marketplace list`                         |
| Update | `/plugin marketplace update ahmadabdalla-plugins`  |
| Remove | `/plugin marketplace remove ahmadabdalla-plugins`  |

> Use `add` / `remove` for **marketplaces**. Use `install` / `uninstall` for **plugins**. The verbs are not interchangeable — `uninstall` silently fails on marketplaces.

</details>

## Available plugins

| Plugin                                                                         | Description                                                    | Version |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------- | ------- |
| [azure-cost-calculator](https://github.com/ahmadabdalla/azure-cost-calculator) | Real-time Azure cost estimation using the Azure Retail Prices API | 1.10.2  |
| [aasystem](https://github.com/ahmadabdalla/aasystem) | Ahmad Abdalla's Pilot System: playbooks, specialist skills, and verification | 0.1.0 |

The original aasystem installation was verified in all three hosts. The temporary aapilot pin needs fresh installation and upgrade checks; full workflow validation remains pending.

## Versioning & update strategy

One catalog, `.claude-plugin/marketplace.json`, serves all three hosts. Each plugin entry is pinned to a release tag (`ref`) or an exact commit (`sha`) in its own repository. aasystem temporarily pins the merged aapilot commit, `48a7e7b0bfd2a4b47c7cae9204f340b34711c58d`, while its [versioned release process](https://github.com/ahmadabdalla/aasystem/issues/2) and [marketplace release adoption](https://github.com/ahmadabdalla/plugins/issues/38) are implemented.

When a plugin cuts a tested release, update its catalog `version` and source selector together. Keep existing release tags immutable.

### Temporary aasystem update

The [temporary SHA update](https://github.com/ahmadabdalla/plugins/issues/39) keeps version `0.1.0` aligned with the upstream manifests. This is a bridge to the versioned release, not a new release. An unchanged manifest version can leave users on cached contents, so a marketplace refresh alone does not establish that the plugin updated.

For an existing Codex installation, refresh this marketplace and reinstall only aasystem:

```bash
codex plugin marketplace upgrade ahmadabdalla-plugins
codex plugin remove aasystem@ahmadabdalla-plugins
codex plugin add aasystem@ahmadabdalla-plugins
```

Start a fresh Codex conversation and select `$aasystem:aapilot`. The new entry point should appear in the installed skills; `$aasystem:aasystem` is the old entry point.

Claude Code and Copilot also provide marketplace refresh and plugin uninstall/install commands, but their same-version reinstall paths for this temporary pin remain unverified. Ordinary or background update must not be assumed to replace cached contents. The permanent release will bump the upstream manifest versions and replace this SHA with a release tag.

## License

[MIT](LICENSE)
