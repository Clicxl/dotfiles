import { createContext, ReactNode, useState } from "react";
import { TileType } from "../utils/types";

export interface SpeedContextInterface {
    speed: SpeedType
}

export const SpeedContext = createContext<SpeedContextInterface | undefined> (undefined);

export const SpeedProvider = ({children}: {children: ReactNode})  => {

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