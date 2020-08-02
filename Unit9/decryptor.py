#coding=utf-8
import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key = "MIIEowIBAAKCAQEArRQ560lbOUu/sXiS3plEPZpPCsiw40+Y0jh6FcStgwMRIk0TghveKycuHSYCKdhcCxmTPHQFwDTp4IUmJdLaoKQoshe66l1btPw5lIVR0B7MxSxdDh+VcqF8w4VcRUKdd5gaorBB955/HvkRzDnw9sltiD6mX9Mmd42olxNI54EL8yqkCxjgQPSIgon08QXL+AqEhwt6oPmBilnXcuk76HqMBUaubj4qkhzT5/bMOerabiupn4lgyWKfggqeM8Le6C1LgnZQTryTeIicSygpwaf61MA39X+jEwmiFegQylYkhKyqX2oU+Vq6POQ9oQOtPG5LI4WuuDVMvjyDdeiSwwIDAQABAoIBADmfYUUXUBq8QF7akLMxfcmwpR4nANU8+9kJWoQCze2vSLYNyS/pDUd6rNyhedjqooJDioR28C80rqTET5YKJCWVYcMhKWa7nDueOaFb3YgXqP8ALR71nvDiGMKTlMuuSPS3HC8L1XqWNyZdr/I5XCMdnqzchtGiX80vyXA6yGviO6cVYLO3Rmgn6AbHyhM6apkdGS7zusgYQbxC7R8PnCZiH+pgLyQuC8boHeUCZW3bdLJ5pRkOw+DpeYNL0yZyvKBicKnX85N+o8+yqO56xdVgPxxUEhFJELCr5TYoQW8D9nN8EWqDgEhDfnOA7T/W06dCFQ9xlCqVGiPdTARBTjkCgYEAz84NmYV+Ww5qsfYOrk42OCkAj63p0TxEpY/9Q/Z9axyFGifi+NO7MZOe4ZgVQTtVv27RRAgbAvDLML4LxPVoWZ8Da6cgxSx11zqawv/bcb2g4qEQi4VQ6Wipa50MMTN7ez1gBZku+HDqIvDDUWQoWHsD0kfqGsOLtM4W4BA0pk0CgYEA1Thm5vVZEqHkQufcBu0ZBv7+qnkHRAv1W2QgOrcQuA1XzFHNVaXO5Y2icCtXZQwcoCemznOuvueC+i20dPKVekFlRwtTgj8yAu26r54FIfxIduowcv1i5tcbQottM6n8YEhub4ALs4O8z6yIifQ6sLSJSmmygjOzPb9qSfBwxU8CgYB+MD037cWWG8IUwTuXA22PWu65UT28TmHNPAvq2mK8yXvWL0R4H3L8Hw2LJqQ5kYN3lR7EtjtY5MoulilleDTev13/YGTY9y+z/CWApogmoKVzGaWHY/SHWIQREjQWKJIie1m07JmGSmMTxqqE4VJSsJjYd80kZXyP1do0RAMEvQKBgQCIdXNuBsG96fxjUW6AxEdLMfEcex7KTvj1R4xU54p8sJVrP0MxuE9EnLPEJAjns6uyWA4qfODubs5lfNDMM+C0gJvnrvkAF5/TPgBHmtNgH8zkxhbB0Sb1498fZIo8EWNi35hGJeXXOs2g/6PW3oadRr3C8Qh8ycfCEfpdXdNegwKBgDsOPlzZBw6D02haTMoeIF+RHESM5ZpWQJm2r+ct7P/1K7XLmFKhN8ZrCEKYysstHWwD4AvgGoWW2F3fJxdkewRkLA5zjRkJXR+NmC8hRjPSzIsmV8LRKLmxDnMGoR5YR5lAXhnuwHUBOf02wJH+IW8EJMkDfrr3r66M/gnw5H24"

rsakey = RSA.importKey(private_key)
rsakey = PKCS1_OAEP.new(rsakey)

chunk_size = 256
offset = 0
decrypted = ""
encrypted = base64.b64decode(encrypted)

while offset < len(encrypted):
	decrypted += rsakey.decrypted(encrypted[offset:offset+chunk_size])
	offset += chunk_size

#
plaintext = zlib.decompress(decrypted)

print plaintext