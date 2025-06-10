function connectFourPlaceTokens(columns){
    let grid = new Array(6).fill(null).map(() => Array(7).fill('-'))

    function checkSpace(row, col, turn){
        if (grid[row][col] === '-'){
            if (turn % 2 === 0){
                grid[row][col] = 'R';
            }
            else{
                grid[row][col] = 'Y';
            }
            
        }else{
            checkSpace(row -= 1, col, turn)
        }
    }

    for (let i=0; i<columns.length; i++){
        let column= columns[i]
        checkSpace(5,column,i+1)
    }
    console.log(grid);
    return grid
}

connectFourPlaceTokens([0,1,0,1,0,1])