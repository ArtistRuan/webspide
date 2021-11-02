
import json


if __name__ == '__main__':
    test = {
        "animals": {
            "dog": [
                {
                    "name": "Rufus",
                    "age": 15
                },
                {
                    "name": "Marty",
                    # "age": null
                    "age": 20
                }
            ]
        }
    }

    json_str = json.dumps(test)
    dog_msg = json.loads(json_str)
    for msg in dog_msg["animals"]["dog"]:
        print(msg["name"],msg["age"])

