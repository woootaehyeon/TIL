function solution(a, d, included) {
    let arr = [];
    let num = a;
    let answer = 0;
    for(let i = 0; i < included.length; i++){
        arr.push(num);
        num += d;
    }
    for(let j = 0; j < included.length; j++){
        if(included[j] == true){
            answer = answer + arr[j];
        }
    }
    return answer;
}