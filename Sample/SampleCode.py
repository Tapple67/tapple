class StockMarket:
    def __init__(self):
        self.stock_prices = {
            "삼성전자": 55000,
            "카카오": 37000,
            "네이버": 180000
        }
        self.user_portfolio = {}

    def show_stock_list(self):
        print("\n📈 현재 주식 리스트:")
        for name, price in self.stock_prices.items():
            print(f" - {name}: {price}원")

    def search_stock(self, keyword):
        print(f"\n🔍 '{keyword}' 검색 결과:")
        found = False
        for name, price in self.stock_prices.items():
            if keyword in name:
                print(f" - {name}: {price}원")
                found = True
        if not found:
            print(" - 해당 종목이 없습니다.")

    def buy_stock(self, name, quantity):
        if name not in self.stock_prices:
            print("❌ 존재하지 않는 종목입니다.")
            return
        self.user_portfolio[name] = self.user_portfolio.get(name, 0) + quantity
        print(f"✅ {name} {quantity}주 매수 완료.")

    def show_portfolio(self):
        print("\n📁 보유 종목:")
        if not self.user_portfolio:
            print(" - 보유 종목이 없습니다.")
        else:
            for name, qty in self.user_portfolio.items():
                print(f" - {name}: {qty}주")

    def sell_stock(self, name, quantity):
        if self.user_portfolio.get(name, 0) < quantity:
            print("❌ 보유 주식 수량이 부족합니다.")
            return
        self.user_portfolio[name] -= quantity
        if self.user_portfolio[name] == 0:
            del self.user_portfolio[name]
        print(f"✅ {name} {quantity}주 매도 완료.")


def main():
    market = StockMarket()

    while True:
        print("\n=== 토스 증권 탭 ===")
        print("1. 주식 리스트 보기")
        print("2. 종목 검색")
        print("3. 주식 매수")
        print("4. 보유 종목 확인")
        print("5. 주식 매도")
        print("0. 종료")
        choice = input("선택: ")

        if choice == "1":
            market.show_stock_list()
        elif choice == "2":
            keyword = input("검색할 종목 이름: ")
            market.search_stock(keyword)
        elif choice == "3":
            name = input("매수할 종목명: ")
            qty = int(input("수량: "))
            market.buy_stock(name, qty)
        elif choice == "4":
            market.show_portfolio()
        elif choice == "5":
            name = input("매도할 종목명: ")
            qty = int(input("수량: "))
            market.sell_stock(name, qty)
        elif choice == "0":
            print("👋 종료합니다.")
            break
        else:
            print("❗ 올바른 번호를 입력하세요.")


if __name__ == "__main__":
    main()
