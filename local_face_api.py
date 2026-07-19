from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis

app = FastAPI()

# 1. 初始化并加载 InsightFace 模型 (首次运行会自动下载模型，请保持联网)
# 使用 antelopev2 是目前速度和精度非常平衡的轻量级模型
model = FaceAnalysis(name='buffalo_sc', providers=['CPUExecutionProvider'])
model.prepare(ctx_id=0, det_size=(640, 480))

def get_face_embedding(image_bytes):
    # 将接收到的二进制文件转为 OpenCV 图像格式
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # 提取人脸特征
    faces = model.get(img)
    if not faces:
        return None
    # 默认取画面中检测到的第一张脸的特征向量 (512维)
    return faces[0].embedding

@app.post("/compare")
async def compare_faces(image_file1: UploadFile = File(...), image_file2: UploadFile = File(...)):
    try:
        # 读取两张照片
        emb1 = get_face_embedding(await image_file1.read())
        emb2 = get_face_embedding(await image_file2.read())

        if emb1 is None or emb2 is None:
            return {"error_message": "NO_FACE_DETECTED"}

        # 计算余弦相似度 (Cosine Similarity)，范围通常在 -1 到 1 之间
        sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        
        # 将相似度映射到 0~100 的分数（InsightFace 中同一个人通常相似度在 0.4 到 0.8 之间）
        # 这里做一个简单的线性放大，方便和之前的逻辑对齐
        score = max(0, min(100, float(sim) * 100))
        
        return {"confidence": score}
        
    except Exception as e:
        return {"error_message": str(e)}

if __name__ == "__main__":
    import uvicorn
    # 在本地 8000 端口启动服务
    uvicorn.run(app, host="127.0.0.1", port=8088)
