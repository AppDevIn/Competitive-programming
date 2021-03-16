# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/
class Codec:
    
    link = "http://tinyurl.com/"
    dictionary = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.dictionary.keys():
            id = str(len(self.dictionary))
            self.dictionary[longUrl] = id
            return self.link + id
        else:
            id = self.dictionary.get(id)
            return self.link + id
            
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        id = shortUrl.split("/")[-1]
        url = list(self.dictionary.keys())[int(id)]
        return url
        
codec = Codec()
codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))