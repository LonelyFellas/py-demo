import requests
from typing import List

url = 'http://maiku.npaas.cn/s/api/file/getAll'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Content-type': 'application/json',
    'X-Token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzE2MzU3ODU3LCJleHAiOjE3MTY5NTc4NTd9.lDokMOZD11QKTj14JI6k83B17HCAaIixXt2LkUGbPzM"
}


def get_files_service() -> List:
    """ 查询我中转站上传的所有文件 """
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get('data')
    else:
        return []
