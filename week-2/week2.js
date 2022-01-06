//要求一
function calculate(min, max) {
  return console.log(((min + max) * (max - min + 1)) / 2);
  // solution ver.1 can work, but is not efficiency
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

// proof f(((min + max) * (max - min + 1)) / 2) can work
// x..y
// == (X..-1) + (1..Y)
// == (x-1)*(-x)/2 + (y+1)*y/2
// == (-x^2+x+y^2+y)/2
// == (y+x)(y-x+1)/2

//要求二
function avg(data) {
  let totalSalary = 0;
  for (i = 0; i < data.employees.length; i++) {
    totalSalary += data.employees[i].salary;
  }
  let avgSalary = totalSalary / data.employees.length;
  return console.log(avgSalary);
}

//use forEach or reduce find the solution
// function avg(data) {
//   let totalSalary = 0;
//   data.employees.forEach((employee) => {
//     totalSalary += employee.salary;
//   });
//   console.log(totalSalary / data.employees.length);
// }

// function avg(data) {
//   if (data.count != data.employees.length) {
//     return "acccount information invalid";
//   } else {
//     avgSalary =
//       data.employees.reduce((totalSalary, employee) => {
//         totalSalary += employee.salary;
//         return totalSalary;
//       }, 0) / data.count;
//   }
//   console.log(avgSalary);
// }

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
  let copyNums = Array.from(nums);
  copyNums.sort((a, b) => a - b);
  let head = copyNums[0];
  let tail = copyNums[copyNums.length - 1];

  while (copyNums.indexOf(tail) - copyNums.indexOf(head) > 1) {
    if (head + tail > target) {
      tail = copyNums[copyNums.indexOf(tail) - 1];
    }
    if (head + tail < target) {
      head = copyNums[copyNums.indexOf(head) + 1];
    }
    if (head + tail == target) {
      [head, tail] = [head, tail];
    }
  }
  if (head + tail == target) {
    return [nums.indexOf(head), nums.indexOf(tail)];
  } else return "not match";

  // solution ver.1
  // for (let i = 0; i < nums.length; i++) {
  //   let diff = target - nums[i];
  //   for (let j = i + 1; j < nums.length; j++) {
  //     if (diff == nums[j]) {
  //       return `[${i}, ${j}]`;
  //     }
  //   }
  // }
  // return "not match";
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

//要求五
function maxZeros(nums) {
  let counter = 0;
  let maxLength = 0;

  nums.forEach((num) => {
    if (num == 0) {
      counter++;
      if (counter > maxLength) {
        maxLength = counter;
      }
    }
    if (num == 1) {
      counter = 0;
    }

    return maxLength;
  });
  console.log(maxLength);
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]); // 得到 3
