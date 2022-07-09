---
title: "Warp，iTerm2 还是 Alacritty？我的终端折腾小记"
date: 2022-07-09T11:18:29+08:00
draft: true
tags: ["dev-environment", "terminal", "macos", "iterm2", "tmux", "alacritty", "zsh", "starship", "warp"]
categories: ["Tools"]
authors:
- "Arthur"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

作为一个开发者，不论是本地代码运行调试还是远程服务器的部署运维，都离不开下图所示的终端，也就是科技电影中常出现的黑窗口。

![my_terminal_tools](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/my_terminal_tools.png)

各个操作系统一般都有自己默认的 Shell，如 Windows 操作系统下的“Powershell”、macOS 与 Linux 系统的 bash、zsh 等，带图形版界面的系统也都会预置终端仿真器（Terminal Emulator），如 macOS 平台下的“Terminal”以及 Linux 各发行版自带的终端程序等。

作为一个生产力工具爱好者与颜控，我对终端配置美化的折腾从未停止过，也几经迭代。可能与大多数开发者不同的是，我并不是某种特定方案的拥趸，而是会去尝试各种工具，依照自己的习惯进行配置降低各个方案之间的操作差异，在日常开发过程中根据用途无缝切换使用，有时甚至是随机选一个使用以切换心情。

本文主要涉及我的终端方案选择及配置细节。

## 终端配置方案需求

终端配置分为几个方面：

1. **外观配置**。在使用 macOS 或 Window 系统进行开发时，我们往往需要一个终端仿真器（Terminal Emulator）连接到本机开发环境或远程服务器，这通常是我们开发过程中的常驻应用，其颜值、响应速度与快捷键等也会很大程度影响我们的开发体验，因此是我们配置与美化的重点。
2. **功能配置**。我们在使用命令行对系统服务/文件进行一些操作时，需要使用 Shell，如 bash、zsh 等，对其进行一些命令提示、自动补全等配置能有效提升我们的使用体验。
3. **工具配置**。除了运行 git 等常用命令行工具外，终端往往还承担了文本编辑、多任务管理等进阶需求。因此，通过终端配置实现 vim、tmux 等工具的深度集成也是我们开发体验优化的重要一环。

而我梳理了自己的终端使用需求，列出了以下几个核心要点：

1. **简约**。作为一个每天都需要长时间面对的软件，再 fancy 的主题也会看腻，甚至影响自己的注意力。因此，我对于终端工具的外观与操作逻辑配置的基本思路为 Minimal Distraction，简约而不单调。
2. **响应速度快**。最开始我对终端的配置侧重在美观与功能，因此安装了很多插件配置，但因此也出现了每次开启需要几秒延迟的不良体验，因此开启与使用过程的响应速度也是我选择和优化的重点。
3. **可定制性**。因为我的代码编辑器与窗口管理使用的都是 Vim 『HJKL』 特殊键位，因此我也希望能够进行比较灵活的快捷键配置，满足自己在各个软件直接切换的成本。
4. **可移植性**。我时常需要在不同的设备上进行操作，偶尔也会有设备的迭代，会希望自己的配置能比较方便地移植到新设备/服务器等。
5. **可拓展性**。我希望能够根据自己的需求拓展一些功能与插件，如使用 fzf 对文件或命令历史记录进行检索，通过命令跳转至指定目录，使用 waka-time 记录自己的编程时间等。

## 我的终端配置之路

即使需求已经比较明确，找到合适的工具与配置方案依旧是一件困难但充满乐趣的事。接下来我将逐个对我仍在使用并且比较满意的方案进行描述，并提供我的配置文件供大家参考。

此外，因为我大多数时间都在 macOS 系统上进行开发，所以我的终端工具配置主要是基于 macOS 平台的，但有些工具或插件（如 Alacritty、ohmyzsh、Neovim 等）是跨平台的，配置方式大同小异，可以根据实际情况进行参照与配置。

### Warp

![warp_interface](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/warp_interface.png)

