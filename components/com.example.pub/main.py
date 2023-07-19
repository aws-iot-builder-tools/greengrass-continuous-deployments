import os
import time
import json
import awsiot.greengrasscoreipc.clientv2 as clientV2

TOPIC="CPU/info"

def get_cpu_temp():
    temp_file = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = temp_file.read()
    temp_file.close()
    return float(cpu_temp)/1000

def main():
    # Create an IPC client.
    ipc_client = clientV2.GreengrassCoreIPCClientV2()

    while True:
        cpu_temp = get_cpu_temp()
        print("CPU temperature: {:.2f} C".format(cpu_temp))

        # Create a payload.
        payload = json.dumps({"temperature": cpu_temp})

        # Publish the payload to AWS IoT Core.
        resp = ipc_client.publish_to_iot_core(topic_name=TOPIC, qos="1", payload=payload)

        time.sleep(1)  # sleep for 1 second

    ipc_client.close()

if __name__ == "__main__":
    main()
