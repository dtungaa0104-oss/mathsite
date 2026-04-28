# МатемПортал — Математикийн Вэб Сайт

## Суулгах ба Ажиллуулах Заавар

### 1. Python суулгах
Python 3.9+ хувилбар шаардлагатай.
https://www.python.org/downloads/

### 2. Виртуал орчин үүсгэх (санал болгосон)
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### 3. Flask суулгах
```bash
pip install -r requirements.txt
```

### 4. Сайтыг ажиллуулах
```bash
python app.py
```

### 5. Браузерт нээх
```
http://127.0.0.1:5000
```

## Хуудсуудын жагсаалт

| URL              | Хуудас                            |
|------------------|-----------------------------------|
| /                | Нүүр хуудас                       |
| /tools           | Тооцоолол ба График хэрэгслүүд    |
| /engagement      | Тоглоомжуулсан үнэлгээний платформ |
| /learning        | Суралцах эх сурвалжууд            |
| /apps            | Гар утасны аппликейшн             |
| /local           | Монгол контентын сан              |

## Файлын бүтэц
```
mathsite/
├── app.py                  ← Flask апп
├── requirements.txt        ← Python хамаарал
├── templates/
│   ├── base.html           ← Үндсэн загвар (nav, footer)
│   ├── index.html          ← Нүүр хуудас
│   ├── tools.html          ← Хэрэгслүүд
│   ├── engagement.html     ← Тоглоомжуулах
│   ├── learning.html       ← Суралцах
│   ├── apps.html           ← Аппликейшн
│   └── local.html          ← Монгол контент
└── static/
    ├── css/main.css        ← Загвар (стиль)
    └── js/main.js          ← Анимейшн, навигаци
```
