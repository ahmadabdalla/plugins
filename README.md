# ahmadabdalla/plugins

Centralized plugin marketplace for all **ahmadabdalla** plugins. Works with both [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/cli-plugin-reference) and [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).

Plugins are hosted in their own dedicated repositories and referenced here via the `github` source type so that this marketplace acts as a single discovery point.

## Quick start

### Add the marketplace

```text
/plugin marketplace add ahmadabdalla/plugins
```

### Install a plugin

**GitHub Copilot CLI:**

```text
/plugin install <plugin-name>
```

**Claude Code:**

```text
/plugin install <plugin-name>@ahmadabdalla-plugins
```

## Marketplace commands

### GitHub Copilot CLI

| Action | Command                                          |
| ------ | ------------------------------------------------ |
| Add    | `/plugin marketplace add ahmadabdalla/plugins`   |
| List   | `/plugin marketplace list`                       |
| Remove | `/plugin marketplace remove ahmadabdalla-plugins` |

> When **adding** a marketplace you use `OWNER/REPO`. When **removing** you use the marketplace **name** (as shown in the list).

### Claude Code

> Claude Code uses the `name@marketplace` format for plugin commands. Direct install from GitHub (without a marketplace) is **not supported**.

**Shortcuts:** `/plugin market` works in place of `/plugin marketplace`. `rm` works in place of `remove`.

| Action | Command                                            |
| ------ | -------------------------------------------------- |
| Add    | `/plugin marketplace add ahmadabdalla/plugins`     |
| List   | `/plugin marketplace list`                         |
| Update | `/plugin marketplace update ahmadabdalla-plugins`  |
| Remove | `/plugin marketplace remove ahmadabdalla-plugins`  |

> Use `add` / `remove` for **marketplaces**. Use `install` / `uninstall` for **plugins**. The verbs are not interchangeable — `uninstall` silently fails on marketplaces.

## Available plugins

| Plugin                                                                         | Description                                                    | Version |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------- | ------- |
| [azure-cost-calculator](https://github.com/ahmadabdalla/azure-cost-calculator) | Real-time Azure cost estimation using the Azure Retail Prices API | 1.2.3   |

## Versioning & update strategy

Each plugin entry in `.claude-plugin/marketplace.json` is pinned to a specific Git tag (`ref`) in the plugin's repository. When a plugin repository cuts a new release:

1. A pull request is opened against this repository (manually or via a GitHub Action in the plugin repo) to bump the `version` and `ref` fields.
2. After review and merge, users pick up the change the next time they run `/plugin marketplace update ahmadabdalla-plugins`.

This keeps the marketplace stable — users always get a known-good version — while still allowing rapid updates when new releases are published.

## License

[MIT](LICENSE)