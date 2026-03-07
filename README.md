# ahmadabdalla/plugins

Centralized [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin marketplace for all **ahmadabdalla** plugins.

Plugins are hosted in their own dedicated repositories and referenced here via the `github` source type so that this marketplace acts as a single discovery point.

## Quick start

### Add the marketplace

```
/plugin marketplace add ahmadabdalla/plugins
```

### Install a plugin

```
/plugin install azure-cost-calculator@ahmadabdalla-plugins
```

### Update the marketplace

```
/plugin marketplace update ahmadabdalla-plugins
```

## Available plugins

| Plugin | Description | Version |
| --- | --- | --- |
| [azure-cost-calculator](https://github.com/ahmadabdalla/azure-cost-calculator) | Real-time Azure cost estimation using the Azure Retail Prices API | 1.2.3 |

## Versioning & update strategy

Each plugin entry in `.claude-plugin/marketplace.json` is pinned to a specific Git tag (`ref`) in the plugin's repository. When a plugin repository cuts a new release:

1. A pull request is opened against this repository (manually or via a GitHub Action in the plugin repo) to bump the `version` and `ref` fields.
2. After review and merge, users pick up the change the next time they run `/plugin marketplace update ahmadabdalla-plugins`.

This keeps the marketplace stable — users always get a known-good version — while still allowing rapid updates when new releases are published.

## License

[MIT](LICENSE)