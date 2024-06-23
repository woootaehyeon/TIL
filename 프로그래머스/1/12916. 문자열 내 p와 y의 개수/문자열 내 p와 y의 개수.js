function solution(s){
    var answer = true;
    let cnt_p = 0;
    let cnt_y = 0;
    for(let i = 0; i < s.length; i++){
        if(s[i] == 'p' || s[i] == 'P'){
            cnt_p++;
        }
        else if(s[i] == 'y' || s[i] == 'Y'){
            cnt_y++;
        }
    }
    if(cnt_p == cnt_y){
        answer = true;
    } else {
        answer = false;
    }
    return answer;
}