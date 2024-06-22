function solution(my_string, m, c) {
    var answer = '';
    let num = Number(my_string.length / m);
    for(let i = c - 1; i < my_string.length; i += m){
        answer = answer + my_string[i];
    }
    return answer;
}