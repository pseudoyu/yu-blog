---
title: "Automating Window Management: A macOS Window Management System Based on yabai+skhd"
date: 2022-06-04T13:08:33+08:00
draft: false
tags: ["macOS", "yabai", "skhd", "window management", "productivity"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Preface

It has been five years since I started using macOS, beginning with my first MacBook Pro that I saved up for during the summer of 2017. As my work and study needs have grown, I've gradually begun to use a multi-screen workflow. Because I constantly need to open many windows, such as IDEs, text editing tools, terminals, IM software, email clients, and so on, it can quickly become disorganized without careful attention. I found myself constantly switching between windows to find the one I needed, which was very inconvenient. Thus began my journey to explore window management solutions.

## Window Management Solution Requirements

First, I outlined my window management needs, listing the following core points:

1. Automatically perform intelligent split-screen on the current desktop each time a new window is opened, such as full screen for a single window, half-screen for two windows, and so on
2. Adjust the split-screen layout or restore the initial layout through shortcuts
3. Jump between different windows using shortcuts
4. Move/exchange different window positions using shortcuts
5. Conveniently perform some operations on the current window through shortcuts, such as full screen, centering, sending to a specific desktop, etc.
6. Fast switching speed

With these requirements in mind, I began to research several popular window management tools currently available.

## Window Management Tools

There are already many relatively mature window management tool solutions on the market, such as [Magnet](https://magnet.crowdcafe.com), [BetterTouchTool's built-in window snapping function](https://docs.folivora.ai/docs/100_window_snapping_chapter.html), etc. I have purchased and used both, but overall, I felt they didn't quite fit my workflow.

Magnet primarily relies on shortcuts. Although you can customize shortcuts to suit your habits, the memory cost is high. Moreover, if you have multiple devices, you need to download and reconfigure it with your own account to continue using it, which is not convenient.

![magnet_keyshotcuts](https://image.pseudoyu.com/images/magnet_keyshotcuts.png)

BetterTouchTool, on the other hand, relies on moving the mouse to various trigger corners of the window. The advantage is that you don't need to set shortcuts yourself; you only need to move the mouse to the edge of the window to achieve split-screen. However, it shares the same drawback as Magnet: each time you open a new window, you still need to manually implement split-screen, which is often forgotten when you're busy or have many windows open, making it inconvenient to manage.

![bettertouchtool_setting](https://image.pseudoyu.com/images/bettertouchtool_setting.png)

Since existing software couldn't fully meet my needs, as a programmer who loves to tinker, I turned my attention to some highly customizable solutions from the open-source community.

## Open Source Solutions

### Hammerspoon

[Hammerspoon](https://www.hammerspoon.org) is a powerful macOS automation tool that can implement window management functions by writing some lua scripts, and can customize shortcuts. In addition to window management, it can also implement rich functions such as sleep control and clipboard tools. After configuring and using it for a while, I found that, similar to Magnet, it couldn't effectively implement intelligent split-screen (perhaps there are ready-made scripts, but it's troublesome to configure many applications individually), so I abandoned it as well.

### yabai + skhd

After some research, I found a solution from YouTuber [Josh Medeski](https://www.youtube.com/c/JoshMedeski)'s video <[Blazing Fast Window Management on macOS](https://www.youtube.com/watch?v=fYsCAOfGjxE)>. It's open-source, free, highly customizable, and only requires one configuration file to perfectly meet all my needs.

#### yabai

[yabai](https://github.com/koekeishiya/yabai) is an open-source extension of macOS's built-in window management tool that allows free control of windows and multiple displays through command-line tools. Its main feature is the use of the `binary space partitioning` algorithm to automatically modify window layout, allowing us to focus on window content without needing active management. We only need to open the corresponding application window to achieve automatic arrangement, without disrupting our workflow.

#### skhd

[skhd](https://github.com/koekeishiya/skhd) is a macOS shortcut management tool that can call and bind other programs/commands through configuration files, such as yabai's window management commands, to achieve highly customized window operations. skhd's implementation is very performance-focused, with fast response times.

## My Window Management Configuration

### yabai

#### Installation and Basic Configuration

yabai is easy to install, just follow the instructions in its [official wiki](https://github.com/koekeishiya/yabai/wiki/Installing-yabai-(latest-release)).

I personally recommend installation through [brew](https://brew.sh). If you haven't installed `brew` before, you can first install it through the official one-click script.

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installing `brew`, you can continue with installation and basic configuration through commands. Open the terminal and enter the following commands:

```sh
brew install koekeishiya/formulae/yabai
```

Install the script plugin:

```sh
sudo yabai --install-sa
sudo yabai --load-sa
```

Start the yabai service:

```sh
brew services start yabai
```

Note: For macOS Big Sur or Monterey systems, because API injection is needed to call scripts, you need to configure `root` permissions and startup at boot. The official also provides detailed operation methods:

Edit the `/private/etc/sudoers.d/yabai` file:

```sh
sudo visudo -f /private/etc/sudoers.d/yabai
```

Add the following content to the opened file:

```sh
<user> ALL = (root) NOPASSWD: <path> --load-sa
```

The `user` and `path` inside the `<>` above can be obtained through the `whoami` and `which yabai` commands.

![see_user_and_config_yabai_sudo](https://image.pseudoyu.com/images/see_user_and_config_yabai_sudo.png)

After completing the above configuration, add the following two lines to the `.yabairc` configuration file of yabai:

```plaintext
sudo yabai --load-sa
yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"
```

#### Custom Configuration

yabai's configuration file is managed by the `.yabairc` file in the user's `$HOME` directory, which can be edited through an editor or command-line tool:

```sh
vi ~/.yabairc
```

The following is my personal configuration, which you can copy and customize. I have placed my personal configuration on the GitHub code hosting platform, which you can view [here](https://github.com/pseudoyu/dotfiles/blob/master/yabai/yabairc).

```plaintext
# !/usr/bin/env sh

sudo yabai --load-sa
yabai -m signal --add event=dock_did_restart action="sudo yabai --load-sa"

# Global configuration
yabai -m config mouse_follows_focus          off
yabai -m config focus_follows_mouse          off
yabai -m config window_origin_display        default
yabai -m config window_placement             second_child
yabai -m config window_topmost               off
yabai -m config window_shadow                on
yabai -m config window_opacity               off
yabai -m config active_window_opacity        1.0
yabai -m config normal_window_opacity        0.90
yabai -m config window_border                off
yabai -m config window_border_width          6
yabai -m config active_window_border_color   0xff775759
yabai -m config normal_window_border_color   0xff555555
yabai -m config insert_feedback_color        0xffd75f5f
yabai -m config split_ratio                  0.50
yabai -m config auto_balance                 off
yabai -m config mouse_modifier               fn
yabai -m config mouse_action1                move
yabai -m config mouse_action2                resize
yabai -m config mouse_drop_action            swap

# Space configuration
yabai -m config layout                       bsp
yabai -m config top_padding                  15
yabai -m config bottom_padding               15
yabai -m config left_padding                 15
yabai -m config right_padding                15
yabai -m config window_gap                   15

# Ignored apps
yabai -m rule --add app="^System Preferences$" manage=off
yabai -m rule --add app="^Archive Utility$" manage=off
yabai -m rule --add app="^Logi Options+$" manage=off
yabai -m rule --add app="^Alfred Preferences$" manage=off
```

My configuration is basically only partially modified based on the example provided officially, using the `bsp` algorithm for intelligent split-screen, and adjusting the space to 15, which is more comfortable spacing.

I also added some custom rules to ignore applications that cannot customize windows when opening system configurations, decompression tools, etc.

The overall presentation is as follows (the following effect is the algorithm automatically arranging after opening application windows, and new windows will be automatically rearranged):

![my_layout_1](https://image.pseudoyu.com/images/my_layout_1.png)

### skhd

After configuring yabai, we have achieved intelligent split-screen, but sometimes the window positions provided by the algorithm do not meet our needs, or we need to frequently switch/adjust between various windows. That's where we need to use the skhd tool to customize some shortcut configurations.

#### Installation

skhd can also be installed through the `brew` package management tool, which is very convenient:

```sh
brew install koekeishiya/formulae/skhd
```

Start it after installation:

```sh
brew services start skhd
```

#### Custom Configuration

Similar to yabai, skhd's configuration is managed through the `$HOME/.skhdrc` configuration file, which can be edited through an editor or command-line tool.

```sh
vi ~/.skhdrc
```

The following is my personal configuration, which you can copy and customize. I have placed my personal configuration on the GitHub code hosting platform, which you can view [here](https://github.com/pseudoyu/dotfiles/blob/master/skhd/skhdrc).

```plaintext
# Window focus
alt - h : yabai -m window --focus west
alt - j : yabai -m window --focus south
alt - k : yabai -m window --focus north
alt - l : yabai -m window --focus east

# Swap windows
shift + alt - h : yabai -m window --swap west
shift + alt - j : yabai -m window --swap south
shift + alt - k : yabai -m window --swap north
shift + alt - l : yabai -m window --swap east

# Move windows
shift + alt + ctrl - h : yabai -m window --warp west
shift + alt + ctrl - h : yabai -m window --warp south
shift + alt + ctrl - h : yabai -m window --warp north
shift + alt + ctrl - h : yabai -m window --warp east

# Rotate window layout
alt - r : yabai -m space --rotate 90

# Full screen
alt -f : yabai -m window --toggle zoom-fullscreen

# Set/unset window space
alt - g : yabai -m space --toggle padding; yabai -m space --toggle gap

# Float window to screen center / unfloat window
alt - t : yabai -m window --toggle float;\
          yabai -m window --grid 4:4:1:1:2:2

# Modify window split method
alt - e : yabai -m window --toggle split

# Reset window layout
shift + alt - 0 : yabai -m space --balance

# Move window to specific desktop
shift + alt - 1 : yabai -m window --space 1; yabai -m space --focus 1
shift + alt - 2 : yabai -m window --space 2; yabai -m space --focus 2
shift + alt - 3 : yabai -m window --space 3; yabai -m space --focus 3
shift + alt - 4 : yabai -m window --space 4; yabai -m space --focus 4
shift + alt - 5 : yabai -m window --space 5; yabai -m space --focus 5
shift + alt - 6 : yabai -m window --space 6; yabai -m space --focus 6
shift + alt - 7 : yabai -m window --space 7; yabai -m space --focus 7
shift + alt - 8 : yabai -m window --space 8; yabai -m space --focus 8
shift + alt - 9 : yabai -m window --space 9; yabai -m space --focus 9

# Increase window size
shift + alt - w : yabai -m window --resize top:0:-20
shift + alt - d : yabai -m window --resize left:-20:0

# Decrease window size
shift + alt - s : yabai -m window --resize bottom:0:-20
shift + alt - a : yabai -m window --resize top:0:20
```

In simple terms, I configured a setup similar to vim shortcut operation logic, implementing the following common functions:

- `<Option> + hjkl` to focus between different windows
- `<Option> + <Shift> + hjkl` to swap different windows
- `<Option> + <Shift> + 0` to reset window layout
- `<Option> + <Shift> + <1~9>` to quickly move the current window to a specific desktop
- `<Option> + f` for full screen
- `<Option> + t` to float window to screen center / unfloat window
- `<Option> + g` to set/unset window space
- `<Option> + r` to rotate window layout
- `<Option> + e` to modify window split method

Among these, `hjkl` are commonly used operations in the vim editor. You can also modify them to up, down, left, right, or other keys you prefer.

After completing the above configuration, we have achieved yabai intelligent window management and window operations through simple shortcuts. Next, let's make some configurations to the macOS system to optimize our window management system.

### macOS Desktop Management

macOS provides powerful multi-desktop management functionality. Each desktop area can be understood as a workspace where different windows can be placed independently, as shown in the following image:

![macos_desktop_management](https://image.pseudoyu.com/images/macos_desktop_management.png)

We can use desktops to distinguish our work areas, such as using Desktop 1 for development IDEs and terminals, Desktop 2 for browser queries and document writing, Desktop 3 for handling WeChat, email, and other communication tools, and Desktop 4 for leisure and entertainment, video playback, etc. This way, we only need to switch between a few desktops to implement our workflow logic without worrying about window focus issues.

To further optimize and switch between desktops more quickly, we can use launchers like [Alfred](https://www.alfredapp.com) or [Raycast](https://www.raycast.com) to quickly launch/focus applications, or use shortcuts provided by window switching software like [AltTab](https://alt-tab-macos.netlify.app) or [Manico](https://manico.im) to quickly switch between open applications.

In addition, the macOS system settings also provide customizable switching shortcuts. I modified `<Option> + <1~9>` to specific desktops, so when I'm working, I can quickly get to the corresponding workspace by pressing the corresponding shortcut, which quickly becomes muscle memory.

Open **System Preferences - Keyboard - Shortcuts - Mission Control**, where we can set corresponding shortcuts for different desktops. If they don't show up, you can first open 9 empty desktops to configure, and the configuration will be retained even after closing the desktops.

![keyboardshortcut_to_change_desktop](https://image.pseudoyu.com/images/keyboardshortcut_to_change_desktop.png)

Additionally, there's another small setting I like. Open **System Preferences - Accessibility - Display - Display - Reduce motion**. This will reduce the animation effect when switching between different desktops, increasing switching speed. Combined with our automatic split-screen and shortcuts, this achieves fast and powerful multi-workspace switching. I prioritize speed and efficiency, but if you enjoy macOS animations, you can skip this step.

![reduce_display_effect](https://image.pseudoyu.com/images/reduce_display_effect.png)

## Conclusion

The above is my current macOS window management solution. I'm someone who loves to tinker with software and various configurations, often spending several days troubleshooting a small requirement, always pursuing my best practices.

Perhaps many configurations won't save me a lot of time in my subsequent work, with window organization and switching only differing by a few seconds. But when I use the system I once spent a lot of thought researching and optimizing in my daily work and study, or when a sudden need uses a software/configuration I previously tinkered with, I feel inexplicably happy and accomplished. This is probably the meaning of tinkering, and I hope everyone can enjoy such happiness.

I maintain a toolbox project on GitHub 『[GitHub - pseudoyu/yu-tools](https://github.com/pseudoyu/yu-tools)』, which records many other software and hardware choices, and is constantly being updated and optimized. If you're interested, feel free to communicate, and I will gradually produce corresponding configuration/usage tutorials.

> Note: This article was first published by me on 『[少数派](https://sspai.com)』 with authorization. The original article address is: 『[让窗口管理也能自动化，基于 yabai+skhd 的 macOS 窗口管理系统](https://sspai.com/post/73620)』.

## References

> 1. [Blazing Fast Window Management on macOS](https://www.youtube.com/watch?v=fYsCAOfGjxE)
> 2. [yabai project address](https://github.com/koekeishiya/yabai)
> 3. [skhd project address](https://github.com/koekeishiya/skhd)
> 4. [pseudoyu/yu-tools personal toolbox project address](https://github.com/pseudoyu/yu-tools)
