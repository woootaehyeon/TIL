function solution(a, b) {
    var answer = 0;
    let value1 = Number(a.toString() + b.toString());
    let value2 = 2 * a * b;
    if (value1 > value2){
        answer = value1;
    } else {
        answer = value2;
    }
    return answer;
}