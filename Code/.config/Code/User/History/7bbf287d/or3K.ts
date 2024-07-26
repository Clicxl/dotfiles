import { MAX_ROWS } from "./constants";
import { GridType, TileType } from "./types";


const createGrid(row:number, startTile:TileType, endTile:TileType) {
    const currRow = [];
    

}


export const createGrid = (startTile:TileType, endTile:TileType) => {
    const grid:GridType = [];

    for (let row = 0; row < MAX_ROWS; row++) {
        grid.push(createRow(row, startTile, endTile))
    }
}