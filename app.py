from flask import Flask, request, jsonify
from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import time

app = Flask(__name__)

@dataclass
class Child:
    name: str
    age: int
    ts: float = field(default_factory=time.time)

class KindergartenQueue:
    def __init__(self):
        self._queue: List[Child] = []

    def enqueue(self, name: str, age: int) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Ім'я має бути непорожнім рядком")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Вік має бути додатним цілим числом")
        self._queue.append(Child(name.strip(), age))

    def dequeue(self) -> Optional[Tuple[str, int]]:
        if not self._queue:
            return None
        c = self._queue.pop(0)
        return (c.name, c.age)

    def remove(self, name: str) -> bool:
        for i, c in enumerate(self._queue):
            if c.name == name:
                del self._queue[i]
                return True
        return False

    def get_position(self, name: str) -> Optional[int]:
        for i, c in enumerate(self._queue):
            if c.name == name:
                return i + 1
        return None

    def list_queue(self) -> List[Tuple[str, int]]:
        return [(c.name, c.age) for c in self._queue]

queue = KindergartenQueue()

@app.route("/")
def index():
    return "<h2>Система черги дитсадка працює ✅</h2><p>Використайте /add, /list, /remove, /dequeue у браузері.</p>"

@app.route("/add")
def add_child():
    name = request.args.get("name")
    age = request.args.get("age")
    if not name or not age:
        return "❌ Вкажіть параметри ?name=Ім'я&age=Вік", 400
    try:
        queue.enqueue(name, int(age))
        return f"✅ Дитину {name} (вік {age}) додано до черги."
    except ValueError as e:
        return f"❌ Помилка: {e}", 400

@app.route("/list")
def list_children():
    return jsonify(queue.list_queue())

@app.route("/remove")
def remove_child():
    name = request.args.get("name")
    if not name:
        return "❌ Вкажіть параметр ?name=Ім'я", 400
    if queue.remove(name):
        return f"🗑️ Дитину {name} видалено з черги."
    else:
        return f"⚠️ Дитину {name} не знайдено.", 404

@app.route("/dequeue")
def dequeue_child():
    child = queue.dequeue()
    if child:
        return f"➡️ {child[0]} ({child[1]} р.) пішла/пішов з черги."
    else:
        return "⚠️ Черга порожня."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
