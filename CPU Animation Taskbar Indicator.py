import sys
import time
import threading
from PIL import Image, ImageDraw, ImageSequence
import psutil
import pystray

class CpuAnimator:
    def __init__(self):
        # 动画帧列表
        self.frames = []
        # 当前帧索引
        self.current_frame = 0
        # 动画速度（毫秒）
        self.animation_speed = 10
        # 最小速度（CPU 0%时）
        self.min_speed = 1000
        # 最大速度（CPU 100%时）
        self.max_speed = 10
        # 当前CPU使用率
        self.cpu_percent = 0
        # 是否运行动画
        self.running = True
        # 创建动画帧
        self.create_frames()

        # 创建系统托盘图标
        self.icon = pystray.Icon("cpu_animator", self.frames[0], "CPU Monitor")
        self.icon.menu = pystray.Menu(
            pystray.MenuItem(f"CPU: {self.cpu_percent}%", lambda: None),
            pystray.MenuItem("Exit", self.exit_program)
        )

    def get_cpu_color(self, percent):
        """根据CPU使用率返回颜色"""
        if percent < 30:
            return "green"
        elif percent < 60:
            return "blue"
        elif percent < 80:
            return "yellow"
        else:
            return "red"

    def create_frames(self):
        """创建动画帧"""
        # 简单的旋转动画
        size = 64
        for i in range(8):
            angle = i * 45
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            # 根据CPU使用率获取颜色
            color = self.get_cpu_color(self.cpu_percent)

            # 绘制旋转箭头
            draw.pieslice([10, 10, size - 10, size - 10], angle - 30, angle + 30, fill=color)
            self.frames.append(img)

    def update_frames_color(self):
        """更新所有帧的颜色"""
        size = 64
        self.frames = []
        for i in range(8):
            angle = i * 45
            img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)

            color = self.get_cpu_color(self.cpu_percent)
            draw.pieslice([10, 10, size - 10, size - 10], angle - 30, angle + 30, fill=color)
            self.frames.append(img)

    def update_animation_speed(self):
        """根据CPU使用率更新动画速度"""
        while self.running:
            # 获取CPU使用率
            self.cpu_percent = psutil.cpu_percent(interval=1)

            # 更新菜单显示
            self.icon.menu = pystray.Menu(
                pystray.MenuItem(f"CPU: {self.cpu_percent}%", lambda: None),
                pystray.MenuItem("Exit", self.exit_program)
            )

            # 更新帧颜色
            self.update_frames_color()

            # 计算新的动画速度（CPU越高，速度越快）
            speed_range = self.min_speed - self.max_speed
            self.animation_speed = self.min_speed - (speed_range * (self.cpu_percent / 100))

            # 限制速度在合理范围内
            self.animation_speed = max(self.max_speed, min(self.min_speed, self.animation_speed))

            # 每秒更新一次
            time.sleep(1)

    def animate(self):
        """运行动画循环"""
        while self.running:
            # 更新图标
            if self.frames:
                self.icon.icon = self.frames[self.current_frame]

                # 前进到下一帧
                self.current_frame = (self.current_frame + 1) % len(self.frames)

                # 根据当前速度等待
                time.sleep(self.animation_speed / 1000)
            else:
                time.sleep(0.1)

    def exit_program(self):
        """退出程序"""
        self.running = False
        self.icon.stop()

    def run(self):
        """启动程序"""
        # 启动CPU监控线程
        cpu_thread = threading.Thread(target=self.update_animation_speed, daemon=True)
        cpu_thread.start()

        # 启动动画线程
        anim_thread = threading.Thread(target=self.animate, daemon=True)
        anim_thread.start()

        # 运行系统托盘图标
        self.icon.run()


if __name__ == "__main__":
    animator = CpuAnimator()
    animator.run()