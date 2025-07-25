# 🎵 Spotify Backend Clone

A Django-based backend project that supports:

- 🔄 **Celery** for asynchronous task processing  
- 💾 **Redis** as broker and cache  
- 🐘 **PostgreSQL** as the database  
- 🐳 **Docker** for seamless containerized deployment  

---

## ✅ Prerequisites

Ensure the following tools are installed and running:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/) (comes with Docker Desktop)

---

## 🚀 Getting Started

```bash
git clone https://github.com/DeveshDutt2710/spotify.git
cd spotify

docker-compose up --build
```

This command will launch:

- Django app (`web`)
- Celery worker (`worker`)
- Celery beat scheduler (`beat`)
- Redis (`redis`)
- PostgreSQL (`db`)

---

## 🧪 Populating Fake Data

Once the containers are running, enter the Django shell:

```bash
docker-compose exec web python manage.py shell
```

Inside the shell:

```python
from songs.utils.fake_data import create_fake_songs
create_fake_songs(1000)
```

Then exit:

```python
exit()
```

---

## 🔐 Admin Panel

Open your browser at:

```
http://localhost:8000/admin/
```

If you haven’t created a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 📡 API Endpoints

| Method | URL                                        | Description                  |
|--------|--------------------------------------------|------------------------------|
| GET    | `http://localhost:8000/api/songs/trending-songs/`              | Get trending songs           |
| GET    | `http://localhost:8000/api/songs/trending-songs/:genre/`        | Get top songs per genre      |

---

## 🛠 Tech Stack

- Python 3.9+
- Django 4.2+
- Celery 5+
- Redis 7+
- PostgreSQL
- Docker + Docker Compose

---

## 📄 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).
