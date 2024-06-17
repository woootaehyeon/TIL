function solution(ineq, eq, n, m) {
    var answer = 0;
    var flag = '';
    flag = flag + ineq + eq;
    if(flag == '>='){
        if(n >= m){
            answer = 1;
        } else {
            answer = 0;
        }
    } else if(flag == '<='){
        if(n <= m) {
            answer = 1;
        }
    } else if(flag == '>!'){
        if(n > m) {
            answer = 1;
        }
    } else if(flag == '<!'){
        if(n < m) {
            answer = 1;
        }
    }
    return answer;
}