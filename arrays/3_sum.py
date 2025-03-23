nums = [-1,0,1,2,-1,-4]

triplets = []

sorted_nums = sorted(nums)

i = 0

while i < len(sorted_nums):

    j, k = i + 1, len(nums) - 1

    """
    just like we are cheking the duplicates for j and k below we are doing the same for i here. 
    """
    if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
        continue

    # for the same i, we gotta check the following things
    while j < k:

        sum_of_nums = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

        if sum_of_nums == 0:
            """ 
            we are not checking if the triplet already exists inside the triplets list because below we are skipping the duplicates by running 2 more while loops
            one is going to check if j is same as the previous one, if so skip it by increamenting j
            another is going to do the same for k
             """ 
            triplets.append(sorted_nums[i], sorted_nums[j], sorted_nums[k])

            while j < k and sorted_nums[j] == sorted_nums[j + 1]:
                j += 1

            while j < k and sorted_nums[k] == sorted_nums[k - 1]:
                k -= 1

            j += 1
            k -= 1

        elif sum_of_nums < 0:
            j += 1

        elif sum_of_nums > 0:
            k -= 1

    i += 1