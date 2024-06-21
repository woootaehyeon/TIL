function solution(my_strings, parts) {
    var answer = '';
    for (let i = 0; i < parts.length; i++) {
        let start = parts[i][0];
        let length = parts[i][1] - start + 1;
        answer += my_strings[i].substr(start, length);
    }
    return answer;
}
