import { createContext, ReactNode } from "react";
import { TileType } from "../utils/types";

interface TileContextInterface {
    startTile: TileType;
    setStartTile: (startTile: TileType) => void;
    endTile: TileType;
    setEndTile: (endTile: TileType) => void;
}

export const TileContext = createContext<TileContextInterface | undefined> (undefined);

export const TileProvider = ({children}: {children: ReactNode})  => {
    
}