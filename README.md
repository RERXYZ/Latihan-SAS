# Penugasan 2

Kode ini membuat kelas abstrak `Mob` untuk semua jenis mob di game. `Mob` punya atribut `mob_count` untuk menghitung total mob hidup, dan property `health` untuk nyawa. Saat `health` turun ke 0, mob mati dan `mob_count` berkurang. Ada metode `receive_damage` untuk mengurangi HP, class method `get_total_mobs` untuk menampilkan total mob, dan static method `check_spawn` untuk menentukan apakah mob bisa muncul berdasarkan level cahaya.

`Zombie` dan `Creeper` adalah subclass `Mob` yang mengimplementasikan metode `attack`. `Zombie` memukul player, sedangkan `Creeper` meledak dan langsung mati.

Di bagian main, jika level cahaya < 7, program membuat Zombie dan Creeper, menampilkan total mob, lalu setiap mob menyerang dan menerima damage 10. Setelah itu, total mob yang masih hidup ditampilkan kembali.

Contoh outputnya:

```
Total Mob: 2
Zombie memukul player.
Zombie sisa HP: 10
----------
Creeper meledak!
Creeper mati.
Creeper sisa HP: 0
----------
Total Mob: 1
```
