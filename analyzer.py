
import csv
from collections import defaultdict

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

def main():
    rows = read_csv("sample.csv")
    total = sum_by_month(rows)
    for month, total_amount in sorted(total.items()):
        print(f"{month}总花费: {total[month]}")

if __name__ == "__main__":
    main()


