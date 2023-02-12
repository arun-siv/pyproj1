#%%
import pandas as pd
import requests
#%%

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.6',
    'cookie': 'nsit=zqfxcCb5aDhVl8Ep5LviDEpP; AKA_A2=A; defaultLang=en; ak_bmsc=FA5130D59C6A4D6DEBC51594858F19EB~000000000000000000000000000000~YAAQQ3xBF6C59T+GAQAAqhUNRhKtDoY8L9Sf3fMXveV2cGgxphnSvStdOgnZysltoasNd25JhqBWcJZYeOnmW1Yems7yZAxtr03NfeTqfn8FkogCvNwDF8/Q3c0DXh3aM4Q2xXiSUFBe4U5MsXeGKZC3sL9/iwVf7nk99bGGgPQBg1eth8XLo+/CjuluwRrGPo0sZZp/EcNQk6VRPKBeG697mMTlrMoQxvIKjmf6Cg5J+XjlmuMhV15Kgf35/zlr6bZIE13z1AbC1Qv3/2SjPXboqvMx7U9uga/1eB5ihbmlLLVDHN6wlZ8mFkYCstTLlbh2wHMvG18nrbZbZXB8pja8f3Ywt0+ZNKjs60l+u93LvHg9uMHk0ugGnEwwl7HZF9+MadjH5J2EqRtNLYSKMr5ZfSUCzokqQiqRj75U3IjAt/qAA6ZW1CRITp7b5uor059gQMAlfMwHgOqWwc9VBgEPT63V+ZmLv3yXpZezcjjjU1hoMqAN9peZsUU=; nseQuoteSymbols=[{"symbol":"RELIANCE","identifier":null,"type":"equity"}]; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTY3NjIxMjYzNSwiZXhwIjoxNjc2MjE2MjM1fQ._niDbiL5Hh-ZuvERBJiU7sg_kZpVCfOIF4B-bw-SSA0; bm_sv=DA89539B180A0CAE0139C52E5305ABDB~YAAQy7YRYHz/RTKGAQAAkBEPRhId5Kcu8NpzU1/tPC2gy2ornzAFuifRP/7S5h+fa/kGi+/tkan30RKJJjUXZTLmZKSHqqZupoOiAAf22R6KOe1DSczoNLcF5iK1nOQKV+kLI2Bdz1l9uAj02qJDKGKhVJ25vxy5pkFbG2L4tldWg6BfTDNYTE2uGZrQSr7UT5SlRnXoR15cjx9B9cljA3pQS5xN/QPWfaXG28XEx/CrOB1gl7hqRc2jFXsbiLhg8Cxp~1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',

}


response = requests.get(url='https://www.nseindia.com/api/chart-databyindex?index=RELIANCEEQN',headers=headers)
# %%
