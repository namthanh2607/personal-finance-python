import json
import os

FILE_NAME = "chi_tieu.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    danh_sach = load_data()
    
    while True:
        print("\n=================================")
        print("   APP QUẢN LÝ CHI TIÊU CÁ NHÂN  ")
        print("=================================")
        print("1. Xem danh sách chi tiêu")
        print("2. Thêm khoản chi tiêu mới")
        print("3. Xem tổng số tiền đã tiêu")
        print("4. Thoát")
        
        chon = input("Nhập lựa chọn của bạn (1-4): ")
        
        if chon == "1":
            if not danh_sach:
                print("\n⚠️ Chưa có khoản chi tiêu nào!")
            else:
                print("\n📋 DANH SÁCH CHI TIÊU:")
                for idx, item in enumerate(danh_sach, 1):
                    print(f"{idx}. {item['ten']}: {item['so_tien']:,} VNĐ")
        
        elif chon == "2":
            ten = input("\nNhập tên khoản chi (VD: Cơm trưa): ")
            try:
                so_tien = int(input("Nhập số tiền (VNĐ): "))
                danh_sach.append({"ten": ten, "so_tien": so_tien})
                save_data(danh_sach)
                print(f"✅ Đã thêm: {ten} - {so_tien:,} VNĐ thành công!")
            except ValueError:
                print("❌ Lỗi: Số tiền phải nhập bằng số!")
                
        elif chon == "3":
            tong = sum(item['so_tien'] for item in danh_sach)
            print(f"\n💰 TỔNG SỐ TIỀN BẠN ĐÃ TIÊU: {tong:,} VNĐ")
            
        elif chon == "4":
            print("\nCảm ơn bạn đã sử dụng App! Tạm biệt 👋")
            break
        else:
            print("\n❌ Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()