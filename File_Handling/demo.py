# with open('input.txt', 'r') as f, open('output1.txt', 'w') as f2:
#     f2.writelines(f.read())

# with open('input.txt', 'r') as f1:
#     with open('output.txt', 'w') as f2:
#         f2.write(f1.read())

# with open('input.txt', 'r') as f1:
#     with open('output3.txt', 'w') as f2:
#         f2.writelines(f1.read())

# with open('input.txt', 'r') as f1:
#     with open('output.txt', 'w') as f2:
#         f2.write(f1.readlines())				# ERROR
        
with open('input.txt', 'r') as f1:
    with open('output4.txt', 'w') as f2:
        f2.writelines(f1.readlines())
