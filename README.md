# Google Maps Review Indonesia

## Installation

Commit Project

```bash
  git commit https://github.com/aldidaim21/Maps-Aldi
```

## Buat Akun Serpapi

**Kunjungi website serpapi**

`https://serpapi.com/`

**Kunjungi website serpapi**

`pada bagian api key copy Your Private API Key
`

## Get Place ID for app.py

- Pada bagian example env rename file tersebut menjadi .env

- Ubah Token Dengan Serpapi Token Akun Untuk Token dapat diperoleh disini https://serpapi.com/manage-api-key

```python
SERPAPI_KEY="isi dengan token serpapi akun masing masing"
```

- Buka app2.python, Untuk kode ini dapat diganti dengan latitude dan longitude daerah yang diinginkan

```python
"q": "Gacoan Terdekat", #ini bisa diganti dengan keyword lain
"ll": "@-6.8731527,107.5423099,10z",
```

- Ketika dijalankan akan terdapat data json
- cari place id nantinya dibutuhkan di app.py

## Running Scrapping

#app.py

Untuk kode ini dapat diganti dengan place id yang diinginkan yang diperoleh dari run kode app2.py

```python
place_id = "ChIJK--RT9TnaC4R3vmpjNmLKMQ"
```

nama csv dapat disesuaikan

```python
csv_file = "GacoanReview.csv"
```