我本身是一个折腾流，会希望能自己能够对各类配置有足够的定制化空间。然而，如果要我只推荐一款工具给刚使用终端不久的新手，我会毫不犹豫地选择『[Warp](https://www.warp.dev)』。

Warp 是一个基于 Rust 开发的速度极快、功能强大且开箱即用的现代化终端工具。不需要额外配置就支持智能提示、AI 命令智能搜索、命令历史查询、自定义 workflow 等功能。

我是很早参与 Warp 内测的那一批用户，即使是在功能还很不完善的早期，我也被它精致的外观和顺滑的使用体验所惊艳到了。因为基于 Rust 语言开发，Warp 的命令执行与响应速度很快，并且它还内置了很多常用功能，我们无需在 Shell 层配置使用历史记录搜索、命令提示等各类插件就能获得强大的功能支持。

![warp_code_block](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/warp_code_block.png)

它还有很多传统终端不具备的特色功能，如“block”的概念，每一条命令的执行都以一个类似于代码块的方式呈现，可以通过上下左右键在各个 block 之间移动，避免了有些命令输出结果太长导致需要一直拉动滚动条阅览；并且我们可以通过右上角对特定 block 进行书签收藏、命令复制、内容检索甚至在线分享等。

![edit_command_in_warp](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/edit_command_in_warp.png)

与常规终端工具体验不同的是，Warp 的命令输入窗口长期固定在底层，且类似于文本编辑器，我们可以通过鼠标或是键盘任意移动光标编辑、修改命令或是输入多行命令依序执行，这也是我所认为的 Warp 的 killer feature。

![warp_other_feature](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/warp_other_feature.png)

我们仅需在输入框使用对应的快捷键即可唤出历史记录检索、自定义 workflow 等功能，并且可以使用鼠标滚轮或是方向键进行选择，十分灵活。更强大的是，当我们使用 Warp 通过 SSH 连接到远程终端时，这些快捷键依然有效，如历史记录搜索等，而无需在目标服务器进行配置。

另外值得一提的是我们可以通过内置快捷键 `Command+D` 与 `Command+Shift+D` 来水平或垂直拆分终端，无需集成其他工具或进行额外配置。

随着技术的发展，文本编辑器不断迭代更新，增加了丰富的功能并提供了更好的使用体验，然后与我们开发人员朝夕相处的终端却一直发展迟缓，Warp 正是在这个阶段应运而生，也正如它官网所描述的那样：

> The terminal for the 21st century.

### iTerm2

在使用 Warp 之前，我的主力终端工具为 [iTerm2](https://iterm2.com)，相信这也是很多开发者刚入手 Mac 时的必装软件（毕竟默认终端的颜值和可玩性都不太行）。iTerm2 是一个集美观与功能性为一体的老牌终端工具了，即使是默认配置也已经很好的满足了我们的需求。

#### 外观与配色

我对一位 YouTuber 『[Takuya Matsuyama](https://www.craftz.dog)』的配置加以改造，定制了一个性冷淡风外观方案。

首先在 **偏好设置** - **Appearance** 部分对主题、Tab 栏与状态栏进行如下配置，保持较为简洁的布局。

![iterm2_theme_config](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/iterm2_theme_config.png)

在 **Profile** - **Colors** 面板选取自己的主题配色或导入其他配色方案。可以点击[这里](https://github.com/pseudoyu/dotfiles/tree/master/iterm2)下载我的配置文件，导入并根据自己的需求进行调整。

![iterm2_window_blur_setting](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/iterm2_window_blur_setting.png)

完成配色方案选择后，我通过调整 Transparency 和 Blur 来实现背景透明与毛玻璃效果（即窗口模糊），此处可以根据具体设备的视觉效果进行调整。

完成了终端工具的配置后，我们还需要对 Shell 进行配置，以集成一些定制主题、智能提示、搜索历史记录等拓展模块，我使用的是 zsh + ohmyzsh + starship 方案，因这些配置为各个方案的通用部分，具体详见下述 Alacritty 配置说明部分。

#### 多服务器管理

![iterm2_profile_settings](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/iterm2_profile_settings.png)

目前我主要使用 iTerm2 来连接我的各个远程主机/服务器，它提供了方便的多配置管理功能，可以通过设置不同的 Profiles 实现不同服务器或配置环境的快速切换，并且可以用醒目的 Badge 来作为标识。

![iterm2_multiple_servers_management](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/iterm2_multiple_servers_management.png)

当我们在工作或个人使用中需要连接到多台开发机时，可以通过 `Command+O` 或通过右键 Dock 栏 iTerm2 图标选择对应 Profile 打开服务器，同时也可以通过内置快捷键 `Command+D` 与 `Command+Shift+D` 来水平或垂直拆分终端，便于多服务器同时操作而无需不断切换窗口。

### Alacritty

iTerm2 已经是 macOS 平台上颜值与功能都非常平衡的终端工具了，但综合使用下来它的响应速度与配置的自由度还是不那么完美，因此我现在主要将其用于连接远程服务器，本地常用终端后续更换为了 Alacritty。

Alacritty 也是一款使用 Rust 编写的跨平台终端工具，本身提供了一些基础默认配置，而通过一个 `alacritty.yml` 进行各项自定义配置，可以点击[这里](https://github.com/pseudoyu/dotfiles/tree/master/alacritty)访问我的完整配置。

#### 外观配置

![alacritty_interface](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/alacritty_interface.png)

外观部分我主要通过如下配置进行窗口与字体配置，实现了一种半透明的极简配置，甚至都没有任何边框与按钮。

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

![alacritty_starship_config](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/alacritty_starship_config.png)

我使用 zsh 作为默认终端，通过 ohmyzsh 来拓展插件功能。zsh + ohmyzsh 是目前非常流行的 Shell 配置方案，其具备了丰富的插件系统，可以通过几行配置轻松实现各项拓展功能，按照其官方说明安装即可：

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

安装完成后，通过在 `~/.zshrc` 中添加如下配置来启用 ohmyzsh：

```plaintext
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh
```

我配置了 starship 来美化 Shell 提示，首先根据官方文档进行安装配置：

```bash
curl -sS https://starship.rs/install.sh | sh
```

完成后在 `~/.zshrc` 中添加如下配置即可：

```plaintext
eval "$(starship init zsh)"
```

此外，我们还可以通过在 `~/.zshrc` 的 plugin 部分添加插件配置，例如我配置了如下插件支持，实现了智能提示、语法高亮、`Ctrl + R` 搜索命令历史记录以及 `j + <path>` 实现快捷跳转等。

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

我的完整配置可点击[这里](https://github.com/pseudoyu/dotfiles/tree/master/zsh)进行查看，各插件安装说明详见官方文档。

#### tmux

![acacritty_tmux_demo](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/acacritty_tmux_demo.png)

因为 Alacritty 本身不提供窗口拆分等功能，所以我们需要集成 tmux 这一强大的窗口管理工具。

macOS 平台用户用过 `brew install tmux` 安装即可，其通过 `~/.tmux.conf` 进行配置，点击[这里](https://github.com/pseudoyu/dotfiles/tree/master/tmux)查看我的配置，因其配置使用需要一定学习与记忆成本，本文不做详述，建议通过官方文档或其他完整教程进行学习。

#### Neovim

我们的日常开发的代码编写一般在 VS Code 或 Jetbrains 家的 IDE 中进行，而调试则需要使用终端，如果不想频繁切换于各个软件之间，我们可以选择 vim 这一可用于命令行的编辑工具，然而，原生 vim 就是一个简单的窗口，与我们的配置好的终端显得格格不入，因此，我们也将对 vim 进行美化配置。限于篇幅，本文不会涵盖 vim 的具体配置使用相关内容，仅对我的配置方案进行描述。

![vi_homepage](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/vi_homepage.png)

我使用的是 neovim 这一 vim 的衍生版本，其高版本采用 lua 进行配置与插件管理。我使用的我的一个朋友 [Cluas](https://github.com/Cluas) 定制的方案，并在其基础上进行了一些修改调整，可点击[这里](https://github.com/pseudoyu/nvim/tree/pseudoyu)查看，仅需将 `nvim/` 目录 clone 或复制到 `~/.config` 即可。

其显示效果如下：

![neovim_file_preview](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/neovim_file_preview.png)

![neovim_edit_file](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/neovim_edit_file.png)

#### 快捷键配置

tmux 是一个强大的窗口管理工具，然而每次都需要使用 `<Ctrl+b> + %` 或 `<Ctrl+b> + :` 来进行水平或垂直分屏，或是使用 `<Ctrl+b> + c` 来新建窗口等操作十分繁琐。

那么，有没有能够通过 macOS 自带的例如其他终端编辑器使用的 `Command+D`、`Command+Shift+D` 或 `Command+T` 来实现分屏或新建窗口等配置呢？

经过了一份调研与折腾，我参照着 [Josh Medeski](https://www.joshmedeski.com) 的这篇『[macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)』完美实现了这一需求。

其基本实现方式为，在终端输入 `xxd -psd` 命令后，键入所需要映射的 tmux 快捷键，如 `<Ctrl+b> + c`，其会显示该输入的 hex codes 为：

```bash
^Bc
02630a
```

其中，`02` 代表 `<Ctrl+b>`，`63` 代表 `c`，而 `0a` 代表回车键，因此，在 tmux 中新建窗口的快捷键对应 hex code 为 `\x02\x63`。我们在 `~/.config/alacritty/alacritty.yml` 中的 key_bindings 部分配置如下选项即可：

```yaml
key_bindings:
  - { key: T, mods: Command, chars: "\x02\x63" }
```

其他快捷键配置实现原理一致，可点击[这里](https://github.com/pseudoyu/dotfiles/tree/master/alacritty)查看我的所有快捷键配置并自行修改调整。

## 总结

至此，我对我所使用过的三种终端工具进行了介绍与配置说明，开箱即用的 Warp 有其强大之处，iTerm2 在易用性与定制化上实现了不错的平衡，而 Alacritty 也自有折腾的乐趣。

如我前文所述，有时候换一个终端就是一种全新的心情，闲暇时不断优化折腾也不失为一种乐趣。当然，每个人的终端配置都各有自己的偏好与特点，本文只是对我的方案进行了介绍，更多满足了自己的审美追求与功能需求，希望能够为你的终端配置提供一个参考。

## 参考资料

> 1. [pseudoyu/dotfiles](https://github.com/pseudoyu/dotfiles)
> 2. [macOS Keyboard Shortcuts for tmux](https://www.joshmedeski.com/posts/macos-keyboard-shortcuts-for-tmux)