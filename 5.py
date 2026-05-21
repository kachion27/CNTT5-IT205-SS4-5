id_user = 0
tong_hoa_don = 0
don_lon_hon_1tr = 0

loop = True

while loop:
    try:
        hoa_don = int(input(f"Khách hàng {id_user+1} - Nhập giá trị đơn hàng: "))
        if (hoa_don >= 1_000_000):
            don_lon_hon_1tr += 1
        tong_hoa_don += hoa_don
    except ValueError:
        print("Lỗi : giá trị không hợp lệ")
        continue
    id_user += 1
    
    while True:
        xac_nhan = input("Có muốn tiếp nhận không? (C/K)").lower().strip()
        if (xac_nhan == "c" or xac_nhan == "k"):
            if(xac_nhan == "c"):
                break
            elif(xac_nhan == "k"):
                loop = False
                break
        else:
            print("Cú pháp không hợp lệ mời nhập lại")
        
tinh_ti_le = (don_lon_hon_1tr / id_user) * 100
print("\n")
print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print(f"Tổng số hóa đơn đã xử lý: {id_user} hóa đơn")
print(f"Tổng doanh thu ngày hôm nay: {tong_hoa_don} VNĐ")
print(f"Số hóa đơn lớn hơn 1,000,000 VNĐ : {don_lon_hon_1tr} hóa đơn")
print(f"Tỷ lệ hóa đơn lớn đạt : {float(tinh_ti_le)}% trên tổng số đơn hàng")