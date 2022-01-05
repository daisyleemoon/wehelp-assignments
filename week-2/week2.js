//要求一
function calculate(min, max) {
  return console.log(((min + max) * (max - min + 1)) / 2);

  // let arrA = [];
  // for (i = min; i < max + 1; i++) {
  //   arrA.push(i);
  // }
  // let sum = arrA.reduce((acc, cur) => {
  //   return acc + cur;
  // }, 0);
  // console.log(sum);
}

calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

// x..y
// -5..10
// == (X..-1) + (1..Y)
// == (x-1)*(-x)/2 + (y+1)*y/2
// == (-x^2+x+y^2+y)/2
// == (y+x)(y-x+1)/2

//要求二
function avg(data) {
  let accountInfo = data;
  let totalSalary = 0;

  for (i = 0; i < accountInfo.employees.length; i++) {
    totalSalary += accountInfo.employees[i].salary;
  }
  let avgSalary = totalSalary / accountInfo.employees.length;
  return console.log(avgSalary);
}

function avg2(data) {
  let totalSalary = 0;
  data.employees.forEach((employee) => {
    totalSalary += employee.salary;
  });
}

function avg3(data) {
  return (
    data.employees.reduce((totalSalary, employee) => {
      totalSalary += employee.salary;
    }, 0) / data.count
  );
}

avg({
  count: 3,
  employees: [
    {
      name: "John",
      salary: 30000,
    },
    {
      name: "Bob",
      salary: 60000,
    },
    {
      name: "Jenny",
      salary: 50000,
    },
  ],
});

//要求三
function maxProduct(nums) {
  if (nums.length < 2) {
    return "invalid input";
  }
  let max1 = nums[0];
  let max2 = nums[1];
  let min1 = nums[0];
  let min2 = nums[1];
  if (max2 > max1) {
    [max1, max2] = [max2, max1];
  }
  if (min2 < min1) {
    [min1, min2] = [min2, min1];
  }

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] > max2) {
      if (nums[i] > max1) {
        [max1, max2] = [nums[i], max1];
      } else {
        max2 = nums[i];
      }
    }
    if (nums[i] < min2) {
      if (nums[i] < min1) {
        [min1, min2] = [nums[i], min1];
      } else {
        min2 = nums[i];
      }
    }
  }

  let product1 = max1 * max2;
  let product2 = min1 * min2;
  return console.log(product1 > product2 ? product1 : product2);
}
maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0
maxProduct([-1, -2, 0]); // 得到 2

//要求四

function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      if (diff == nums[j]) {
        return `[${i}, ${j}]`;
      }
    }
  }
  return "not match";
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
