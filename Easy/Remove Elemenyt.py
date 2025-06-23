def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in nums[:]:
        if i == val:
            nums.remove(i)
        else:
            k += 1
    return k

'''nums[:] → returns a new list containing the same integers.

Iteration happens on the copy, so removing from the original doesn’t interfere with your loop.

If you’d iterated directly over nums, doing nums.remove(i) while looping would skip elements or even raise errors. Using the slice sidesteps that by decoupling the loop from the list you’re mutating.'''