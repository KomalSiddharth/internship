

import requests
import json
import pandas as pd
from datetime import datetime, timedelta
base_url = "https://vegetablemarketprice.com/market/maharashtra/daywisedata?date="
image_base_url = "https://vegetablemarketprice.com"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "cookie": "_ga=GA1.1.579592366.1719805178; JSESSIONID=94BC2263A4585B7B98973770D043973E; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1723005535:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1723005535:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1723005535:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; _ga_2RYZG7Y4NC=GS1.1.1723005406.6.1.1723005422.0.0.0; FCNEC=%5B%5B%22AKsRol_kGpfj4tbq-JAcaePomD_rENfM7CoC2_i6HDJVYSw4cWOh7pQ9CXbipqMHb62O7np-PDjxheGEiTgZkJEE5FSrt9VaMjmBWfr2KCJxD3MS6AltfjtAvgrloBirs4JHC2h-PTsORX3xL8I2-nlxuCx-uNbtUg%3D%3D%22%5D%5D",
    "Referer": "https://vegetablemarketprice.com/market/maharashtra/today",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)
all_data = []
while start_date <= end_date:
    cust_date = start_date.strftime("%Y-%m-%d")
    url = f"{base_url}{cust_date}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        js_data = json.loads(response.text)
        for api in js_data["data"]:
            veg_name = str(api["vegetablename"])
            whole_price = str(api["price"])
            retail_price = str(api["retailprice"])
            shoping_mall_price = str(api["shopingmallprice"])
            unit_val = str(api["units"])
            date_collected = cust_date
            image_src_file = api["table"].get("table_image_url", "")
            image_url = f"{image_base_url}/{image_src_file}" if image_src_file else "No Image"

            new_js = {
                "Date": date_collected,
                "State_Name": "MAHARASTRA",
                "Vegetable_Name": veg_name,
                "Whole_Price": whole_price,
                "Retail_Price": retail_price,
                "Shopping_Mall_Price": shoping_mall_price,
                "units": unit_val,
                "Vegetable_Image": image_url
            }

            all_data.append(new_js)
    start_date += timedelta(days=1)
df = pd.DataFrame(all_data)
csv_path = 'Maharastra_Vegetable_Market_Prices.csv'
df.to_csv(csv_path, index=False)
df.head()
