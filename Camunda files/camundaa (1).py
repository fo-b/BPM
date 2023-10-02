import requests
import json



# Camunda REST API endpoint to start a new process instance
camunda_endpoint = "http://localhost:8080/engine-rest/process-definition/key/Process_1drnqb6/start"

# Process definition key for the process you want to start
process_definition_key = "Process_1drnqb6"

# Variables to pass to the process instance (if needed)
backpack = 15
variables = {
    "titts": {"value": "BIIIG", "type": "String"},
    "age": {"value": 16, "type": "Integer"},
    "weight": {"value": 45 - backpack, "type": "Integer"}
}
list = []

# Payload for starting a new process instance
payload = {
    "variables": variables
}

headers = {
    "Content-Type": "application/json"
}

for jalla in range(1, 5):
    variables['weight']['value'] = 90 + jalla

    response = requests.post(
        camunda_endpoint,
        data=json.dumps(payload),
        headers=headers
    )

    id_value = response.json().get('id')

    list.append(id_value)

    with open("log.txt", "a") as file:
        file.write(str(id_value)+ '\n')

    if response.status_code == 200:
        print("Process instance started successfully.")
    else:
        print(f"Failed to start process instance. Status code: {response.status_code}")
        print(f"Response content: {response.text}")

    #print(jalla)





