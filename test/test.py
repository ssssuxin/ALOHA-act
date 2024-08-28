import random
# print(help(random))
# def test_random_seed_in_std_lib(seed=0, cnt=3):
#     random.seed(seed)
#     print("test seed: ", seed)
#     for _ in range(cnt):
#         print(random.random())
#         print(random.randint(0,100))
#         print(random.uniform(1, 10))
#         print('\n')


# test_random_seed_in_std_lib()
# test_random_seed_in_std_lib()
# test_random_seed_in_std_lib(100)
# test_random_seed_in_std_lib()

random.seed(0)
print(random.random())
print(random.random())
print(random.random())
random.seed(0)
print(random.random())
print(random.random())