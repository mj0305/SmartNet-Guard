#!/usr/bin/env python3
import sys
import time
from RPLCD.i2c import CharLCD

# 你的 I2C 地址 (0x27 或 0x3f)
I2C_ADDR = 0x27 

try:
    # 初始化 20x4 LCD
    lcd = CharLCD('PCF8574', I2C_ADDR, port=1, cols=20, rows=4, charmap='A02', dotsize=8)
    
    if len(sys.argv) > 1:
        raw_text = sys.argv[1]
        lines = raw_text.split('\\n')
        
        # 修复乱码核心：绝不使用 lcd.clear()！
        # 直接利用 Node-RED 传来的 20 字符定长字符串进行“完美覆盖写入 (Overwrite)”
        
        if len(lines) > 0:
            lcd.cursor_pos = (0, 0)
            lcd.write_string(lines[0][:20])
            
        if len(lines) > 1:
            lcd.cursor_pos = (1, 0)
            lcd.write_string(lines[1][:20])
            
        if len(lines) > 2:
            lcd.cursor_pos = (2, 0)
            lcd.write_string(lines[2][:20])
            
        if len(lines) > 3:
            lcd.cursor_pos = (3, 0)
            lcd.write_string(lines[3][:20])
            
            # 🌟 危险爆闪核心：检测第四行是否进入熔断拦截状态
            if "LOCKDOWN" in lines[3]:
                # 让 LCD 屏幕背光连续爆闪 3 次
                for _ in range(3):
                    lcd.backlight_enabled = False
                    time.sleep(0.15)
                    lcd.backlight_enabled = True
                    time.sleep(0.15)
                
except Exception as e:
    print(f"LCD Render Error: {e}")
