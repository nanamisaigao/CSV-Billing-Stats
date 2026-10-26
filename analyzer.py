
import csv
from collections import defaultdict

CATEGORY_ORDER = ["餐饮", "交通", "购物"]

def read_csv(path):
    """读 CSV，返回所有行的列表，每行是字典。"""
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def sum_by_month(rows):
    """按月份累加金额，返回 {月份: 总花费}。"""
    total = defaultdict(float)
    for row in rows:
        month=row["日期"][:-3]
        total[month] += float(row["金额"])
    return total

def sum_by_month_category(rows):
    """返回 {月份: {类别: 金额}}。"""
    total = defaultdict(lambda: defaultdict(float))
    for row in rows:
        month=row["日期"][:-3]
        category=row["类别"]
        total[month][category] += float(row["金额"])
    return total

def main():
    rows = read_csv("sample.csv")
    data = sum_by_month_category(rows)
    grand_total = 0.0
    for month in sorted(data):
        month_total = sum(data[month].values())
        grand_total += month_total
        print(f"{month} 总花费: {month_total}")
        for category in CATEGORY_ORDER:
            amount = data[month].get(category,0.0)
            pct=amount/month_total*100
            print(f"  {category}: {amount:.1f} ({pct:.1f}%)")
        print()

    print(f"总计: {grand_total:.1f}")

if __name__ == "__main__":
    main()


