import { createContext, ReactNode, useState } from "react";
import { TileType } from "../utils/types";
import { START_TILE_CONFIGURATION } from "../utils/constants";

interface TileContextInterface {
    startTile: TileType;
    setStartTile: (startTile: TileType) => void;
    endTile: TileType;
    setEndTile: (endTile: TileType) => void;
}

export const TileContext = createContext<TileContextInterface | undefined> (undefined);

export const TileProvider = ({children}: {children: ReactNode})  => {
    const [startTile, setStartTile] =useState<TileType>(START_TILE_CONFIGURATION)

}