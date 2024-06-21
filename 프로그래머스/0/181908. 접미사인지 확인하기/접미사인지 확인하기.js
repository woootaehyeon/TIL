function solution(my_string, is_suffix) {
    var answer = [];
    let TF = 0;
    for(let i = my_string.length -1; i > -1; i--){
        let s = my_string.slice(i,my_string.length);
        answer.push(s);
    }
    for(let i = 0; i < answer.length; i++){
        if(answer[i] == is_suffix){
            TF = 1;
        }
    }
    return TF;
}