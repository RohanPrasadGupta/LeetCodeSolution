class Codec:

    def __init__(self):
        self.encodeDic = {}
        self.decodeDic = {}
        self.base = "http://timyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeDic:
            shortUrl = self.base + str(len(self.encodeDic))
            self.encodeDic[longUrl] = shortUrl
            self.decodeDic[shortUrl] = longUrl
        
        return self.encodeDic[longUrl]        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeDic[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))