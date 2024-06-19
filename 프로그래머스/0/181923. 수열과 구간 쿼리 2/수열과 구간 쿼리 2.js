function solution(arr, queries) {
    var answer = [];
    for(let i = 0; i < queries.length; i++){
        let max = 1000000;
        let min = -1;
        for(let j = queries[i][0]; j < queries[i][1]+1; j++){
            if(arr[j] > queries[i][2] && arr[j] < max){
                min = arr[j];
                max = min;
            }
        } answer.push(min);
    }
    return answer;
}