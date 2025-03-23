# Open Web RSR

ממשק משתמש web עבור מודל Llama עם תמיכה ב-Jenkins CI/CD.

## דרישות מערכת

- Python 3.9 ומעלה
- Docker
- Jenkins
- Ollama
- מודל Llama

## התקנה

1. שיבוט המאגר:
```bash
git clone git@github.com:ugs1311/open-web-rsr.git
cd open-web-rsr
```

2. יצירת סביבה וירטואלית:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. התקנת תלויות:
```bash
pip install -r requirements.txt
```

4. הגדרת משתני סביבה:
```bash
cp .env.example .env
# ערוך את הקובץ .env עם ההגדרות המתאימות
```

## הפעלה

### פיתוח מקומי

1. הפעלת Ollama:
```bash
ollama --model llama.bin --port 11010
```

2. הפעלת האפליקציה:
```bash
python app.py
```

### באמצעות Docker

1. בניית תמונת Docker:
```bash
docker build -t open-web-rsr .
```

2. הפעלת הקונטיינר:
```bash
docker run -p 5000:5000 -p 11010:11010 open-web-rsr
```

## בדיקות

הרצת בדיקות:
```bash
pytest
```

הרצת בדיקות עם כיסוי קוד:
```bash
pytest --cov=app tests/
```

## CI/CD

הפרויקט משתמש ב-Jenkins לתהליך CI/CD. התהליך כולל:
- בדיקת איכות קוד
- בדיקות אוטומטיות
- בניית תמונת Docker
- דיפלוי אוטומטי

## ניטור

האפליקציה כוללת:
- בדיקות בריאות (health checks)
- לוגים מפורטים
- מדדי ביצועים

## אבטחה

- שימוש במשתמש לא-root ב-Docker
- הגדרות אבטחה בסיסיות
- תמיכה ב-HTTPS

## תרומה

1. Fork את המאגר
2. צור branch חדש (`git checkout -b feature/amazing-feature`)
3. Commit את השינויים (`git commit -m 'Add amazing feature'`)
4. Push ל-branch (`git push origin feature/amazing-feature`)
5. פתח Pull Request

## רישיון

פרויקט זה מופץ תחת רישיון MIT. ראו קובץ `LICENSE` לפרטים נוספים. 