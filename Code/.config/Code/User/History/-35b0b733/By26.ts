import { createContext, ReactNode, useState } from "react";
import { AlgorithmType, MazeType, GridType } from "../utils/types";
import { createGrid } from "../utils/helpers";
import { ENDTile_TILE_CONFIGURATION, START_TILE_CONFIGURATION } from "../utils/constants";

interface PathFindingContextInterface {
  algorithm: AlgorithmType;
  setAlgorithm: (algorithum: AlgorithmType) => void;
  maze: MazeType;
  setMaze: (maze: MazeType) => void;
  grid: GridType;
  setGrid: (grid: GridType) => void;
  isGraphVisualized: boolean;
  setIsGraphVisualized: (isGraphVisualized: boolean) => void;
}

export const pathFindingContext = createContext<
  PathFindingContextInterface | undefined
>(undefined);

export const pathFindingProvider = ({ children }: { children: ReactNode }) => {
  const [algorithm, setAlgorithm] = useState<AlgorithmType>("BFS");
  const [maze, setMaze] = useState<MazeType>("NONE");
  const [grid,setGrid] = useState<GridType>(createGrid(START_TILE_CONFIGURATION,END))
};
