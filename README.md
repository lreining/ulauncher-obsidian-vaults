<img src="images/logo.png" width=150>

# Ulauncher Obsidian Vaults
A simple extension for ulauncher to open your obsidian vaults.

## How it works
The plugin parses the obsidian.json configuration file (usually found at `~/.config/obsidian/obsidian.json`), and presents the list of vaults added to 
Obsidian.md to the user.

## Installation
Open the ulauncher preferences, and under the `extentions` tab, click `Add extension`. Paste the url
```
https://github.com/Kappabyte/ulauncher-obsidian-vaults
```
into the box and click add.

## Configuration
There are currently two supported configuation options.

### Vaults keyword

Here you can change the keyword that ulauncher looks for when using the extension.

**Default Value:** `ov`

### Obsidian config

Here you can change where the extension looks for the `obsidian.json` file, which is useful for if you have changed your `XDG_CONFIG_DIR` environment variable.

**Default Value:** `~/.config/obsidian/obsidian.json`

>[!note]
>You can use `~` to reference your home directory. Environment Varaibles are currently not supported.

## Usage

When ulauncher is open, simply type the keyword you defined in the configuration (by default, `ov`), followed by a space. Your list of vaults should appear. 
Any further input is treated as a filter for the results.

# Contributing

Feel free to open an issue or pull request if you would like to contribute or have any problems with the extension.
