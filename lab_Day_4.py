# Question One
import requests


class QueueDataStructure:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Warning: Queue is empty")
            return None
        else:
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


q = QueueDataStructure()

q.insert(1)
q.insert(2)
q.insert(3)
print()
print(q.pop())  # Output: 1
print(q.pop())  # Output: 2
print(q.is_empty())  # Output: False
print(q.pop())  # Output: 3
print(q.is_empty())  # Output: True
print(q.pop())


# Question Two
class QueueName(QueueDataStructure):
    allQueues = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        self.queue = []
        self.allQueues[name] = self.queue

    def appending(self, value):
        if len(self.queue) == self.size:
            raise Exception("Queue is full")
        self.queue.append(value)

    def removing(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    @classmethod
    def getQueueByName(cls, name):
        return cls.allQueues.get(name)


nameQueueObjectOne = QueueName("Youssef", 6)

nameQueueObjectOne.appending(10)
nameQueueObjectOne.appending(11)
nameQueueObjectOne.appending(12)
nameQueueObjectOne.appending(13)
nameQueueObjectOne.appending(14)
nameQueueObjectOne.appending(15)
# nameQueueObjectOne.appending(16) # Raise error (the queue is full)


nameQueueObjectTwo = QueueName("Alaa", 3)

nameQueueObjectTwo.appending("Youssef")
nameQueueObjectTwo.appending("Alaa")
nameQueueObjectTwo.appending("Youssef")


print(f"Dicrionary With keys and values: {QueueName.allQueues}")
print("values by key Youssef", QueueName.getQueueByName("Youssef"))
print("values by key Alaa", QueueName.getQueueByName("Alaa"))


# Question Three


class WeatherApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.weatherapi.com/v1/"

    def get_current_temperature(self, city):
        endpoint = "current.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.base_url + endpoint, params=params)
        data = response.json()
        temperature = data["current"]["temp_c"]
        return temperature

    def get_lat_and_long(self, city):
        endpoint = "current.json"
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.base_url + endpoint, params=params)
        data = response.json()
        latitude = data["location"]["lat"]
        longitude = data["location"]["lon"]
        return latitude, longitude


weather = WeatherApiClient("84d5eff3327c4a6ab7d203114231602")

print(weather.get_current_temperature("minia"))
print(weather.get_lat_and_long("minia"))
