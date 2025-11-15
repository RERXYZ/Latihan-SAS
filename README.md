# Penugasan 1

## Fitur

### 1. Tambah Todo

Menambahkan satu atau lebih kegiatan ke hari tertentu.

### 2. Tampilkan Todo

Menampilkan jadwal berdasarkan hari yang dipilih.
Jika mengetik **`semua`**, maka seluruh hari akan ditampilkan.

### 3. Tampilkan Todo Tertentu

Menampilkan jadwal untuk satu hari tertentu.

### 4. Update Todo

Mengganti seluruh isi jadwal untuk hari tertentu.

### 5. Hapus Todo

Menghapus semua jadwal pada hari yang dipilih.

### 6. Keluar

Menutup program.

## Struktur Data

Program menggunakan dictionary bernama `schedule`:

```python
schedule = {
    'monday': [],
    'tuesday': [],
    'wednesday': [],
    'thursday': [],
    'friday': [],
    'saturday': [],
    'sunday': [],
}
```

Setiap hari menyimpan list kegiatan (*todo*).

## Fungsi Utama

### `create(day, *todo)`

Menambah kegiatan ke hari tertentu.

### `read(*days)`

Menampilkan jadwal:

* Jika input `semua`, semua hari ditampilkan.
* Jika input beberapa hari (dipisahkan koma), semua akan ditampilkan berurutan.

### `find(day)`

Menampilkan jadwal satu hari.

### `update(day, *todo)`

Mengganti seluruh isi jadwal hari tersebut.

### `delete(day)`

Menghapus semua jadwal pada hari tersebut.

## Flow Program (`main()`)

Program berjalan dalam loop dan menampilkan menu:

```
1. Tambah todo
2. Tampilkan todo
3. Tampilkan todo tertentu
4. Update todo
5. Hapus todo
6. Keluar
```

User memilih menu, lalu program menjalankan fungsi sesuai pilihan.