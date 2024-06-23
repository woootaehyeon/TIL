function solution(cards1, cards2, goal) {
    let index1 = 0;  // Pointer for cards1
    let index2 = 0;  // Pointer for cards2
    
    for (let i = 0; i < goal.length; i++) {
        if (index1 < cards1.length && goal[i] === cards1[index1]) {
            index1++;
        } else if (index2 < cards2.length && goal[i] === cards2[index2]) {
            index2++;
        } else {
            return 'No';
        }
    }
    return 'Yes';
}
