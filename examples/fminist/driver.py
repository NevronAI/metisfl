
from metisfl.driver.driver_session import DriverSession
from env import env
import json

session = DriverSession(env)

res = session.run()
print(res)
with open('result.json', 'w') as f:
    json.dump(res, f)
