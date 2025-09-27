import requests
import json

def list_ollama_models():
    """查看 Ollama 已安裝的模型"""
    try:
        # 向 Ollama API 發送請求
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        
        data = response.json()
        models = data.get("models", [])
        
        if not models:
            print("❌ 沒有找到任何已安裝的模型")
            return
        
        print("📋 Ollama 已安裝的模型：")
        print("=" * 50)
        
        for model in models:
            name = model.get("name", "未知")
            size = model.get("size", 0)
            modified_at = model.get("modified_at", "未知")
            
            # 轉換大小為可讀格式
            size_mb = size / (1024 * 1024)
            if size_mb > 1024:
                size_str = f"{size_mb/1024:.1f} GB"
            else:
                size_str = f"{size_mb:.1f} MB"
            
            print(f"🔹 模型名稱: {name}")
            print(f"   大小: {size_str}")
            print(f"   修改時間: {modified_at}")
            print("-" * 30)
            
    except requests.exceptions.ConnectionError:
        print("❌ 無法連接到 Ollama 服務")
        print("請確認 Ollama 是否正在運行 (ollama serve)")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

if __name__ == "__main__":
    list_ollama_models()
