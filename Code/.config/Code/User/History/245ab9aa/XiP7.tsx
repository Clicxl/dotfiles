import { createContext, ReactNode, useState } from "react";
import { TileType } from "../utils/types";
import { END_TILE_CONFIGURATION, START_TILE_CONFIGURATION } from "../utils/constants";

export interface SpeedContextInterface {
    startTile: TileType;
    setStartTile: (startTile: TileType) => void;
    endTile: TileType;
    setEndTile: (endTile: TileType) => void;
}

export const SpeedContext = createContext<SpeedContextInterface | undefined> (undefined);

export const SpeedProvider = ({children}: {children: ReactNode})  => {
    const [startTile, setStartTile] =useState<TileType>(START_TILE_CONFIGURATION)
    const [endTile, setEndTile] =useState<TileType>(END_TILE_CONFIGURATION)

    return (
        <SpeedContext.Provider value={
{            startTile,
            setStartTile,
            endTile,
            setEndTile
}        }>
            {children}
        </SpeedContext.Provider>

    )


}