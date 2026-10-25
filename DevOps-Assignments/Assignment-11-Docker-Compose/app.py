from flask import Flask
import redis
import os

app = Flask(__name__)
cache = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    try:
        count = cache.incr("visits")
        return f"<h1>Docker Compose Flask App</h1><p>Visit count: {count}</p>"
    except redis.RedisError:
        return "<h1>Flask is running, but Redis is unavailable.</h1>", 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
