# ahmadabdalla/plugins

Centralized plugin marketplace for all **ahmadabdalla** plugins. Works with both [GitHub Copilot CLI](https://docs.github.com/en/copilot/reference/cli-plugin-reference) and [Claude Code](https://code.claude.com/docs/en/plugin-marketplaces).

Plugins are hosted in their own dedicated repositories and referenced here via the `url` source type (with explicit HTTPS URLs) so that this marketplace acts as a single discovery point.

## Quick start

### Add the marketplace

```text
/plugin marketplace add ahmadabdalla/plugins
```

> Adding the repo `ahmadabdalla/plugins` registers the marketplace under its manifest name **`ahmadabdalla-plugins`**. Use the manifest name for all subsequent commands (`install`, `update`, `remove`).

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

<details>
<summary><strong>GitHub Copilot CLI</strong></summary>

| Action | Command                                          |
| ------ | ------------------------------------------------ |
| Add    | `/plugin marketplace add ahmadabdalla/plugins`   |
| List   | `/plugin marketplace list`                       |
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
| [azure-cost-calculator](https://github.com/ahmadabdalla/azure-cost-calculator) | Real-time Azure cost estimation using the Azure Retail Prices API | 1.5.4   |

## Versioning & update strategy

Each plugin entry in `.claude-plugin/marketplace.json` is pinned to a specific Git tag (`ref`) in the plugin's repository. When a plugin repository cuts a new release, the `version` and `ref` fields in this marketplace are updated to match.

## License

[MIT](LICENSE)