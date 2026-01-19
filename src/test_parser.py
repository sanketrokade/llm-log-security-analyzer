from log_parser import read_log_file, filter_important_lines, chunk_lines

lines = read_log_file("logs/sample.log")
important = filter_important_lines(lines)
chunks = chunk_lines(important)

print("Important lines:")
for line in important:
    print(line)

print("\nChunks:")
print(chunks)
