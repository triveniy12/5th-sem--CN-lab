

class Client:
    def __init__(self, rate, data = []):
        self.rate = rate
        self.data = data

    def __str__(self):
        return str([str(self.rate), str(self.data)])


class Buffer:
    def __init__(self, bucket_size = int, bucket = []):
        self.bucket_size = bucket_size
        self.bucket = bucket

    def checkstate(self):
        if len(self.bucket) == 0:
            return True

    def __str__(self):
        return str([str(self.bucket_size), str(self.bucket)])

basestate = True
sec = 1
buffer = Buffer(int(input("Enter bucket size")))
client = Client(int(input("Enter client acceptance rate in bps")))
lost_data = []
data_to_send = str

while basestate:
    data_to_send = input("Enter a string send by the server")
    count = 0
    if buffer.checkstate():
        for i in range(0, len(data_to_send)):
            if i < client.rate:
                client.data.append(data_to_send[i])
            else:
                if count < buffer.bucket_size:
                    buffer.bucket.append(data_to_send[i])
                    count = len(buffer.bucket)
                else:
                    lost_data.append(data_to_send[i])
        if lost_data:
            print("data Lost due to collision")
            for i in lost_data:
                print(i, end="")
    else:
        j=0
        for i in range(0, len(data_to_send)+len(buffer.bucket)):
            if i < client.rate:
                if len(buffer.bucket):
                    client.data.append(buffer.bucket[0])
                    del buffer.bucket[0]
                else:
                    client.data.append(data_to_send[j])
                    j += 1
            else:
                if len(buffer.bucket) <= buffer.bucket_size:
                    if j < len(data_to_send):
                        buffer.bucket.append(data_to_send[j])
                        j += 1
                else:
                    if j < len(data_to_send):
                        j += 1
                        lost_data.append(data_to_send[i])
        if lost_data:
            print("data Lost due to collision")
            for i in lost_data:
                print(i, end="")

    print("BUFFER SIZE: "+str(buffer.bucket_size))
    if buffer.bucket:
        print("contents stored in the bucket")
        for i in buffer.bucket:
            print(i, end="")
    print(" ")
    print("rate at which data is sent: "+str(client.rate))
    if client.data:
        print("contents successfully sent :")
        for i in client.data:
            print(i, end="")
    print(" ")

