from crypto import getPrice
from headers import headers

data = headers.header("minelounge.org")
data.update({
    "test": "test",
    "test2": "test2"

})
print(data)
