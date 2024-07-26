import { TileType } from "../utils/types";

interface TileContentInterface {
    startTile: TileType,
    setStartTile: (startTile: TileType) => void;
    endTile: TileType,
    setEndTile: (endTile: TileType) => void

}