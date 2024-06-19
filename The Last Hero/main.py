import os
from karakter import Ksatria, TacetDiscord, Phoenix
from senjata import FireBreath, Sword, Axe, SamuraiSword, Claws

def main():
   
    nama_ksatria = input("Masukkan nama untuk Hero: ")

    
    while True:
        print("Pilih senjata untuk Ksatria:")
        print("1. Pedang - Damage: 50, Durability: 50")
        print("2. Kapak - Damage: 60, Durability: 40")
        print("3. Samurai Sword - Damage: 70, Durability: 60")

        pilihan_senjata = input("Masukkan pilihan (1/2/3): ")

        if pilihan_senjata == "1":
            senjata_ksatria = Sword
            break

        elif pilihan_senjata == "2":
            senjata_ksatria = Axe
            break

        elif pilihan_senjata == "3":
            senjata_ksatria = SamuraiSword
            break
        else:
            print("Pilihan tidak ada.")

    # Prompt pengguna untuk memilih lawan
    while True:
        print("Pilih lawan:")
        print("1. Naga")
        print("2. Phoenix")

        pilihan_lawan = input("Masukkan pilihan (1/2): ")

        if pilihan_lawan == "1":
            musuh = TacetDiscord(nama="Tacet Discord", health=2100, weapons=[Claws, FireBreath])
            break

        elif pilihan_lawan == "2":
            musuh = Phoenix(nama="Phoenix", health=2500, weapons=[Claws, FireBreath])
            break
        else:
            print("Pilihan tidak ada.")

    ksatria = Ksatria(nama=nama_ksatria, health=2600)
    ksatria.use(senjata_ksatria)

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        ksatria.attack(musuh)
        if musuh.health == 0:
            print(f"{musuh.nama} telah mati!")
            break

        musuh.attack(ksatria)
        if ksatria.health == 0:
            print(f"{ksatria.nama} telah gugur!")
            break

        ksatria.nyawa.draw()
        musuh.nyawa.draw()

        choice = input("Tekan Enter untuk serang / ketik 'x' untuk exit: ")
        if choice.lower() == 'x':
            print("Aplikasi Ditutup")
            return

    while True:
        choice = input("Ketik 'y' untuk main lagi atau 'x' untuk keluar: ").lower()
        if choice == 'y':
            main()
            return
        elif choice == 'x':
            print("Aplikasi Ditutup")
            return
        else:
            print("Invalid input. Pilih 'y' atau 'x'.")

if __name__ == "__main__":
    main()
