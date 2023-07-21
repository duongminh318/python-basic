while True:
    hten= input("nhap ten: ")
    mhoc= input("nhap mon hoc: ")
    diem= float(input("nhap diem: "))
    print(f"hoc sin: {hten} --- du thi mon {mhoc}"
          f"-- co diem {diem}")
    if diem>=7:
        print("xep loai diem : Dat")
    else:
        print("xep loai diem : Khong Dat")
    hoi= input("nhap n de thoat, hoac bam phim bat ky de tiep tuc: ")
    if hoi=="n" or hoi=="N":
        break