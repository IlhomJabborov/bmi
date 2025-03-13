# O'zbek Tilidagi Stopwordlarni Aniqlovchi API

Bu loyiha O'zbek tilidagi stopwordlarni aniqlash va ularni matndan olib tashlash uchun FastAPI asosida yaratilgan. Loyiha open-source bo'lib, istalgan dasturchi uni rivojlantirishga hissa qo'shishi mumkin.

## 🚀 Loyihaning Maqsadi
O'zbek tilida matnlarni tozalash va stopwordlarni tahlil qilish uchun API yaratish. Bu dastur orqali foydalanuvchilar berilgan matndan stopwordlarni ajratib olishi yoki ularni matndan olib tashlashi mumkin.

## 🛠 O'rnatish
Loyihani yuklab olish va ishlatish uchun quyidagi amallarni bajaring:

### 1. Repositoryni klonlash
```sh
  git clone https://github.com/username/stopword-api.git
  cd stopword-api
```

### 2. Virtual muhit yaratish va kutubxonalarni o'rnatish
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Kerakli kutubxonalarni o'rnatish
```sh
pip install -r requirements.txt
```

### 4. SpaCy modelini yuklash
```sh
python -m spacy download xx_ent_wiki_sm
```

### 5. Serverni ishga tushirish
```sh
uvicorn main:app --reload
```

Server ishga tushirilgandan so'ng, API quyidagi manzilda ishlaydi:
```
http://127.0.0.1:8000
```

## 📡 API dan foydalanish
### 1. Matndan stopwordlarni olib tashlash

#### Endpoint:
```http
POST /process_text/
```

#### Kirish (Input):
```json
{
  "text": "Bu mening birinchi open-source loyiham. Men uni sinab ko'rmoqchiman."
}
```

#### Chiqish (Output):
```json
{
  "filtered_text": "Mening birinchi open-source loyiham. Men sinab ko'rmoqchiman.",
  "removed_stopwords": {
    "bu": 1,
    "uni": 1
  },
  "total_stopwords": 2
}
```

## 🌍 Open Source va Hissa Qo'shish
Ushbu loyiha ochiq manbali (open-source) bo'lib, quyidagilarga ochiq:
- Backend funksiyalarini yaxshilash
- Frontend interfeys yaratish (sayt, Telegram bot, mobil ilova)
- API imkoniyatlarini kengaytirish

### 🔥 Hissa Qo'shish Tartibi
1. Repositoryni fork qiling.
2. O'zgarishlarni amalga oshiring va commit qiling.
3. Pull request yuboring.

Agar sizda biror taklif yoki savol bo'lsa, muhokamalar bo'limida baham ko'ring yoki issue yarating.

## 📝 Litsenziya
Bu loyiha [MIT litsenziyasi](LICENSE) asosida tarqatiladi.
