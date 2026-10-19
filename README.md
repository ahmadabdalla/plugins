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

Run `/skills` in Copilot to inspect the installed skills, then use `/aapilot` to start a task.

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
| [aasystem](https://github.com/ahmadabdalla/aasystem) | Ahmad Abdalla's Pilot System: playbooks, specialist skills, and verification | 0.5.1 |

## Release updates

The catalog pins published release tags. To adopt a new release, update its `source.ref` and `version` together in `.claude-plugin/marketplace.json`, then open a reviewed PR. Keep installation names unchanged and never move a published tag.

Before opening the PR, run the catalog check. It requires Python 3 and GitHub CLI (`gh`):

```bash
python3 scripts/validate-marketplace.py
```

The check resolves each tag, confirms the release exists and compares upstream manifest versions. Installation and upgrades need separate host checks.

Successful aasystem publication automatically opens or updates one reviewed PR on `automation/aasystem-release`. It includes the release, exact commit and catalog validation results. Merge it after review and available host checks. Setup and retry instructions live in [aasystem's release guide](https://github.com/ahmadabdalla/aasystem/blob/main/docs/ops/releasing.md#marketplace-automation-setup).

PR CI also rejects catalog version downgrades. Require the `validate` check with branches up to date before merging so a stale PR cannot undo a newer adoption.

## Upgrade aasystem

Refresh the marketplace, update the installed plugin, then start a fresh session. The old `$aasystem:aasystem` and `/aasystem:aasystem` entry points are now `$aasystem:aapilot` and `/aasystem:aapilot`; there is no old-name alias.

For Codex, refresh and reinstall:

```bash
codex plugin marketplace upgrade ahmadabdalla-plugins
codex plugin remove aasystem@ahmadabdalla-plugins
codex plugin add aasystem@ahmadabdalla-plugins
codex plugin list --marketplace ahmadabdalla-plugins --json
```

For Claude Code:

```bash
claude plugin marketplace update ahmadabdalla-plugins
claude plugin update aasystem@ahmadabdalla-plugins
```

For Copilot CLI:

```bash
copilot plugin marketplace update ahmadabdalla-plugins
copilot plugin update aasystem@ahmadabdalla-plugins
```

Confirm the installed version and source tag match the aasystem catalog entry, then try a read-only `aapilot` invocation. Host test results and any gaps are recorded in the adoption PR; command help alone is not upgrade proof.

## License

[MIT](LICENSE)

