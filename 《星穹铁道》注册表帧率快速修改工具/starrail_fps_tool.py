# save_as: starrail_fps_tool.py
"""
《星穹铁道》帧率修改控制台工具 版本 1.0
用法：
  以管理员身份运行cmd执行:
    starrail_fps_tool.py [目标帧率]

示例：
  starrail_fps_tool.py 120      # 设置为120帧
  starrail_fps_tool.py --revert # 恢复默认60帧
"""
import winreg
import ctypes
import sys
import argparse

# 配置区（根据实际情况修改）
REG_PATH = r"Software\miHoYo\崩坏：星穹铁道"
VALUE_NAME = "GraphicsSettings_Model_h2986158309"
DEFAULT_FPS = 60


def is_admin():
    """检查管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def modify_fps(target_fps):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            # 读取原始值和类型
            original_value, reg_type = winreg.QueryValueEx(key, VALUE_NAME)

            # 类型处理逻辑
            if reg_type == winreg.REG_BINARY:
                # 将bytes转为字符串处理
                decoded_value = original_value.decode('utf-8', errors='ignore')
                modified_str = decoded_value.replace(f"FPS\":{DEFAULT_FPS}", f"FPS\":{target_fps}")
                modified_value = modified_str.encode('utf-8')
            elif reg_type == winreg.REG_SZ:
                modified_str = original_value.replace(f"FPS\":{DEFAULT_FPS}", f"FPS\":{target_fps}")
                modified_value = modified_str
            else:
                print(f"❌ 不支持的注册表类型: {reg_type}")
                return

            # 写入新值
            winreg.SetValueEx(key, VALUE_NAME, 0, reg_type, modified_value)
            print(f"✅ 成功设置为 {target_fps} 帧！")

    except Exception as e:
        print(f"❌ 错误: {str(e)}")
        sys.exit(1)


def revert_default():
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            original_value, reg_type = winreg.QueryValueEx(key, VALUE_NAME)
            modified_value = original_value.replace(f"FPS\":120", f"FPS\":{DEFAULT_FPS}").replace(f"FPS\":144",
                                                                                                  f"FPS\":{DEFAULT_FPS}")
            winreg.SetValueEx(key, VALUE_NAME, 0, reg_type, modified_value)
            print(f"✅ 已恢复默认 {DEFAULT_FPS} 帧")
    except Exception as e:
        print(f"❌ 恢复失败: {str(e)}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='星穹铁道帧率修改工具')
    parser.add_argument('fps', type=int, nargs='?', help='目标帧率数值 (目前只支持 120)')
    parser.add_argument('--revert', action='store_true', help='恢复默认帧率')
    args = parser.parse_args()

    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{sys.argv[0]}"', None, 1)
        sys.exit()

    print("\n★ 操作前请确认：")
    print("1. 已备份注册表（应该没问题）")
    print("2. 游戏已完全关闭\n")

    if args.revert:
        revert_default()
    elif args.fps:
        if args.fps < 60 or args.fps > 360:
            print("❌ 帧率范围应为60-360")
            sys.exit(1)
        modify_fps(args.fps)
        print("\n💡 修改完成后请重启游戏验证效果")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()