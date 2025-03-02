function findDisappearedNumbers(nums: number[]): number[] {
    /**
    create set with nums
    loop from 1 .. nums.size
        if current index not in set:
            add to []

    return []
     */
    let numSet = new Set(nums);
    let output: number[] = [];
    for (let i = 1; i <= nums.length; i++) {
        if (!numSet.has(i)) {
            output.push(i)
        }
    }

    return output;
};