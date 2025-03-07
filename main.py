from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
from fastapi.middleware.cors import CORSMiddleware

# FastAPI ilovasini yaratish
app = FastAPI()

# CORS (Cross-Origin Resource Sharing) muammolarini hal qilish
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Barcha domenlardan so'rovlarni qabul qilish
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SpaCy ko'p tilli modelini yuklash
nlp = spacy.load("xx_ent_wiki_sm")

def load_stopwords(file_path="uz.txt"):
    """Stop wordslarni fayldan yuklash"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return set(word.strip() for word in f.readlines() if word.strip())
    except FileNotFoundError:
        print(f"Xato: {file_path} fayli topilmadi!")
        return set()
    except UnicodeDecodeError:
        print("Xato: Faylni UTF-8 kodirovkasida o'qib bo'lmadi!")
        return set()

# Stop wordsni yuklash
stopword_list = load_stopwords("uz.txt")

class TextRequest(BaseModel):
    text: str

def tokenize_text(text: str):
    """Matnni tokenlarga ajratish"""
    return [token.text for token in nlp(text)]

def filter_stopwords(text: str, stopwords: set):
    """Matndan stop wordslarni olib tashlash"""
    tokens = tokenize_text(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
    return " ".join(filtered_tokens)

def stopword_analysis(text: str, stopwords: set):
    """Matndagi stop wordslarni sanash"""
    tokens = tokenize_text(text)
    stopword_count = {}
    total_stopwords = 0
    
    for word in tokens:
        if word.lower() in stopwords:
            stopword_count[word] = stopword_count.get(word, 0) + 1
            total_stopwords += 1
    
    return stopword_count, total_stopwords

@app.post("/process_text/")
def process_text(request: TextRequest):
    """Berilgan matnni stop wordsdan tozalash va statistikani qaytarish"""
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Matn bo'sh bo'lishi mumkin emas")
    
    filtered_text = filter_stopwords(text, stopword_list)
    stopword_stats, total_stopwords = stopword_analysis(text, stopword_list)
    
    return {
        "filtered_text": filtered_text,
        "removed_stopwords": stopword_stats,
        "total_stopwords": total_stopwords
    }
