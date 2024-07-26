import { MAX_COLS, MAX_ROWS } from "./constants";
import { GridType, TileType } from "./types";


const createGrid(row:number, startTile:TileType, endTile:TileType):TileType[] {
    const currRow = [];
    for (let col = 0; col < MAX_COLS; col++){
        currRow.push({
            row,
            col,
            isEnd: row === endTile.row && col == endTile.col,
            isWall: false,
            isPath: false,
            distance: Infinity,
            isStart: row == startTile.row && col == startTile.col,
            isTraversed: false,
            parent: null

        })
    }
    return currRow
}


export const createGrid = (startTile:TileType, endTile:TileType) => {
    const grid:GridType = [];

    for (let row = 0; row < MAX_ROWS; row++) {
        grid.push(createRow(row, startTile, endTile))
    }
}