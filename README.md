# CPU 动画任务栏指示器
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

一款轻量级的系统托盘工具，通过动态速度和颜色变化的动画图标实时监控 CPU 使用情况。

## 功能特点 ✨
- 🎨 颜色编码 CPU 状态：
 - 💚 绿色 (0-30%)：系统空闲
 - 💙 蓝色 (30-60%)：正常负载
 - 💛 黄色 (60-80%)：高负载
 - ❤️ 红色 (80-100%)：超负荷
- ⚡ 动态动画速度 - CPU 使用率越高，旋转速度越快
- 📊 显示实时百分比

## 截图 🖼️
| Low Usage (Green) | Medium Usage (Blue) | High Usage (Red) |
|-------------------|---------------------|------------------|
| ![Green](screenshots/green.png) | ![Blue](screenshots/blue.png) | ![Red](screenshots/red.png) |

## 安装 ⚙️
1.**先决条件**：
 - Python 3.7+

- 2.**pip依赖**：
  ```bash
  pip install psutil pystray pillow

## 参与贡献 🤝
欢迎提交 Pull Request！如有重大改动，请先提交 Issue 讨论。


# CPU Animation Taskbar Indicator

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight system tray utility that visually monitors CPU usage through an animated icon with dynamic speed and color changes.

## Features ✨

- 🎨 **Color-coded CPU status**:
  - 💚 Green (0-30%): System idle
  - 💙 Blue (30-60%): Normal load
  - 💛 Yellow (60-80%): High load
  - ❤️ Red (80-100%): Overload
- 📊 **Real-time percentage** in context menu


## Screenshots 🖼️

| Low Usage (Green) | Medium Usage (Blue) | High Usage (Red) |
|-------------------|---------------------|------------------|
| ![Green](screenshots/green.png) | ![Blue](screenshots/blue.png) | ![Red](screenshots/red.png) |

## Installation ⚙️

1. **Prerequisites**:
   - Python 3.7+
   - pip package manager

2. **Install dependencies**:
   ```bash
   pip install psutil pystray pillow


Contributing 🤝
Pull requests are welcome! For major changes, please open an issue first.
