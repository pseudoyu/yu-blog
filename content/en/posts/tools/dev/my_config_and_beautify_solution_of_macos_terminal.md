---
title: "Warp, iTerm2, or Alacritty? My Terminal Tinkering Journey"
date: 2022-07-10T11:18:29+08:00
draft: false
tags: ["dev-environment", "terminal", "macos", "iterm2", "tmux", "alacritty", "zsh", "starship", "warp", "neovim", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here After Us - Mayday》" >}}

## Preface

As a developer, whether running and debugging code locally or deploying and maintaining projects on remote servers, we can't do without the terminal shown in the image below, which is the black window often seen in sci-fi movies.

![my_terminal_tools](https://image.pseudoyu.com/images/my_terminal_tools.png)

Operating systems generally have their default shells, such as "Powershell" on Windows, and bash or zsh on macOS and Linux systems. Systems with graphical interfaces also come with pre-installed terminal emulators, like "Terminal.app" on macOS and various terminal programs bundled with Linux distributions.

As a productivity tool enthusiast and aesthete, my tinkering with terminal configuration and customization has never ceased, going through several iterations. Perhaps unlike most developers, I'm not a devotee of any particular solution. Instead, I try various tools, configuring them according to my habits to reduce operational differences between different solutions. In daily development, I switch seamlessly between them based on purpose, sometimes even randomly choosing one to use as a mood changer.

This article mainly describes my terminal solution choices and configuration details.

## Terminal Configuration Requirements

Terminal configuration consists of several aspects:

1. **Tool Configuration**. When developing on macOS or Windows systems, we often need a terminal emulator to connect to the local development environment or remote servers. This is usually a resident application in our development process, and its aesthetics, response speed, and shortcuts greatly affect our development experience, making it the focus of our configuration and customization.

2. **Functional Configuration**. When using the command line to perform operations on system services/files, we need to use shells like bash or zsh. Configuring command prompts, auto-completion, and other features can effectively enhance our user experience.

3. **Integration Configuration**. Besides running common command-line tools like git, terminals often need to meet advanced needs such as text editing and multi-task management. Therefore, deeply integrating tools like vim and tmux through terminal configuration is also an important aspect of optimizing our development experience.

I've outlined my terminal usage requirements, listing the following core points:

1. **Minimalist Style**. As software that I need to face for long periods every day, even the fanciest themes can become tiresome and even affect my focus. Therefore, my basic approach to configuring the appearance and operational logic of terminal tools is Minimal Distraction - simple but not monotonous.

2. **Fast Response**. Initially, I focused on aesthetics and functionality in terminal configuration, installing many plugins and configurations, but this also resulted in the unpleasant experience of several seconds of delay each time the software started. Therefore, the response speed during use is also a focus of my solution selection and optimization.

3. **Customizability**. Because I use the special Vim "HJKL" key layout for my code editor and window management, I also hope to be able to configure flexible shortcuts to reduce the cost of switching between different software.

4. **Portability**. I often need to operate on different devices, and occasionally there are device iterations. I hope my configurations can be conveniently ported to new devices/servers, preferably reusing the same configuration file.

5. **Extensibility**. I hope to be able to extend some functions and plugins according to my needs, such as using fzf to search for files or command history, jumping to specified directories via commands, using waka-time to record my programming time, etc.

## My Terminal Configuration Explanation

Even with relatively clear requirements, finding suitable tools and configuration solutions is still a challenging but enjoyable task. Next, I will describe the solutions I'm still using and quite satisfied with, and provide my configuration files for reference.

Furthermore, since I develop on macOS most of the time, my terminal tool configurations are mainly based on the macOS platform. However, some tools or plugins (such as Alacritty, ohmyzsh, Neovim, etc.) are cross-platform, with similar configuration methods that can be referenced and configured according to actual situations.

### Warp

![warp_interface](https://image.pseudoyu.com/images/warp_interface.png)

I'm naturally inclined to tinker, hoping to have enough customization space for various configurations. However, if I were to recommend only one tool to newcomers who have just started using terminals, I would unhesitatingly choose "[Warp](https://www.warp.dev)".

Warp is a modern terminal tool developed based on Rust, which is extremely fast, powerful, and ready to use out of the box. It supports intelligent prompts, AI command smart search, command history query, custom workflows, and other functions without additional configuration.

I was one of the early batch of users participating in Warp's internal testing. Even in the early stages when the functions were still incomplete, I was amazed by its exquisite appearance and smooth user experience. Because it's developed using the Rust language, Warp's command execution and response speed are very fast. Moreover, it has many common functions built-in, allowing us to get powerful functional support without configuring plugins like history search and command prompts at the Shell layer.

![warp_code_block](https://image.pseudoyu.com/images/warp_code_block.png)

It also has many unique features that traditional terminals don't possess, such as the concept of "blocks". Each command execution is presented in the form of a "command block", allowing movement between blocks using arrow keys, avoiding the need to constantly drag the scroll bar to read when some command output results are too long. We can also bookmark, copy commands, search content, or even share online specific blocks through the upper right corner.

![edit_command_in_warp](https://image.pseudoyu.com/images/edit_command_in_warp.png)

Different from the experience of conventional terminal tools, Warp's command input window is permanently fixed at the bottom (closer to an IDE), visually separating our command input from result feedback. Moreover, its input mode is closer to a text editor - we can move the cursor freely using the mouse or keyboard to edit, modify commands, or input multi-line commands for sequential execution. This is what I consider to be Warp's killer feature.

![warp_other_feature](https://image.pseudoyu.com/images/warp_other_feature.png)

We only need to use the corresponding shortcuts in the input box to invoke functions like history search and custom workflows, and can use the mouse wheel or direction keys for selection, which is very flexible. More powerful is that when we use Warp to connect to a remote terminal via SSH, these shortcuts are still effective, such as history search, without the need for configuration on the target server.

It's also worth mentioning that we can use the built-in shortcuts `Command+D` and `Command+Shift+D` to split the terminal horizontally or vertically, without the need to integrate other tools or perform additional configuration.

With the development of technology, text editors have been continuously updated, adding rich features and providing better user experiences. However, the terminal that we developers work with day and night has been developing slowly. Warp was born in this context, just as its official website describes:

> The terminal for the 21st century.

### iTerm2

Before using Warp, my main terminal tool was [iTerm2](https://iterm2.com), which I believe is also a must-install software for many developers when they first get a Mac (after all, the aesthetics and playability of the default terminal are not great). iTerm2 is a long-standing terminal tool that combines aesthetics and functionality, and even its default configuration already meets our needs very well.

#### Appearance and Color Scheme

![iterm2_interface](https://image.pseudoyu.com/images/iterm2_interface.png)

I modified the configuration of a YouTuber "[Takuya Matsuyama](https://www.craftz.dog)" to customize a minimalist appearance scheme.

First, configure the theme, tab bar, and status bar in the **Preferences** - **Appearance** section as follows to maintain a relatively simple layout.

![iterm2_theme_config](https://image.pseudoyu.com/images/iterm2_theme_config.png)

After completing the theme configuration, right-click the bottom status bar for detailed configuration. I selected some status bar components to display device status in real-time. This part can be chosen according to your preferences.

![iterm2_status_components](https://image.pseudoyu.com/images/iterm2_status_components.png)

Select your theme color scheme or import other color schemes in the **Profile** - **Colors** panel. You can click [here](https://github.com/pseudoyu/dotfiles/tree/master/iterm2) to download my configuration file, import it, and adjust it according to your needs.

![iterm2_window_blur_setting](https://image.pseudoyu.com/images/iterm2_window_blur_setting.png)

After selecting the color scheme, I achieved a transparent background and frosted glass effect (window blur) by adjusting Transparency and Blur. This can be adjusted according to the visual effect of the specific device.

After configuring the terminal tool, we still need to configure the Shell to integrate some custom themes, intelligent prompts, search history records, and other extension modules. I use the zsh + ohmyzsh + starship solution. Since these configurations are common to various solutions, see the Alacritty configuration description section below for details.

#### Multi-server Management

![iterm2_profile_settings](https://image.pseudoyu.com/images/iterm2_profile_settings.png)

Currently, I mainly use iTerm2 to connect to my various remote hosts/servers. It provides convenient multi-configuration management functionality, allowing quick switching between different servers or configuration environments by setting different Profiles, and can use conspicuous Badges as identifiers.

![iterm2_multiple_servers_management](https://image.pseudoyu.com/images/iterm2_multiple_servers_management.png)

When we need to connect to multiple development machines for work or personal use, we can open the server by pressing `Command+O` or by right-clicking the iTerm2 icon in the Dock bar to select the corresponding Profile. We can also use the built-in shortcuts `Command+D` and `Command+Shift+D` to split the terminal horizontally or vertically, facilitating simultaneous operation of multiple servers without constantly switching windows.

### Alacritty

iTerm2 is already a terminal tool with a very balanced aesthetic and functionality on the macOS platform, but its overall response speed and configuration freedom are not so perfect. Therefore, I now mainly use it to connect to remote servers, and have switched to [Alacritty](https://alacritty.org) for my commonly used local terminal.

Alacritty is also a cross-platform terminal tool written in Rust, providing some basic default configurations and customizing various settings through the `~/.config/alacritty/alacritty.yml` file. You can click [here](https://github.com/pseudoyu/dotfiles/tree/master/alacritty) to access my complete configuration.

#### Appearance Configuration

![alacritty_interface](https://image.pseudoyu.com/images/alacritty_interface.png)

For the appearance part, I mainly use the following configuration for window and font settings, achieving a semi-transparent minimalist configuration without any borders or buttons. Other configurations can be viewed on your own, such as select-to-copy and other commonly used features in iTerm2, which can be implemented through a few simple configuration items.

```yaml
window:
  opacity: 0.85
  padding:
    x: 18
    y: 16
  dynamic_padding: false
  decorations: buttonless

font:
  normal:
    family: "MesloLGSDZ Nerd Font Mono"
    style: Regular
  size: 13.0
  use_thin_strokes: true
```

#### ohmyzsh + starship

![alacritty_starship_config](https://image.pseudoyu.com/images/alacritty_starship_config.png)

I use zsh as the default terminal and use ohmyzsh to extend plugin functionality. zsh + ohmyzsh is currently a very popular Shell configuration solution, with a rich plugin system that can easily implement various extended functions through a few lines of configuration. First, we install according to its [official instructions](https://ohmyz.sh/#install).

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

After installation, enable ohmyzsh by adding the following configuration to `~/.zshrc`:

```plaintext
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh
```

I configured starship to beautify the Shell prompt. Similarly, we install and configure according to the [official instructions](https://starship.rs/guide/#🚀-installation):

```bash
curl -sS https://starship.rs/install.sh | sh
```

After completion, add the following configuration to `~/.zshrc`:

```plaintext
eval "$(starship init zsh)"
```

In addition, we can add plugin configurations in the plugin section of `~/.zshrc`. For example, I configured the following plugins to support intelligent prompts, syntax highlighting, `Ctrl + R` to search command history, and `j + <path>` for quick jumps.

```plaintext
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  zsh-history-substring-search
  autojump
  zsh-wakatime
  fzf-zsh-plugin
)
```

Click [here](https://github.com/pseudoyu/dotfiles/tree/master/zsh) to view my complete configuration. See the official documentation for installation instructions for each plugin.

#### tmux

![acacritty_tmux_demo](https://image.pseudoyu.com/images/acacritty_tmux_demo.png)

Because Alacritty itself doesn't provide functions like window splitting and session management, we need to integrate [tmux](https://github.com/tmux/tmux/wiki), a powerful cross-platform window management tool.

macOS platform users can install it via `brew install tmux`, while other platforms can install according to the [official instructions](https://github.com/tmux/tmux/wiki/Installing).

It's configured through `~/.tmux.conf`. Click [here](https://github.com/pseudoyu/dotfiles/tree/master/tmux) to view my configuration. Because its configuration and use require some learning and memory costs, this article will not describe it in detail. It's recommended to learn through the official documentation or other complete tutorials.

#### Neovim

We generally write code for our daily development in VS Code or Jetbrains' IDEs, while debugging requires the use of a terminal. If you don't want to frequently switch between various software, we can choose vim, an editing tool that can be used on the command line.

However, native vim is just a simple window, which seems out of place with our well-configured terminal. Therefore, we will also beautify and configure vim. Due to space limitations, this article will not cover specific configuration and usage content related to vim, but only describe my configuration solution.

![vi_homepage](https://image.pseudoyu.com/images/vi_homepage.png)

I use neovim, a derivative version of vim, whose high version uses lua for configuration and plugin management. I use a scheme customized by my friend [Cluas](https://github.com/Cluas), and made some modifications and adjustments based on it. You can click [here](https://github.com/pseudoyu/nvim/tree/pseudoyu) to view it. You only need to clone or download the `nvim/` directory and copy it to `~/.config`.

Its display effect is as follows:

![neovim_file_preview](https://image.pseudoyu.com/images/neovim_file_preview.png)

![neovim_edit_file](https://image.pseudoyu.com/images/neovim_edit_file.png)

#### Shortcut Configuration

tmux is a powerful window management tool, but it's very cumbersome to use `<Ctrl+b> + %` or `<Ctrl+b> + :` for horizontal or vertical screen splitting, or `<Ctrl+b> + c` to create a new window every time.

So, is there a way to achieve screen splitting or creating new windows through macOS's built-in shortcuts like `Command+D`, `Command+Shift+D`, or `Command+T` used by other terminal editors?

After some research and tinkering, I perfectly implemented this requirement by referring to [Josh Medeski](https://www.joshmedeski.com)'s article "[macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)".

The basic implementation method is to enter the `xxd -psd` command in the terminal, then type the tmux shortcut you want to map, such as `<Ctrl+b> + c`. It will display the hex codes for this input as:

```bash
^Bc
02630a
```

Here, `02` represents `<Ctrl+b>`, `63` represents `c`, and `0a` represents the enter key. Therefore, the hex code corresponding to the shortcut for creating a new window in tmux is `\x02\x63`. We can configure the following option in the key_bindings section of `~/.config/alacritty/alacritty.yml`:

```yaml
key_bindings:
  - { key: T, mods: Command, chars: "\x02\x63" }
```

The implementation principle for other shortcut configurations is the same. You can click [here](https://github.com/pseudoyu/dotfiles/tree/master/alacritty) to view all my shortcut configurations and modify them as needed.

## Conclusion

Up to this point, I have introduced and explained the configuration of the three terminal tools I currently use. The out-of-the-box Warp has its strengths, iTerm2 achieves a nice balance between ease of use and customization, and Alacritty has its own joy of tinkering.

As I mentioned earlier, sometimes switching to a different terminal is a whole new mood, and constantly optimizing and tinkering in leisure time is also a form of relaxation. Of course, everyone's terminal configuration has its own preferences and characteristics. This article only introduced my solution, which mostly satisfies my aesthetic pursuit and functional needs. I hope it can provide a reference for your terminal configuration. If you encounter problems in configuration or have better optimization suggestions, feel free to communicate.

## References

> 1. [GitHub - pseudoyu/dotfiles](https://github.com/pseudoyu/dotfiles)
> 2. [GitHub - Cluas/nvim](https://github.com/Cluas/nvim)
> 3. [Warp Official Website](https://www.warp.dev)
> 4. [iTerm2 Official Website](https://www.iterm2.com)
> 5. [Alacritty Official Website](https://alacritty.org)
> 6. [ohmyzsh Official Website](https://ohmyz.sh)
> 7. [starship Official Website](https://starship.rs)
> 8. [Neovim Official Website](https://neovim.io)
> 9. [GitHub - tmux/tmux](https://github.com/tmux/tmux)
> 10. [macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)