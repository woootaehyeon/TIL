function solution(a, b) {
    let value1 = a.toString() + b.toString();
    let value2 = b.toString() + a.toString();
    let answer;
    
    if (Number(value1) > Number(value2)){
        answer = Number(value1)
    } else {
        answer = Number(value2)
    }
    return answer;
}