import os

print("=== dist目录内容 ===\n")
files = sorted(os.listdir('dist'))
total_size = 0

for f in files:
    path = os.path.join('dist', f)
    size = os.path.getsize(path)
    size_mb = size / 1024 / 1024
    total_size += size
    print(f"{f:<40} {size_mb:>8.2f} MB")

print("-" * 50)
print(f"{'总计':<40} {total_size/1024/1024:>8.2f} MB")

