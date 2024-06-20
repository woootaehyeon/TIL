function solution(number) {
    var answer = 0;
    let num = 0;
    for(let i = 0; i < number.length; i++){
        num = num + Number(number[i]);
    }
    answer = num % 9;
    return answer;
}