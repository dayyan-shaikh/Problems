nums = [2,7,8,3,5]
target = 9

for(let i=0;i<nums.length;i++){
    for(let j=0;j<i+1,nums.length;j++){
        if(nums[i] + nums[j] == target){
            console.log([i,j])
        }
    }
}