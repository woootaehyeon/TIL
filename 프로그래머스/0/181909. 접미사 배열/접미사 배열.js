function solution(my_string) {
    var answer = [];
    for(let i = my_string.length -1; i > -1; i--){
        let s = my_string.slice(i,my_string.length);
        answer.push(s);
    }
    answer = answer.sort();
    return answer;
}