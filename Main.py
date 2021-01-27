import requests
import os

from Utils.Fingerprint import Fingerprint
from Utils.Files import Files
from Utils.CdnUrl import CdnUrl


class Main:
    def __init__(self):
        self.game = 'brawl stars'
        self.cdn_url = CdnUrl.get_url(self, self.game)


    def initialize(self):
        if os.path.exists('fingerprint.json'):

            json_data = open('fingerprint.json', 'r').read()
            fingerprint = Fingerprint.info(self, json_data)

            print(f"Version: {fingerprint[2]}")
            print(f"SHA:     {fingerprint[1]}\n")


            for file in Files.get_all(self, json_data):
                self.download(fingerprint[1], file)

        else:
            print("fingerprint.json not found.")



    def download(self, fingerprintSha, file):
        url = f"{self.cdn_url}/{fingerprintSha}/{file}"
        folder, name = os.path.split(file)
        full_path = f"{fingerprintSha}/{folder}/{name}"

        if not os.path.isdir(fingerprintSha):
            os.mkdir(fingerprintSha)

        if not os.path.isdir(folder):
            if not os.path.exists(f"{fingerprintSha}/{folder}"):
                os.makedirs(f"{fingerprintSha}/{folder}")

        data = requests.get(url).content

        open(os.path.join(full_path), 'wb').write(data)

        print((f"Downloaded {file}"))



if __name__ == "__main__":
   AssetsDownloader = Main()
   AssetsDownloader.initialize()


