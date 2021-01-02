class Codec:
    
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if not hasattr(self, 'd'):
            self.d = {0:""}
        self.d[max(self.d.keys())+1] = longUrl
        return str(max(self.d.keys()))
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
