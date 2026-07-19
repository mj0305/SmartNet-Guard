#!/usr/bin/env python3
import subprocess, os, requests, sys

SNAPSHOT_PATH = "/tmp/auth_frame.jpg"
ADMIN_IMAGE_PATH = "/home/mj/admin.jpg"

# ⚠️ 这里变了！指向你刚才搭建的本地微服务 API
LOCAL_API_URL = "http://127.0.0.1:8088/compare"

# 依然使用 rpicam-still 预览 5 秒并抓拍
CAPTURE_CMD = ["rpicam-still", "-t", "5000", "--width", "640", "--height", "480", "-o", SNAPSHOT_PATH]

def main():
    if not os.path.exists(ADMIN_IMAGE_PATH):
        print("DENIED: NO_ADMIN_PHOTO")
        sys.exit(0)
        
    try:
        # 1. 清理旧缓存并抓拍
        if os.path.exists(SNAPSHOT_PATH):
            os.remove(SNAPSHOT_PATH)
        subprocess.run(CAPTURE_CMD, capture_output=True, timeout=15)
        
        if not os.path.exists(SNAPSHOT_PATH):
            print("DENIED: CAMERA_ERROR")
            return

        # 2. 调用本地的 InsightFace API
        with open(ADMIN_IMAGE_PATH, 'rb') as f1, open(SNAPSHOT_PATH, 'rb') as f2:
            files = {'image_file1': f1, 'image_file2': f2}
            # 设置 timeout 长一点，树莓派纯 CPU 推理可能需要 1-2 秒
            response = requests.post(LOCAL_API_URL, files=files, timeout=40)
            res = response.json()

        # 3. 解析结果 (与之前逻辑完全一样，无缝对接 Node-RED)
        if "error_message" in res:
            print(f"DENIED: {res['error_message']}")
        elif "confidence" in res:
            conf = res['confidence']
            # InsightFace 的余弦相似度百分比，通常大于 40 就是同一个人了
            # 我们设定 45 分为安全阈值
            if conf >= 45:
                print("AUTHORIZED:mj")
            else:
                print(f"DENIED:UNKNOWN_FACE_SCORE_{conf:.1f}")
        else:
            print("DENIED: UNKNOWN_ERROR")
            
    except Exception as e:
        # 报错 ConnectionRefusedError 说明你忘了开 local_face_api.py
        print(f"DENIED: {repr(e)}")

if __name__ == "__main__":
    main()
