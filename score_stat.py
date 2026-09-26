def main():
    scores = [85,92,78,90,66,77,88,95]
    total = sum(scores)
    avg = total / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    print("=====成绩统计结果====")
    print(f"总分：{total}")
    print(f"平均分：{avg:.2f}")
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")

if __name__ == "__main__":
    main()
